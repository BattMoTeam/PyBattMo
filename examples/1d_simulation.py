# %%
from battmo import *
import plotly.express as px
import pandas as pd
import numpy as np
import asyncio

# %%
# Load parameter sets
cell_parameters = load_cell_parameters(from_default_set="chen_2020")
cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")

# %%
# Have a quick look into what kind of cell we're dealing with
quick_cell_check(cell_parameters)

# %%
# Setup model and simulation
model = LithiumIonBattery()
sim = Simulation(model, cell_parameters, cycling_protocol)
output = solve(sim)

# %%
# Have a look into which output quantities are available
print_info(output)

# %%
# Plot voltage curve
time_series = output.time_series

df = to_pandas(time_series)
fig = px.line(df, x="Time", y="Voltage", title="Voltage curve")
fig.show()


# %%
# Plot a dashboard
plot_dashboard(output, plot_type="contour")


# %%
