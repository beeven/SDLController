import sys,os
import init

try:
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

from sdl2.ext import Resources
RESOURCES = Resources(__file__, "resources")

sdl2ext.init()

window = sdl2ext.Window("Hello World!", size=(640,480))
window.show()

factory = sdl2ext.SpriteFactory(sdl2ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("totoro.png"))

spriterenderer = factory.create_sprite_renderer(window)
spriterenderer.render(sprite)

processor = sdl2ext.TestEventProcessor()
processor.run(window)

sdl2ext.quit()
