# SimulationBasedInferenceExercises

Repository containing exercises for the SimulationBasedInference Course, DSBA 2023

The repository will contain a folder for each session. 

Here we give a brief description of the structure of each of folder

## Session 1

Contains the code necessary for solving the exercises presented during the first session of the course.
It is organized as follows:

### ```./session1/StateSpaceModels``` 

This directory contains the definition of the objects used for simulating the models seen in class.
For more details about them, check the course material.

In particular, we have the following files: 

#### ```./session1/StateSpaceModels/StochasticVolatility.py```

Contains the ```StochasticVolatility``` object for running the simulation of a stochastic volatility model

#### ```./session1/StateSpaceModels/BassModel.py```

Contains the object for running the simulation of a Bass model (i.e.: ```BassModel```). This object will allow to run simulations for both the stochastic and the deterministic  versions of the model, by specifying the ```BassModel.deterministic``` attribute. Intuitively, when such attribute is set to```True```, the simulation will be of a deterministic Bass model, while in case it is set to ```False```, the simulation will involve a stochastic Bass model.

### ```./session1/Notebook.ipynb```

Notebook where the simulations are run using the above defined objects and the results are plotted with ```matplotlib.pyplot```.


## Session 2

Contains the code necessary for solving the exercises presented during the first session of the course.
It is organized as follows:

### ```./session2/MCPiEstimator/MCPiEstimator.py```

This file contains the definition of the object used for running Monte Carlo Sampling for estimating the constant pi.

### ```./session2/InversionSampler/InversionSampler.py```


This file contains the definition of the object used for running the Inversion Sampling method over an Exponential Distribution.
For more details about the method, check the course material.

### ```./session2/Notebook.ipynb```

Notebook where the exercises are run and some results are plotted with ```matplotlib.pyplot```.

