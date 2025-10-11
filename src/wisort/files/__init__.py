from pathlib import Path
from wisort.config import Config, Library
import questionary


def move(map: dict[Path, Library], target: Path, cfg: Config):
    for src, lib in map.items():
        dest = Path(lib.destination).expanduser().absolute()

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

        dfile = dest / src.name
        if (
            lib.flatten is not None and not lib.flatten
        ) or cfg.orders.move_str == "preserveFolders":
            new_parent = dest / src.relative_to(target).parent
            new_parent.mkdir(exist_ok=True, parents=True)

            dfile = new_parent / src.name

        if dfile.exists():
            # conflict resolution
            # TODO: replace home path by tilde
            if not cfg.args.force:
                overwrite = questionary.confirm(
                    f"{dfile.relative_to(dest)} already exists in {dest}"
                ).ask()

                if not overwrite:
                    continue

        src.move(dfile)
