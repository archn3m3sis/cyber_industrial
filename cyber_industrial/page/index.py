import reflex as rx
from cyber_industrial.layout.bg_layout_aibrain import BackgroundLayout

def index() -> rx.Component:
    return BackgroundLayout(
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
                "align_items": "center",
                "margin": "0 auto",
            },            
        ),
    )
