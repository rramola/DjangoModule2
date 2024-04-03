from dataclasses import dataclass
from typing import List


@dataclass
class Team:
    name: str
    members: list[str]
    details: str


Teams = [
    Team(
        "Documentation",
        ["member_one", "member_two", "member_three"],
        "These are the details",
    ),
    Team(
        "Management",
        ["member_one", "member_two", "member_three"],
        "These are the details",
    ),
    Team(
        "Procurement",
        ["member_one", "member_two", "member_three"],
        "These are the details",
    ),
]
