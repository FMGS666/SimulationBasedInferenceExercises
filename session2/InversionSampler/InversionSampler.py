import numpy as np


class InverseExpSampler(object):
    def __init__(
            self,
            rate: float = 2.0, 
            seed: int = 1024,
            n_samples: int = 100000 
        ) -> None:
        self.seed = seed
        self.rate = rate 
        self.n_samples = n_samples
        np.random.seed(self.seed)
        self.samples = np.zeros(
            (self.n_samples, )
        )

    
    def __sample_points(
            self
        ) -> np.ndarray:
        points = np.random.uniform(
            low = 0.0, 
            high = 1.0, 
            size = self.n_samples
        )
        return points
    
    def sample(
            self
        ) -> None:
        uniform_points = 1 - self.__sample_points()
        self.samples = np.log(uniform_points)
        self.samples *= -(1 / self.rate)
    