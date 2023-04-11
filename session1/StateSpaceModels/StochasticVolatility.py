import numpy as np

class StochasticVolatility(object):

    def __init__(
            self, 
            sigma: np.float32 = 1e-1,
            beta: np.float32 = 1, 
            alpha: np.float32 = 99e-2,
            time_horizon: int = 1000, 
            seed: int = 1024
        ) -> None:
        self.sigma = sigma
        self.beta = beta
        self.alpha = alpha
        self.seed = seed
        self.time_horizon = time_horizon
        self.latent_variables_history = []
        self.observation_history = []
        np.random.seed(self.seed)
    
    def __generate_initial_latent_variable(
            self
        ) -> None:
        initial_latent_var = self.sigma**2 / (1 - self.alpha**2)
        initial_latent_std = np.sqrt(initial_latent_var)
        X_0 = np.random.normal(loc = 0, scale = initial_latent_std, size = 1)
        self.latent_variables_history.append(X_0[0])

    def __generate_observation(
            self
        ) -> None:
        X_t = self.latent_variables_history[-1]
        observation_variance = self.beta**2 * np.exp(X_t)
        observation_std = np.sqrt(observation_variance)
        Y_t = np.random.normal(loc = 0, scale = observation_std, size = 1)
        self.observation_history.append(Y_t[0])

    def __generate_latent_transition(
            self
        ) -> None:
        X_t = self.latent_variables_history[-1]
        latent_variable_mean = self.alpha * X_t
        X_t1 = np.random.normal(loc = latent_variable_mean, scale = self.sigma, size = 1)
        self.latent_variables_history.append(X_t1[0])
    
    def run_simulation(
            self
        ) -> None:
        self.__generate_initial_latent_variable()
        self.__generate_observation()
        for time_step in range(self.time_horizon):
            self.__generate_latent_transition()
            self.__generate_observation()