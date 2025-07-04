import reflex as rx

config = rx.Config(
    app_name="cyber_industrial",
    db_url="sqlite:///cyber_industrial/database/data/cyber_industrial.db",
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
)
