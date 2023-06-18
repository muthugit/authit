from dataclasses import dataclass
from uuid import uuid4


@dataclass
class BaseEntity:
    ...

    def __post_init__(self):
        if self._id == "" or self._id is None:
            self._id = str(uuid4())