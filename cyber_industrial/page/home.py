import reflex as rx
from cyber_industrial.components.particle_component import particles

def home() -> rx.Component:
    # Welcome Page (Index)
    return particles(
        rx.color_mode.button(position="top-right", z_index=1),
    )

