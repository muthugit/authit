from dataclasses import dataclass, field
from typing import List
from authr.entities.permission import Permission


@dataclass
class Role:
    roleName: str
    roleDescription: str = ""
    permissions: List[Permission] = field(default_factory=lambda: [])