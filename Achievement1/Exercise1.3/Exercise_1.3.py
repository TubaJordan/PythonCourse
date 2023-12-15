recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter your recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients_input = input("Enter your ingredients, seperated by a comma: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    return recipe

n = int(input("How many recipes would you like to enter?: "))
print("----------")

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    print()
    
print("\n--------------------------\nRecipe Details\n--------------------------")
for recipe in recipes_list:
    num_ingredients = len(recipe["ingredients"])
    cooking_time = recipe["cooking_time"]

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print(f"Recipe: {recipe['name'].title()}\n  Time: {recipe['cooking_time']} mins")
    print("  Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"  - {ingredient.title()}")
    print(f"  Difficulty: {difficulty}")
    print()

print("\n--------------------------\nComplete Ingredients List\n--------------------------")
for ingredient in sorted(ingredients_list):
    print(f"- {ingredient.title()}")