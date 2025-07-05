import reflex as rx
from components.particles_bg import ParticlesBg

# Example reactive config
particle_opts = rx.Var(
    {
        "particles": {
            "number": {"value": 80, "density": {"enable": True, "value_area": 800}},
            "color": {"value": "#0ff"},
            "move": {"enable": True, "speed": 1},
        }
    }
)

#@rx.page()

def particles() -> rx.Component:
    return rx.box(
        ParticlesBg(options=particle_opts, style={"position": "absolute", "zIndex": -2}),
        rx.box("Cyber Industrial", style={"position": "relative", "zIndex": -1, "color": "white"}),
        style={"position": "relative", "width": "100vw", "height": "100vh", "overflow": "hidden"},
    )