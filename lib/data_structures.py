spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy_food["name"] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[spiciest_food for spiciest_food in spicy_foods if spiciest_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        x = "🌶" * food['heat_level']
        print(f"{food['name']} ({(food['cuisine'])}) | Heat level : {x}")
print_spicy_foods(spicy_foods)
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return[spicy_food for spicy_food in spicy_foods if spicy_food["cuisine"] == cuisine]
    # for spicy_food in spicy_foods:
    #     if spicy_food["cuisine"] == cuisine:
    #         return [spicy_food]
def print_spiciest_foods(spicy_foods):
    newFood = get_spiciest_foods(spicy_foods)
    print_spicy_foods(newFood)
    

def get_average_heat_level(spicy_foods):
    sum = 0
    for spicy_food in spicy_foods:
        sum += spicy_food["heat_level"]
    return int(sum / len(spicy_foods))
   
  

def create_spicy_food(spicy_foods, spicy_food):
    pass
