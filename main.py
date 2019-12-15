import pygame

class Game:
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.FPS = 60
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.render()
            pygame.display.flip()
        pygame.quit()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def loop(self):
        self.clock.tick(self.FPS)

    def render(self):
        pass


class TheCageOfMage(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Сюда необходимо добавить информацию о поле

    def handle_event(self, event):
        super().handle_event(event)
        # Здесь будут события

    def loop(self):
        super().loop()
        # Здесь движение

    def render(self):
        self.screen.fill(pygame.Color('black'))
        # self.board.render(self.screen)
        # Поле, когда оно появится)))


game = TheCageOfMage(1366, 768)
game.execute()