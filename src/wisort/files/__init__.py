from pathlib import Path
from wisort.config import Config


def move(map: dict[Path, str], cfg: Config):
    for src, dest_str in map.items():
        dest = Path(dest_str).expanduser().absolute()
        print(dest)

        if not dest.is_dir():
            raise Exception(
                f"Destination path {
                    dest.absolute()
                } is not a directory or does not exist"
            )

        # do some smart automations
        # dont move if in ignored
        # handle symlinks
        # unzip on move? -> smartly if zip has multiple elements zip to folder, otherwise zip to element directly

        # this doesnt support preserve file structure as of now
        src.move(dest / src.name)
