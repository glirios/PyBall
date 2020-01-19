from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.draft.home import Home
from pyball.models.draft.school import School
from pyball.models.person import Person
from pyball.models.generic_team import Team


@dataclass
class Prospect:
    bisPlayerId: int = None
    home: Union[Home, Dict[str, Any]] = field(default_factory=dict)
    scoutingReport: str = None
    school: Union[School, Dict[str, Any]] = field(default_factory=dict)
    blurb: str = None
    headshotLink: str = None
    person: Union[Person, Dict[str, Any]] = field(default_factory=dict)
    draftPlayerId: int = None
    pickRound: float = None
    pickNumber: float = None
    rank: float = None
    pickedTeamCode: str = None
    comments: str = None
    photoFlag: bool = None
    isDrafted: bool = None
    currentAge: int = None
    team: Union[Team, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.person = Person(**self.person)
        self.home = Home(**self.home)
        self.school = School(**self.school)
        self.team = Team(**self.team)
