import reflex as rx
from reflex import Var
from typing import Optional

class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[
        str
    ] = "https://prod.spline.design/wBkT88TLmC5CIpSD/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline = Spline.create


