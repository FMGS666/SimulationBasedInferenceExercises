import numpy as  np

from scipy.optimize import minimize_scalar
from tqdm import tqdm

#proposal distribution
def sample_uniform() -> float:
    return np.random.uniform()

def compute_log_likelihood(
        theta: float,
        class_counts: list[int] = [125, 18, 20, 34] 
    ) -> float:
    y1, y2, y3, y4 = class_counts
    likelihood = y1 * np.log(2 + theta) + \
        (y2 + y3) * np.log(1 - theta) + \
            y4 * np.log(theta)
    return - likelihood

def maximize_likelihood() -> float:
    minimized_likelihood = minimize_scalar(compute_log_likelihood, bounds = [0, 1], method = "bounded")
    return - minimized_likelihood.fun

def accept_proposal(x
        theta: float,
        unif_sample: float,
        log_C: float
    ) -> bool:
    likelihood = - compute_log_likelihood(theta)
    log_U = np.log(unif_sample)
    #print(f"theta {theta} log_U {log_U} likelihood {likelihood} log_C {log_C}")
    return log_U <= likelihood - log_C

def rejection_sampling() -> float:
    theta = sample_uniform()
    unif_sample = sample_uniform()
    log_C = maximize_likelihood()
    while not accept_proposal(theta, unif_sample, log_C):
        theta = sample_uniform()
    return theta

def genetic_linkage_rejection_sampling(
        n_samples: int = 10000
    ) -> list[float]:
    samples = []
    for sample in tqdm(range(n_samples)): 
        theta = rejection_sampling()
        samples.append(theta)
    return samples