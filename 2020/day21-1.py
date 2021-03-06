from collections import defaultdict


with open("day21.txt", "r") as f:
    data = f.read().splitlines()

all_ingredients = set()
all_allergens = set()
recipes = {}
recipes_with_allergens = defaultdict(list)

for i, food in enumerate(data):
    ingredients = food.split("(")[0].strip().split(" ")
    allergens = food.split("(contains")[-1][:-1].strip().split(", ")
    for allergen in allergens:
        recipes_with_allergens[allergen].append(i)
    recipes[i] = ingredients

    all_ingredients.update(ingredients)
    all_allergens.update(allergens)

possible_allergens = {ingredient: set(all_allergens) for ingredient in all_ingredients}

clean_ingredients = []
for ingredient in possible_allergens:
    allergens = possible_allergens[ingredient]
    impossible_allergens = set()
    for allergen in allergens:
        recipes_with_allergen = recipes_with_allergens[allergen]
        if (
            len(
                [
                    recipe
                    for recipe in recipes_with_allergen
                    if ingredient not in recipes[recipe]
                ]
            )
            > 0
        ):
            impossible_allergens.add(allergen)
    allergens -= impossible_allergens
    if not allergens:
        clean_ingredients.append(ingredient)

total = 0
for ingredient in clean_ingredients:
    for _, ingredients in recipes.items():
        if ingredient in ingredients:
            total += 1

print(total)
