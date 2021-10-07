import sys
from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor
import scan
from normalize import normalize


def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    print(target_folder)
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_video(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_audio(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_doc(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_other(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dist):
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


def main(folder):
    scan.scan(folder)

    for file in scan.IMAGE:
        handle_image(file, folder, "images")

    for file in scan.VIDEO:
        handle_video(file, folder, "video")

    for file in scan.AUDIO:
        handle_audio(file, folder, "audio")

    for file in scan.DOC:
        handle_doc(file, folder, "documents")

    for file in scan.OTHER:
        handle_other(file, folder, "other")

    for file in scan.ARCH:
        handle_archive(file, folder, "archives")

    for item in scan.FOLDERS:
        handle_folder(item)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())
    # main(sort_folder.resolve())
