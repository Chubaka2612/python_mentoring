from enum import Enum
import random


class Sex(Enum):
    MALE = "male"
    FEMALE = "female"

    @classmethod
    def get_gender(cls):
        return random.choice([Sex.FEMALE, Sex.MALE])
