import tkinter as tk


class Resources:
    ALL_RESOURCES = {}

    def __init__(self, name, amount=0, dependent=None, increase_amount_base=0):
        self.name = name
        self.amount = tk.IntVar()
        self.unlocked = False
        self.amount.set(amount)
        self.dependent = dependent
        self.button = False
        self.automated = tk.BooleanVar()
        self.increase_amount_base = 1
        self.increase_amount_building = {"Base": 0}
        self.increase_amount_other = {"Base": 0}
        self.multiplier_bonus = {"Base": 1}
        self.incrase_amount = 1
        self.label = None
        self.check_box = None
        self.color_var = tk.StringVar()
        self.apply_all_increases()
        self.drains = {}
        Resources.ALL_RESOURCES[self] = self

    def get(self):
        return self.amount.get()

    def set(self, amount=0):
        dependent = self.dependent
        if amount >= 0:
            amount = self.increase_amount + amount
        if dependent == None or amount < 0:
            self.amount.set(self.get() + amount)
            return
        need_count = 0
        building_count = 0
        for building in self.increase_amount_building:
            building_count += self.increase_amount_building[building]
        for resource in dependent:
            need_amount = self.dependent[resource]
            if resource.get() >= need_amount * building_count:
                need_count += 1
            else:
                if not self.automated:
                    print(f"Not enough {resource.name}: {resource.get()}/{need_amount * building_count}")
        if need_count >= len(dependent):
            for resource in dependent:
                need_amount = dependent[resource]
                resource.set(-need_amount * building_count)
            self.amount.set(self.get() + amount)

        # if dependent.get() >= need_amount:
        #     self.amount.set(self.get() + amount)
        #     dependent.set(-need_amount)

    def increase_building_bonus(self, building, value):
        self.increase_amount_building[building] = value
        self.apply_all_increases()

    def increase_other_bonus(self, bonus, value):
        self.increase_amount_other[bonus] = value
        self.apply_all_increases()

    def increase_multiplier_bonus(self, bonus, value):
        self.multiplier_bonus[bonus] = value
        self.apply_all_increases()

    def apply_all_increases(self):
        total_multiplier = 1
        total_bonus = 0
        bonuses = [self.increase_amount_building, self.increase_amount_other]
        for multiplier in self.multiplier_bonus:
            total_multiplier *= self.multiplier_bonus[multiplier]
        for bonus in bonuses:
            for value in bonus:
                total_bonus += bonus[value]
        self.increase_amount = (self.increase_amount_base + total_bonus) * total_multiplier

    def calculate_drain(self):
        total_drain = 0
        for res in self.drains:
            total_drain += self.drains[res]
        return self.increase_amount - total_drain
    # def create_resource_button(self):
    #     if not self.button:
    #         self.tk_button = tk.Button(gather_button_container,
    #                     text=f"Gather {self.name}",
    #                     padx = 50,
    #                     command=lambda:self.set()).pack()
    #         self.check_box = tk.Checkbutton(gather_automate_container, text="automate", variable=self.automated).pack()
    #         self.label = tk.Label(left, text=f"{self.name}: {self.get()}", fg="dark green")
    #         # self.label_updater(self.label)
    #         self.label.pack()
    #         self.button = True

    # def label_updater(self, label):
    #     def tracker():
    #         if self.automated.get():
    #             self.set()
    #         label.after(100, tracker)
    #     tracker()


Food = Resources("Food",
                 increase_amount_base=1)

Wood = Resources("Wood",
                 dependent={
                     Food: 10
                 })

Stone = Resources("Stone",
                  dependent={
                      Food: 5
                  })

Water = Resources("Water")

Wheat = Resources("Wheat",
                  dependent={
                      Food: 50,
                      Water: 10
                  })

Bread = Resources("Bread",
                  dependent={
                      Food: 5,
                      Wood: 5,
                      Water: 10,
                      Wheat: 15
                  })
