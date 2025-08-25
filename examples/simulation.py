# Partial port of https://battmoteam.github.io/BattMo.jl/dev/tutorials/2_run_a_simulation
import battmo as bm

cell_parameters = bm.load_cell_parameters(from_default_set = "Chen2020")
cycling_protocol = bm.load_cycling_protocol(from_default_set = "CCDischarge")
model_setup = bm.LithiumIonBattery()
output = bm.solve(sim)
