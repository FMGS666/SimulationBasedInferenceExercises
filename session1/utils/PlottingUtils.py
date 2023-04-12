from __future__ import annotations
import matplotlib.pyplot as plt

def plot_simulation(
        observations: list[float],
        latent_variables: list[float],
        title: str = "Simulation of State Space Model",
        observations_label: str =  "Observations (Y)",
        latent_label: str = "Latent Variable (X)",
        fig_size: tuple[int] | None = (15, 10),
    ) -> None:
    fig, ax = plt.subplots(figsize = fig_size)
    ax.plot(observations, label = observations_label)
    ax.plot(latent_variables, label = latent_label)
    ax.set_title(title)
    ax.set_xlabel('Time')
    ax.set_ylabel('')
    ax.legend()
    plt.show()