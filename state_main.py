import logging
import sys
from time import sleep

from transitions import Machine


class BaseGundam:
    states = ["docked", "airframe", "fighter", "transforming"]
    transitions = [
        ["takeoff", "docked", "airframe"],
        ["dock", "airframe", "docked"],
        {"trigger": "transform", "source": "fighter", "dest": "transforming", "after": "transform_airframe"},
        {"trigger": "transform", "source": "airframe", "dest": "transforming", "after": "transform_fighter"},
        ["go_airframe", "transforming", "airframe"],
        ["go_fighter", "transforming", "fighter"],
    ]

    def __init__(self, name: str = None) -> None:
        self.machine = Machine(
            model=self,
            states=BaseGundam.states,
            transitions=BaseGundam.transitions,
            initial="docked",
        )
        self._name = name

    @property
    def name(self):
        return self._name

    def transform_airframe(self):
        # if testing, skip
        if "unittest" in sys.modules.keys():
            pass  # skip transformation delay
        else:
            sleep(100)

        self.go_airframe()

        logging.info(f"{self.name} is now in 'airframe' mode.")

    def transform_fighter(self):
        # if testing, skip
        if "unittest" in sys.modules.keys():
            pass  # skip transformation delay
        else:
            sleep(100)

        self.go_fighter()

        logging.info(f"{self.name} is now in 'fighter' mode.")

    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()
