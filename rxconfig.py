import reflex as rx

config = rx.Config(
    app_name="cyber_industrial",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)