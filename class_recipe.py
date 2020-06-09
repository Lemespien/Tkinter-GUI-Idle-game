from class_resources import *
from class_building import *
class Recipe():
    ALL_RECIPES = []
    def __init__(self, unlocked_resource, required_resources):
        self.unlocked_resource = unlocked_resource
        self.name = unlocked_resource.name
        self.required_resources = required_resources
        self.unlocked = False
        Recipe.ALL_RECIPES.append(self)

    def check_requirements(self):
        if not self.unlocked:
            count = 0
            for resource in self.required_resources:
                if self.required_resources[resource] <= resource.get():
                    count += 1
                    if resource.label is not None:
                        resource.label.config(fg="dark green")
                    print(f"I've got enough {resource.name} ({resource.get()}/{self.required_resources[resource]})")
                else:
                    # resource.color_var.set("red")
                    if resource.label is not None:
                        resource.label.config(fg="red")
                    # resource.label.config(bg="black").pack()
                    print(f"Not enough {resource.name} ({resource.get()}/ {self.required_resources[resource]})")
            if count >= len(self.required_resources):
                print(f"UNLOCKED {self.name}")
                self.unlocked = True
                return True



wood_unlock = Recipe(Lumberjack_Hut, {Food:10})
stone_unlock = Recipe(Stonemason, {Food:10, Wood: 20})
water_unlock = Recipe(Water_Well, {Food: 100, Wood: 20, Stone: 50})
wheat_unlock = Recipe(Farm, {Food: 10, Wood: 50, Stone: 25, Water: 20})
bread_unlock = Recipe(Bakery, {Food: 5, Wood: 5, Water: 10, Wheat:15})