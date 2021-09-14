import shutil
from sys import argv
import re
from pathlib import Path


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "e", "u", "ja")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str):
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name


IMAGE = []
VIDEO = []
DOC = []
AUDIO = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "IMAGE": IMAGE,
    "VIDEO": VIDEO,
    "DOC": DOC,
    "AUDIO": AUDIO,
    "ARCH": ARCH,
    "OTHER": OTHER,
}


def get_extension(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("images", "video", "audio", "documents", "other", "archives"):
                FOLDERS.append(item)
                scan(item)
            continue
        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                if extension in ("JPEG", "JPG", "SVG", "PNG"):
                    current_container = REGISTERED_EXTENSIONS["IMAGE"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
                elif extension in ("MP4", "MPEG", "WMV", "MOV", "MKV", "3gp", "AVI"):
                    current_container = REGISTERED_EXTENSIONS["VIDEO"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
                elif extension in "MP3":
                    current_container = REGISTERED_EXTENSIONS["AUDIO"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
                elif extension in ("DOC", "DOCX", "TXT", "PDF"):
                    current_container = REGISTERED_EXTENSIONS["DOC"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
                elif extension in ("ZIP", "RAR"):
                    current_container = REGISTERED_EXTENSIONS["ARCH"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
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


def clean(folder):

    scan(folder)

    for file in IMAGE:
        handle_image(file, folder, "images")

    for file in VIDEO:
        handle_video(file, folder, "video")

    for file in AUDIO:
        handle_audio(file, folder, "audio")

    for file in DOC:
        handle_doc(file, folder, "documents")

    for file in OTHER:
        handle_other(file, folder, "other")

    for file in ARCH:
        handle_archive(file, folder, "archives")

    for item in FOLDERS:
        handle_folder(item)


def main():
    input_folder_path = input("enter path of folder for cleaning: ")

    sort_folder = Path(input_folder_path)
    print(sort_folder.resolve())
    clean(sort_folder.resolve())


if __name__ == "__main__":
    main()

