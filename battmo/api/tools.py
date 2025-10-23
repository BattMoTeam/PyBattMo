from ..julia_import import jl


def print_submodels(*arg, **kwargs):
    return jl.print_submodels(*arg, **kwargs)


def print_default_input_sets(*arg, **kwargs):
    return jl.print_default_input_sets(*arg, **kwargs)


def print_info(*arg, **kwargs):
    return jl.print_info(*arg, **kwargs)


def generate_default_parameter_files(*arg, **kwargs):
    return jl.generate_default_parameter_files(*arg, **kwargs)


def write_to_json_file(*arg, **kwargs):
    return jl.write_to_json_file(*arg, **kwargs)


def quick_cell_check(*arg, **kwargs):
    return jl.quick_cell_check(*arg, **kwargs)


def plot_cell_curves(*arg, **kwargs):
    return jl.plot_cell_curves(*arg, **kwargs)
