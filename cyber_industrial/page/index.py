import reflex as rx
from cyber_industrial.components.wavespline import wave_spline

def index() -> rx.Component:
    return rx.box(
        # Background wave
        rx.box(
            wave_spline(),
            style={
                "position": "absolute",
                "zIndex": 0,
                "top": 0,
                "left": 0,
                "width": "100vw",
                "height": "100vh",
                "overflow": "hidden",
            },
        ),
        # Foreground content
        rx.container(
            rx.heading(
                "IAMS",
                size="6",
                color="gray",
                align="center",
            ),
            rx.text(
                "Next Generation Asset "
            ),
            style={
                "position": "relative",
                "zIndex": 1,
                "width": "fit-content",
                "align": "center",
            },            
            ),

        ),
