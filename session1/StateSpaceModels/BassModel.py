import numpy as np

class BassModel(object):

    def __init__(
            self,
            deterministic: bool = False,  
            alpha: np.float32 = 5e-1,
            beta: np.float32 = 1e-4,
            gamma: np.float32 = 5e-1,
            N: int = 100,
            X_0: int = 0, 
            time_horizon: int = 20, 
            seed: int = 0,
        ) -> None:
        self.deterministic = deterministic
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.N = N
        self.X_0 = X_0
        self.time_horizon = time_horizon
        self.seed = seed
        np.random.seed(self.seed)
        self.latent_variables_history = []
        self.observation_history = []
    
    def __generate_initial_latent_variable(
            self
        ) -> None:
        self.latent_variables_history.append(self.X_0)

    def __generate_deterministic_latent_transition(
            self
        ) -> None:
        X_t = self.latent_variables_history[-1]
        update_term = (self.N - X_t) * (self.alpha + self.beta * (X_t / self.N))
        X_t1 = X_t + update_term
        self.latent_variables_history.append(X_t1)
    
    def __generate_stochastic_latent_transition(
            self
        ) -> None:
        X_t = self.latent_variables_history[-1]
        n_binomial = self.N - X_t
        p_binomial = self.alpha + self.beta * (X_t / self.N)
        update_term = np.random.binomial(n = n_binomial, p = p_binomial)
        X_t1 = X_t + update_term
        self.latent_variables_history.append(X_t1)
    
    def __generate_latent_transition(
            self
        ) -> None:
        if self.deterministic:
            self.__generate_deterministic_latent_transition()
        else:
            self.__generate_stochastic_latent_transition()
        
    def __generate_observation(
            self
        ) -> None:
        X_t = self.latent_variables_history[-1]
        Y_t = np.random.binomial(n = X_t, p = self.gamma)
        self.observation_history.append(Y_t)
    
    def run_simulation(
            self
        ) -> None:
        self.__generate_initial_latent_variable()
        self.__generate_observation()
        for time_step in range(self.time_horizon):
            self.__generate_latent_transition()
            self.__generate_observation()