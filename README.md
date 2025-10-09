# PyBattMo

**PyBattMo** is a Python wrapper around the Julia-based [BattMo.jl](https://github.com/BattMoTeam/BattMo.jl).

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
