from dataclasses import dataclass


@dataclass(frozen=True)
class HeaderResult:
    name: str
    status: str
    message: str