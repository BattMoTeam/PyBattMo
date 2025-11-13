import pytest
import os, sys
import numpy as np

from battmo import *

# Import chayambuka input functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from examples.input.chayambuka_functions import *


def test_loading():

    cell_parameters = load_cell_parameters(from_default_set="chen_2020")
    cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")
    model_settings = load_model_settings(from_default_set="p2d")
    simulation_settings = load_simulation_settings(from_default_set="p2d")
    solver_settings = load_solver_settings(from_default_set="direct")
    full = load_full_simulation_input(from_default_set="chen_2020")


def test_simulation():
    cell_parameters = load_cell_parameters(from_default_set="chen_2020")
    cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")

    print_info(cell_parameters, view="NegativeElectrode")
    print_info(cell_parameters, view="Electrode")

    model_setup = LithiumIonBattery()
    sim = Simulation(model_setup, cell_parameters, cycling_protocol)
    output = solve(sim)

    cell_parameters = load_cell_parameters(from_default_set="chayambuka_2022")
    model_settings = load_model_settings(from_default_set="p2d")
    model_settings["ButlerVolmer"] = "Chayambuka"

    model_setup = SodiumIonBattery(model_settings=model_settings)
    sim = Simulation(model_setup, cell_parameters, cycling_protocol)
    output = solve(sim)


def test_output_handling():
    cell_parameters = load_cell_parameters(from_default_set="chen_2020")
    cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")
    model_setup = LithiumIonBattery()
    sim = Simulation(model_setup, cell_parameters, cycling_protocol)
    output = solve(sim)

    ts = output.time_series
    states = output.states
    metrics = output.metrics
    print_info(output)


# def test_plotting():

#     install_plotting()
#     activate_plotting()
#     make_interactive()

#     uninstall_plotting()


def test_utils():
    print_submodels()
    print_default_input_sets()
    print_info("Electrode")
    print_info("Grid")
    print_info("Concentration", view="OutputVariable")

    cell_parameters = load_cell_parameters(from_default_set="chen_2020")
    quick_cell_check(cell_parameters)

    # plot_cell_curves(cell_parameters)


def test_calibration():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    df_05 = pd.read_csv(
        os.path.join(
            base_path, os.path.join("examples", "input", "data", "Xu_2015_voltageCurve_05C.csv")
        ),
        names=["Time", "Voltage"],
    )

    cell_parameters = load_cell_parameters(from_default_set="xu_2015")
    cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")

    cycling_protocol["LowerVoltageLimit"] = 2.25
    cycling_protocol["DRate"] = 0.5

    model = LithiumIonBattery()
    sim = Simulation(model, cell_parameters, cycling_protocol)
    output0 = solve(sim)

    time_series = output0.time_series
    df_sim = to_pandas(time_series)

    cal = VoltageCalibration(np.array(df_05["Time"]), np.array(df_05["Voltage"]), sim)

    print_info(cal)
    free_calibration_parameter(
        cal,
        ["NegativeElectrode", "ActiveMaterial", "StoichiometricCoefficientAtSOC100"],
        lower_bound=0.0,
        upper_bound=1.0,
    )
    free_calibration_parameter(
        cal,
        ["PositiveElectrode", "ActiveMaterial", "StoichiometricCoefficientAtSOC100"],
        lower_bound=0.0,
        upper_bound=1.0,
    )

    free_calibration_parameter(
        cal,
        ["NegativeElectrode", "ActiveMaterial", "StoichiometricCoefficientAtSOC0"],
        lower_bound=0.0,
        upper_bound=1.0,
    )
    free_calibration_parameter(
        cal,
        ["PositiveElectrode", "ActiveMaterial", "StoichiometricCoefficientAtSOC0"],
        lower_bound=0.0,
        upper_bound=1.0,
    )

    free_calibration_parameter(
        cal,
        ["NegativeElectrode", "ActiveMaterial", "MaximumConcentration"],
        lower_bound=10000.0,
        upper_bound=1e5,
    )
    free_calibration_parameter(
        cal,
        ["PositiveElectrode", "ActiveMaterial", "MaximumConcentration"],
        lower_bound=10000.0,
        upper_bound=1e5,
    )

    solve(cal)

    cell_parameters_calibrated = cal.calibrated_cell_parameters

    sim_calibrated = Simulation(model, cell_parameters_calibrated, cycling_protocol)
    output_calibrated = solve(sim_calibrated)

    time_series_cal = output_calibrated.time_series

    df_sim_cal = to_pandas(time_series_cal)


def test_user_defined_function():

    import os
    import sys

    # Get the directory of the current file
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the relative path you want to add
    relative_path = os.path.join(root_dir, 'examples')

    # Add it to the system path
    sys.path.append(relative_path)

    # Import chayambuka input functions
    import input.chayambuka_functions

    cell_parameters = load_cell_parameters(from_default_set="chayambuka_2022")
    cycling_protocol = load_cycling_protocol(from_default_set="cc_discharge")
    model_settings = load_model_settings(from_default_set="p2d")
    model_settings["ButlerVolmer"] = "Chayambuka"

    model_setup = SodiumIonBattery(model_settings=model_settings)
    sim = Simulation(model_setup, cell_parameters, cycling_protocol)
    output = solve(sim)
