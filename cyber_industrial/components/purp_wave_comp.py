import reflex as rx 
from reflex import Var
from typing import Optional
from .purp_wave_spline import Spline

spline=Spline.create

def splinecall() -> rx.Component:
    return rx.center(
        spline(),
        overflow="hidden",
        width="100%",
        height="100%",
        z_index="-1",
        position="absolute",
        sticky="True",
    )



