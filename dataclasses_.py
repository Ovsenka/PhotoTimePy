from typing import NamedTuple

class ServerData(NamedTuple):
    server: int
    hash: str
    photo: str

class AccountData(NamedTuple):
    id: str
    name: str
    lastname: str

class CurrentTime(NamedTuple):
    hour: str
    minute: str
    second: str
    