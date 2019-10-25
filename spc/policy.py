from typing import Dict


class BasePolicy:
    def __call__(self, m: Dict):
        raise NotImplementedError("BasePolicy.__call__")


class RewardPolicy(BasePolicy):
    def __init__(self, reward_fun):
        self.reward_fun = reward_fun

    def __call__(self, m: Dict):
        import numpy as np
        r = self.reward_fun(m)
        return np.unravel_index(np.argmax(r), r.shape)