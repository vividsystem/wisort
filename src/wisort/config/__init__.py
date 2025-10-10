from pydantic import BaseModel, Field
from typing import Protocol, Literal
import json


class Library(BaseModel):
    destination: str
    filetypes: list[str]


class Orders(BaseModel):
    unzip: bool = Field(default=True)
    dedupe: bool = Field(default=False)

    # portal: symlinks
    # remove: removes
    # auto: symlinks if duplicate looks intentional: completely other name, etc.
    dedupe_strategy: Literal["portal", "remove", "auto"] = Field(default="portal")

    recursion_strategy: Literal["preserveFolders", "flatten"] = Field(default="flatten")
    honor_gitignore: bool = Field(default=True)
    ignore_dotfiles: bool = Field(default=True)


class Config(BaseModel):
    # spell = spell (dict[str])
    # spell = list of str -> e.g. list of filetypes
    # ...
    spells: dict[str, str | list[str] | bool | int]
    libraries: dict[str, Library] | list[Library]
    orders: Orders


def load(path: str = "./config.json") -> Config:
    with open(path, "r") as f:
        data = json.load(f)
    return Config(**data)


loaded = load()
