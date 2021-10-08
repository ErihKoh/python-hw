import sys
from pathlib import Path
import shutil
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

import scan
from normalize import normalize


def handle_image(root_folder: Path, dist: str):
    for file in scan.IMAGE:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)


def handle_video(root_folder: Path, dist: str):
    for file in scan.VIDEO:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)


def handle_audio(root_folder: Path, dist: str):
    for file in scan.AUDIO:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)


def handle_doc(root_folder: Path, dist: str):
    for file in scan.DOC:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)


def handle_other(root_folder: Path, dist: str):
    for file in scan.OTHER:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)


def handle_archive(root_folder: Path, dist):
    for file in scan.ARCH:
        target_folder = root_folder / dist
        target_folder.mkdir(exist_ok=True)
        ext = Path(file).suffix
        folder_for_archive = normalize(file.name.replace(ext, ""))
        archive_folder = target_folder / folder_for_archive
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


workers = scan.REGISTERED_EXTENSIONS.keys()


def main(folder):
    thr = Thread(target=scan.scan, args=(folder,))
    thr.start()
    thr.join()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.submit(handle_image, folder, 'images')
        executor.submit(handle_video, folder, 'video')
        executor.submit(handle_audio, folder, 'audio')
        executor.submit(handle_doc, folder, 'documents')
        executor.submit(handle_other, folder, 'other')
        executor.submit(handle_archive, folder, 'archives')

    for item in scan.FOLDERS:
        handle_folder(item)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)

    main(sort_folder.resolve())
