import reflex as rx 
from reflex import Var
from typing import Optional
from .spline import Spline

spline=Spline.create
def wave_spline() -> rx.Component:
    return rx.center(
        spline(),
        overflow="hidden",
        width="100%",
        height="100%",
        z_index="-1",
        position="absolute",
        sticky="True",
    )



