import time
import tkinter as tk
root = tk.Tk()
root.geometry("900x600")
root.title("Lemegame")
from class_recipe import *
from class_resources import *
from class_building import *

def create_menu():
    menu_choice = tk.IntVar()
    menu = [
        ("Buildings", 1),
        ("Research", 2),
        ("Resources", 3),
        ("No_Clue", 4),
        ("No_Clue_#2", 5)
    ]

    def ShowChoice():
        print(menu_choice.get())
            
    def Commands():
        ShowChoice()

    menu_title = tk.StringVar()
    menu_title.set("Menu")
    length = len(menu_title.get())*2

    menu_frame = tk.Frame(root)
    menu_frame.pack(side=tk.LEFT)  

    menu_label = tk.Label(menu_frame,
            text= menu_title.get(),
            justify = tk.LEFT,
            padx = 20).pack()

    for val, language in enumerate(menu):
        tk.Radiobutton(menu_frame,
                    text=language,
                    indicatoron = 0,
                    width = 40,
                    padx = length,
                    variable=menu_choice,
                    command=Commands,
                    value=val + 1).pack(anchor=tk.W)

def create_resource_button(resource, resource_box):
    if not resource.button:
        button_container, checkbox_container, label_container = resource_box
        resource.color_var.set("dark green")
        resource.tk_button = tk.Button(button_container,
                    text=f"Gather {resource.name}",
                    padx = 50,
                    command=lambda:resource.set()).pack()
        resource.button = True

def create_building_button(building, parent):
    if not building.button:
        button_container, checkbox_container, label_container = parent
        building.tk_button = tk.Button(button_container,
                    text=f"Build {building.name}",
                    padx = 50,
                    command=lambda:building.build(checkbox_container))
        building.tk_button.pack()
        resource = building.resource
        resource.label = tk.Label(label_container, text=f"{resource.name}: {resource.get()}", fg="dark green")
        resource.label.pack()
        # building.check_box = tk.Checkbutton(checkbox_container, text="automate", variable=building.automated).pack()
        building.button = True

def resource_display_updater(updater, resources, resource_box):
    def tracker():
        for recipe in Recipe.ALL_RECIPES:
            if not recipe.unlocked:
                unlocked = recipe.check_requirements()
                if unlocked:
                    create_building_button(recipe.unlocked_resource, resource_box)
                else:
                    break
        for resource in resources:
            if resource.label is not None: 
                drain = resource.calculate_drain()
                resource.label.config(text=f"{resource.name}: {resource.get()} ({drain}/tick)")
            if resource.automated.get():
                ### this part -> fix drain when less than 0
                resource.set()

        updater.after(100, tracker)
    tracker()

def create_resource_panel(parent, side):
    resource_frame = tk.Frame(parent)
    left = tk.Frame(resource_frame, borderwidth=2, relief="solid")
    right = tk.Frame(resource_frame, borderwidth=2, relief="solid")
    gather_button_container = tk.Frame(right, borderwidth=2, relief="solid")
    gather_automate_container = tk.Frame(right, borderwidth=2, relief="solid")
    container = tk.Frame(right, borderwidth=2, relief="solid")

    container_label = tk.Label(container, text="Maybe i should be research stuff\nOr perhaps feedback window/log").pack()

    resource_box = [gather_button_container, gather_automate_container, left]
    resource_display_updater(left, Resources.ALL_RESOURCES, resource_box)

    left.pack(side=tk.LEFT, expand=True, fill="both")
    right.pack(side=tk.RIGHT, expand=True, fill="both", padx=10)
    container.pack(side=tk.BOTTOM, expand=True, fill="both", padx=5, pady=5)
    gather_button_container.pack(side=tk.LEFT, expand=True, fill="both", padx=5, pady=5)
    gather_automate_container.pack(side=tk.RIGHT, expand=True, fill="both", padx=5, pady=5)

    resource_frame.pack(side=side, expand=True, fill="both", padx=10, pady=10)
    return resource_box

def create_research_panel():   
    research_frame = tk.Frame(root,
        cursor="heart")

    research_label = tk.Label(research_frame,
            text= "Research",
            padx = 20)

    research_frame.pack(side=tk.RIGHT)
    research_label.pack()

def __main__():
    create_menu()
    container = tk.Frame(root, borderwidth=2, relief="solid")
    resource_box = create_resource_panel(container, tk.RIGHT)
    # construction_box = create_resource_panel(container, tk.LEFT)
    create_resource_button(Food, resource_box)
    create_building_button(Gatherers_Hut, resource_box)
    container.pack(side=tk.BOTTOM, expand=True, fill="both", padx=5, pady=5)
    Wood.amount.set(100)
    Food.amount.set(100)
    # Food.increase_other_bonus("Random bonus", 2)
    # Food.increase_multiplier_bonus("New_multiplier", 10)
    # Food.increase_multiplier_bonus("Another_multiplier", 5)

    print(Food.increase_amount_building)
    root.mainloop()

 

if __name__ == "__main__":
    __main__()

