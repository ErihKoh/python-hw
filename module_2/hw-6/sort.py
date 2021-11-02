import sys
from pathlib import Path
import shutil
import asyncio
import scan
from normalize import normalize


async def handle_files(root_folder: Path, folder_for_sort, dist: str):
    for file in folder_for_sort:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext

        if dist != 'archives':
            file.replace(target_folder / new_name)
        else:
            archive_folder = target_folder / new_name
            archive_folder.mkdir(exist_ok=True)
            try:
                shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
            except shutil.ReadError:
                archive_folder.rmdir()
                return
            file.unlink()


async def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        pass


async def main(folder):
    await scan.scan(folder)

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
