from dataclasses import dataclass


@dataclass
class Permission:
    permissionName: str
    permissionDescription: str