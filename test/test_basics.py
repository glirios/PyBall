import pytest
from pyball import PyBall
from pyball.models import Person

from pyball.exceptions import InvalidIdError, BadRequestError

@pytest.fixture(scope='module')
def test_intro_code():
	pb = pyball.PyBall()
	kluber = pb.get_player(446372)
	print(kluber.fullName)
	print(kluber.pitchHand.description)
	print(kluber.batSide.description)