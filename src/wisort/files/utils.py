from pathlib import Path


def creation_time(p: Path):
    return p.stat().st_birthtime
