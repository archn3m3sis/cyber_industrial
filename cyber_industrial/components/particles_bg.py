# components/particles_bg.py
import reflex as rx

# Use NoSSRComponent because particles relies on browser APIs
class ParticlesBg(rx.NoSSRComponent):
    library = "react-tsparticles"
    tag = "Particles"
    lib_dependencies = ["tsparticles"]  # ensure lib is bundled
    is_default = False  # export is named

# If you want theme or config changes, override __init__
    def __init__(self, options: rx.Var | dict, **props):
        super().__init__(options=options, **props)

