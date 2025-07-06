import reflex as rx
from cyber_industrial.layout.bg_layout_aibrain import BackgroundLayout
from reflex_type_animation import type_animation

def index() -> rx.Component:
    return BackgroundLayout(
        rx.container(
            rx.heading(
                "IAMS",
                size="6",
                color="gray",
                align="center",
            ),
            type_animation(
                sequence=[
                    "The quick brown fox jumped over the lazy Dog",
                    800
                ]
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


