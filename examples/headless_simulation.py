from battmo import *

simulation_input = load_full_simulation_input(from_default_set="chen_2020")

output = run_simulation(simulation_input)

plot_dashboard(output, plot_type="contour")
