import sys
from pathlib import Path
from threading import Thread

IMAGE = []
VIDEO = []
DOC = []
AUDIO = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

threads = []

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
                thread_dir = Thread(target=scan, args=(item,))
                threads.append(thread_dir)
                thread_dir.start()
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
                else:
                    current_container = REGISTERED_EXTENSIONS["OTHER"]
                    EXTENSION.add(extension)
                    current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start scan the folder {scan_path}")

    search_folder = Path(scan_path)

    scan(search_folder)
