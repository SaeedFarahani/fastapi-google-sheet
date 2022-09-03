import dataclasses

import pandas


@dataclasses.dataclass
class Contract:
    firstname: str
    lastname: str
    street: str
    zip: int
    city: str
    image: str

