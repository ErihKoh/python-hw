import sys
from pathlib import Path
import shutil
import asyncio
import aiopath

import scan
from normalize import normalize


async def handle_files(root_folder, folder_for_sort, dist: str):
    for file in folder_for_sort:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext

        if dist != 'archives':
            await file.replace(target_folder / new_name)
        else:
            archive_folder = target_folder / new_name
            async_folder = aiopath.AsyncPath(archive_folder)
            await async_folder.mkdir(exist_ok=True)
            try:
                async_file = aiopath.AsyncPath(file)
                shutil.unpack_archive(str(async_file), str(async_folder))
            except shutil.ReadError:
                archive_folder.rmdir()
                return
            await file.unlink()


async def handle_folder(folder):
    try:
        await folder.rmdir()
    except OSError:
        pass


async def main(folder):
    path = aiopath.AsyncPath(folder)
    await scan.scan(path)

    await handle_files(folder, scan.IMAGE, 'images')
    await handle_files(folder, scan.VIDEO, 'video')
    await handle_files(folder, scan.AUDIO, 'audio')
    await handle_files(folder, scan.DOC, 'documents')
    await handle_files(folder, scan.OTHER, 'other')
    await handle_files(folder, scan.ARCH, 'archives')

    for item in scan.FOLDERS:
        await handle_folder(item)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())
    asyncio.run(main(sort_folder.resolve()))
