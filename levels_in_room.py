import pygame

from level_mask import LevelMask


class NewLevel(LevelMask):
    def __init__(self, width, height):
        super().__init__(width, height)
        print('я утка')
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            self.all_sprites.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            self.mage_group.draw(self.screen)

            self.mage_group.update(event, 10, self.bottom_border, self.borders)

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)