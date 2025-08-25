# Partial port of https://battmoteam.github.io/BattMo.jl/dev/tutorials/2_run_a_simulation
from battmo import load_cell_parameters, load_cycling_protocol, LithiumIonBattery, Simulation, solve

cell_parameters = load_cell_parameters(from_default_set = "Chen2020")
cycling_protocol = load_cycling_protocol(from_default_set = "CCDischarge")
model_setup = LithiumIonBattery()
sim = Simulation(model_setup, cell_parameters, cycling_protocol)
output = solve(sim)
