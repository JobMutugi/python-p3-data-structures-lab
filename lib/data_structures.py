def get_names(spicy_foods):
    # return a list of all the names
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # return foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    # print each food formatted with 🌶 repeated heat_level times
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return the first food that matches the given cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    # filter foods heat_level > 5 and print them
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    # average of heat_level values
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    # return new list with extra spicy food added
    return spicy_foods + [spicy_food]
