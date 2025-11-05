import juliapkg
from ..julia_import import jl
import juliacall
import time
import asyncio


def activate_plotting():
    try:
        jl.seval("using GLMakie; GLMakie.activate!()")

    except:

        print("Unable to load GLMakie. Have you called install_plotting()?")

        return False
    return True


def install_plotting():
    juliapkg.add("GLMakie", "e9467ef8-e4e7-5192-8a1a-b1aee30e663a")
    juliapkg.resolve()
    activate_plotting()
    return True


def uninstall_plotting():
    juliapkg.rm("GLMakie", "e9467ef8-e4e7-5192-8a1a-b1aee30e663a")
    juliapkg.resolve()
    return True


def make_interactive():
    juliacall.interactive()


async def keep_plot_dashboard_alive(*arg, **kwargs):
    fig = jl.plot_dashboard(*arg, **kwargs)
    while True:
        jl.seval("yield()")
        await asyncio.sleep(0.1)


def plot_dashboard(*arg, **kwargs):

    if activate_plotting():

        loop = asyncio.get_event_loop()

        if loop.is_running():
            # Notebook or already running loop
            loop.create_task(keep_plot_dashboard_alive(*arg, **kwargs))
        else:
            # Script or no loop running - start a loop
            asyncio.run(keep_plot_dashboard_alive(*arg, **kwargs))


async def keep_plot_output_alive(*arg, **kwargs):
    fig = jl.plot_output(*arg, **kwargs)
    while True:
        jl.seval("yield()")
        await asyncio.sleep(0.1)


def plot_output(*arg, **kwargs):
    if activate_plotting():
        try:
            loop = asyncio.get_event_loop()
            # Notebook or already running loop
            loop.create_task(keep_plot_output_alive(*arg, **kwargs))

        except RuntimeError:
            # Script: no loop running, so start one
            asyncio.run(keep_plot_output_alive(*arg, **kwargs))


async def keep_plot_interactive_3d_alive(*arg, **kwargs):
    fig = jl.plot_interactive_3d(*arg, **kwargs)
    while True:
        jl.seval("yield()")
        await asyncio.sleep(0.1)


def plot_interactive_3d(*arg, **kwargs):
    if activate_plotting():
        try:
            loop = asyncio.get_event_loop()
            # Notebook or already running loop
            loop.create_task(keep_plot_interactive_3d_alive(*arg, **kwargs))

        except RuntimeError:

            # Script: no loop running, so start one
            asyncio.run(keep_plot_interactive_3d_alive(*arg, **kwargs))
