class Father():
    eye_color = "brown"
    hair = "curly"
    height = "average"
    voice = "deep"
    favorite_sport = "tennis"
    def laugh(self):
        return "LOL"
    def hobby(self):
        return "I work with wood in my free time"
    def walk(self):
        return "Walking with long and quick steps"

class Child(Father):

    def hobby(self):
        return "I play video games in my free time"
