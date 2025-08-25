from .julia_import import jl

def load_cell_parameter(*arg, **kwargs):
    return jl.load_cell_parameters(*arg, **kwargs)

def load_cycling_protocol(*arg, **kwargs):
    return jl.load_cycling_protocol(*arg, **kwargs)

def LithiumIonBattery(*arg, **kwargs):
    return jl.LithiumIonBattery(*arg, **kwargs)

def Simulation(*arg, **kwargs):
    return jl.Simulation(*arg, **kwargs)

def solve(*arg, **kwargs):
    return jl.solve(*arg, **kwargs)
