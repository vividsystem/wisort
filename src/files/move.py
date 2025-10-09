from config import Library


def lib_map(libraries: dict[str, Library]) -> dict[str, str]:
    result: dict[str, str] = {}
    for lib in libraries.values():
        for ft in lib.filetypes:
            result[ft] = lib.destination

    return result
