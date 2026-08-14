import json

class Games:
    def __init__(self, title, plataform, hours_played):
        self.title = title
        self.plataform = plataform
        self.hours_played = hours_played

    def to_dict(self):
        return {
            "title": self.title,
            "plataform": self.plataform,
            "hours_played": self.hours_played
        }

mi_juego = Games("Minecraft", "PC", 500)

print(mi_juego.title)
print(mi_juego.to_dict())