class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    def __repr__(self):
        return f"Model: {self.model} and color {self.color}"


# create an instance of Tesla

tesla_car = Tesla(model="s", color="black")
