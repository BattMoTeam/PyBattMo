
[![Logo](https://github.com/BattMoTeam/visual-identity/blob/1bc87b07605d77fb3faa788c82f06ec2735ed31f/logos/battmo_logo_side.png)](https://github.com/BattMoTeam/BattMo.jl)

---

<p align="center">
  <a href="https://battmoteam.github.io/BattMo.jl/dev/manuals/pybattmo/installation">
    <img src="https://img.shields.io/badge/docs-dev-blue.svg" alt="Documentation">
  </a>
  <a href="https://github.com/battmoteam/PyBattMo/actions/workflows/CI.yml?query=branch%3Amain">
    <img src="https://github.com/battmoteam/BattMo.jl/actions/workflows/CI.yml/badge.svg?branch=main" alt="Build Status">
  </a>
  <a href="https://doi.org/10.5281/zenodo.17310497">
    <img src="https://zenodo.org/badge/1044330784.svg" alt="DOI">
  </a>
</p>

# PyBattMo

**PyBattMo** is a Python wrapper around the Julia-based [BattMo.jl](https://github.com/BattMoTeam/BattMo.jl). The Battery Modelling Toolbox (**BattMo**) is a resource for continuum modelling of electrochemical devices in MATLAB. The initial development features a pseudo X-dimensional (PXD) framework for the Doyle-Fuller-Newman model of lithium-ion battery cells. This is currently a early release that implements a subset of features from the [MATLAB version of BattMo](https://github.com/BattMoTeam/BattMo).

## BattMo Family
BattMo can be used through several interfaces:

- [MATLAB](https://github.com/BattMoTeam/BattMo)
- [Julia](https://github.com/BattMoTeam/BattMo.jl)
- [Python](https://github.com/BattMoTeam/PyBattMo)
- [Web app](https://app.batterymodel.com/)

## Installation

In addition to Python, Julia needs to be installed. Visit the [Julia website](https://julialang.org/install/) for more information on how to install Julia. To install PyBattMo, use the following pip command:

```bash
pip install battmo
```

## Quick start

Run examples using our internal library, for example the cell parameters from [Chen et al.](https://doi.org/10.1149/1945-7111/ab9050)

### P2D example

Here are a few examples to get you started:

```python
from battmo import *
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize the model
model = LithiumIonBattery()

# Load cell parameters and cycling protocol
cell_parameters = load_cell_parameters(from_default_set = "Chen2020")
cycling_protocol = load_cycling_protocol(from_default_set = "CCDischarge")

# Set up the simulation
sim = Simulation(model, cell_parameters, cycling_protocol)

# Run the simulation
output = solve(sim)

# Have a quick look into what kind of cell we're dealing with
print_cell_info(cell_parameters)

# Setup model and simulation
model = LithiumIonBattery()
sim = Simulation(model, cell_parameters, cycling_protocol)
output = solve(sim)

# Have a look into which output quantities are available
print_output_overview(output)

# Plotting using Plotly
df = to_pandas(output.time_series)
fig = px.line(df, x="Time", y="Voltage", title="Voltage curve")
fig.show()

# Use BattMo internal plotting functions
install_plotting()
plot_dashboard(output, plot_type="contour")

```

### Run a 3D simulation

```python
from battmo import *

# Load parameter sets and settings
cell_parameters = load_cell_parameters(from_default_set="Chen2020")
cycling_protocol = load_cycling_protocol(from_default_set="CCDischarge")
model_settings = load_model_settings(from_default_set="P4D_cylindrical")

# Setup model and simulation
model = LithiumIonBattery(model_settings=model_settings)
sim = Simulation(model, cell_parameters, cycling_protocol, simulation_settings=simulation_settings)
output = solve(sim)

# Plot interative 3D results
plot_interactive_3d(output)
```

## Documentation

Some additional examples are be found in the [BattMo.jl documentation](https://battmoteam.github.io/BattMo.jl/dev/pybattmo/installation) as well as a comprehensive documentation on the API and architecture of BattMo.jl.

## Acknowledgements

BattMo has received funding from the European Union’s Horizon 2020 innovation program under grant agreement numbers:

- 875527 HYDRA
- 957189 BIG-MAP
- 101104013 BATMAX
- 101103997 DigiBatt
