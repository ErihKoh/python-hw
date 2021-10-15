import sys
from pathlib import Path
import shutil
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import scan
from normalize import normalize


def handle_files(root_folder: Path, folder_for_sort, dist: str):
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


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        pass


workers = len(scan.REGISTERED_EXTENSIONS.keys())


def main(folder):
    scan.scan(folder)
    for thr in scan.threads:
        thr.join()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.submit(handle_files, folder, scan.IMAGE, 'images')
        executor.submit(handle_files, folder, scan.VIDEO, 'video')
        executor.submit(handle_files, folder, scan.AUDIO, 'audio')
        executor.submit(handle_files, folder, scan.DOC, 'documents')
        executor.submit(handle_files, folder, scan.OTHER, folder, 'other')
        executor.submit(handle_files, folder, scan.ARCH, 'archives')

    for item in scan.FOLDERS:
        handle_folder(item)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)

    main(sort_folder.resolve())
