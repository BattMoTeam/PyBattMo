import pytest

from battmo import (
    load_cell_parameters,
    load_cycling_protocol,
    LithiumIonBattery,
    Simulation,
    solve,
    print_output_overview,
    plot_interactive_3d,
    make_interactive,
    install_plotting,
)


def test_api():

    cell_parameters = load_cell_parameters(from_default_set="Chen2020")
    cycling_protocol = load_cycling_protocol(from_default_set="CCDischarge")

    model_setup = LithiumIonBattery()
    sim = Simulation(model_setup, cell_parameters, cycling_protocol)
    output = solve(sim)
