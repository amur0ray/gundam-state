from transitions import Machine

class BaseGundam:
    states = ['dock', 'airframe', 'fighter', 'transform']

    def __init__(self) -> None:
        self.machine = Machine(model=self,
                               states=BaseGundam.states,
                               initial='dock')
        
    def move(self):
        raise NotImplementedError()
    
    def attack(self):
        raise NotImplementedError()
    