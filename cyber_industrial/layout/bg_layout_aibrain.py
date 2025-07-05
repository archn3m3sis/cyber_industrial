import reflex as rx
from cyber_industrial.components.ai_brain_comp import splinecall

def BackgroundLayout(*children) -> rx.Component:
    return rx.box(
        # Background wave (fixed, behind everything)
        rx.box(
            splinecall(),
            style={
                "position": "fixed",
                "zIndex": 0,
                "top": 0,
                "left": 0,
                "width": "100vw",
                "height": "100vh",
                "overflow": "hidden",
            },
        ),
        # Foreground content (children)
        rx.box(
            *children,
            style={
                "position": "relative",
                "zIndex": 1,
                "width": "100vw",
                "minHeight": "100vh",
            },
        ),
        style={"width": "100vw", "minHeight": "100vh", "position": "relative"},
    )