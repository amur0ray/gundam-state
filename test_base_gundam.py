from unittest import TestCase

from transitions import MachineError

from state_main import BaseGundam


class TestBaseGundam(TestCase):
    def setUp(self):
        self.test_gundam = BaseGundam()

    def test_transition_from_docked(self):
        # normal transition
        self.test_gundam.takeoff()
        self.assertTrue(self.test_gundam.machine.is_state("airframe", self.test_gundam))

        # failed transition
        with self.assertRaises(MachineError):
            self.test_gundam.takeoff()
        self.assertTrue(self.test_gundam.machine.is_state("airframe", self.test_gundam))

        # transition back
        self.test_gundam.dock()
        self.assertTrue(self.test_gundam.machine.is_state("docked", self.test_gundam))

    def test_transition_to_fighter(self):
        self.test_gundam.takeoff()
        self.test_gundam.transform()

        self.assertTrue(self.test_gundam.machine.is_state("fighter", self.test_gundam))

    def test_transition_to_airframe(self):
        self.test_gundam.takeoff()
        self.test_gundam.transform()
        self.test_gundam.transform()

        self.assertTrue(self.test_gundam.machine.is_state("airframe", self.test_gundam))
