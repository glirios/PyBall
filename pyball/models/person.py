from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: int = None
    fullName: str = None
    link: str = None
    firstName: str = None
    lastName: str = None
    primaryNumber: str = None
    birthDate: str = None
    currentAge: int = None
    birthCity: str = None
    birthStateProvince: str = None
    birthCountry: str = None
    height: str = None
    weight: int = None
    active: bool = None
    primaryPosition: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    useName: str = None
    middleName: str = None
    boxscoreName: str = None
    nickName: str = None
    gender: str = None
    isPlayer: bool = None
    isVerified: bool = None
    draftYear: int = None
    pronunciation: str = None
    mlbDebutDate: str = None
    batSide: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    pitchHand: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    nameFirstLast: str = None
    nameSlug: str = None
    firstLastName: str = None
    lastFirstName: str = None
    lastInitName: str = None
    initLastName: str = None
    fullFMLName: str = None
    fullLFMName: str = None
    strikeZoneTop: float = None
    strikeZoneBottom: float = None
    nameTitle: str = None
    nameMatrilineal: str = None
    deathDate: str = None
    deathCity: str = None
    deathCountry: str = None


    def __post_init__(self):
        self.pitchHand = PitchHand(**self.pitchHand)
        self.primaryPosition = PrimaryPosition(**self.primaryPosition)
        self.batSide = BatSide(**self.batSide)
