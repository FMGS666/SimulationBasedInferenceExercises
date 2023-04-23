import numpy as np

class MCPiEstimator(object):
    def __init__(
            self,
            seed: int = 1024,
            sample_size: int = 1000,
            n_simulations: int = 1
        ) -> None:
        self.seed = seed
        self.sample_size = sample_size
        self.n_simulations = n_simulations
        np.random.seed(self.seed)
        self.n_within = 0
        self.pi_hat = np.zeros(
            (self.n_simulations, )
        )
        self.mean_squared_error = None
        self.target_sample_shape = (
            2, 
            self.sample_size 
        ) 

    def __sample_points(
            self
        ) -> np.ndarray:
        points = np.random.uniform(
            low = -1.0, 
            high = 1.0, 
            size = self.target_sample_shape
        )
        return points

    def __is_within_circle(
            self
        ) -> int:
        points = self.__sample_points()
        squared_points = np.square(points)
        summed_squares = np.sum(squared_points, axis = 0)
        self.n_within = np.sum(summed_squares <= 1.0)
    
    def __fit_one_simulation(
            self
        ) -> float:
        self.__is_within_circle()
        proportion_within = self.n_within / (self.sample_size)
        pi_hat = 4.0 * proportion_within
        return pi_hat

    
    def __fit(
            self
        ) -> None:
        squared_error = 0
        for idx in range(self.n_simulations):
            pi_hat = self.__fit_one_simulation()
            self.pi_hat[idx] = pi_hat

    def __compute_mean_squared_error(
            self,
        ) -> float:
        pi = np.pi
        self.mean_squared_error = np.mean((pi - self.pi_hat)** 2) 
    
    def fit(
            self
        ) -> None:
        self.__fit()
        self.__compute_mean_squared_error()

    def display_results(
            self
        ) -> None:        
        print(f"MCPiEstimator:\n\tsample_size: {self.sample_size}\n\tn_simulations: {self.n_simulations}\n")
        print(f"\tpi: {np.pi}\n\tpi_hat: {np.mean(self.pi_hat)}\n\tmean_squared_error {self.mean_squared_error}\n")


