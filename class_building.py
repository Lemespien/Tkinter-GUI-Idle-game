from class_resources import *


def toggle_automated(resource, value):
    if resource.dependent is not None:
        if resource.automated.get():
            for res in resource.dependent:                
                res.drains[resource] = resource.dependent[res] * value
                print("Set dependency drains")
                print(res.drains[resource])
        else:
            for res in resource.dependent:                
                res.drains[resource] = 0
                print("Removed dependency drains")
                print(res.drains[resource])
            
class Building():
    def __init__(self, name, resource, cost, value=1):
        self.name = name
        self.resource = resource
        self.count = 0
        self.cost = cost
        self.value = value
        self.button = False

    def build(self, checkbox_container):
        count = 0
        for resource in self.cost:
            if resource.get() >= self.cost[resource]:
                count += 1
        if count >= len(self.cost):
            for resource in self.cost:
                resource.set(-self.cost[resource])
                self.cost[resource] = round(self.cost[resource]**1.05)
            if self.count == 0:
                self.resource.check_box = tk.Checkbutton(checkbox_container, text=f"automate {self.resource.name}", variable=self.resource.automated, command=lambda:toggle_automated(self.resource, self.count)).pack()
                self.resource.automated.set(True)
            self.count += 1
            self.resource.increase_building_bonus(self.name, self.count * self.value)
            if self.resource.dependent is not None:
                for res in self.resource.dependent:
                    res.drains[self.resource] = self.resource.dependent[res] * self.count

Gatherers_Hut = Building("Gatherers Hut", Food, cost={Food: 10, Wood: 15})
Hunters_Cabin = Building("Hunters Cabin", Food, cost={Food: 10, Wood: 15}, value=5)
Lumberjack_Hut = Building("Lumberjack_Hut", Wood, 
    cost={
        Food:10
    })

Stonemason = Building("Stonemason", Stone, 
    cost={
        Food:10,
        Wood:15
    })

Water_Well = Building("Water Well", Water,
    cost={
        Food:5,
        Wood:20,
        Stone:50
    })

Farm = Building("Farm", Wheat, 
    cost={
        Food:10,
        Wood:15,
        Stone: 10
    })
Bakery = Building("Bakery", Bread, 
    cost={
        Food:15,
        Wood:25,
        Stone: 30
    })

