import pickle

# Prints a decorative header for the application
def print_header():
    print("********************************************************************************************************************")
    print("********************************************************************************************************************")
    print("   ______    _______  _______  ___   _______  _______       _______  _______  _______  ______    _______  __   __   ")
    print("  |    _ |  |       ||       ||   | |       ||       |     |       ||       ||   _   ||    _ |  |       ||  | |  |  ")
    print("  |   | ||  |    ___||       ||   | |    _  ||    ___|     |  _____||    ___||  |_|  ||   | ||  |       ||  |_|  |  ")
    print("  |   |_||_ |   |___ |       ||   | |   |_| ||   |___      | |_____ |   |___ |       ||   |_||_ |       ||       |  ")
    print("  |    __  ||    ___||      _||   | |    ___||    ___|     |_____  ||    ___||       ||    __  ||      _||       |  ")
    print("  |   |  | ||   |___ |     |_ |   | |   |    |   |___       _____| ||   |___ |   _   ||   |  | ||     |_ |   _   |  ")
    print("  |___|  |_||_______||_______||___| |___|    |_______|     |_______||_______||__| |__||___|  |_||_______||__| |__|  \n")
    print("********************************************************************************************************************")
    print("********************************************************************************************************************\n")

# Displays a single recipe in a readable format
def display_recipe(recipe):
    print(f"\nRecipe: {recipe['name'].title()}")
    print(f"  Time: {recipe['cooking_time']} mins")
    print("  Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"  - {ingredient.title()}")
    print(f"  Difficulty: {recipe['difficulty']}")

# Searches for recipes containing a specific ingredient
def search_ingredient(data):
    all_ingredients = data["all_ingredients"]
    print("\n-----------------------")
    print(" Full Ingredients List ")
    print("-----------------------")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i+1}.) {ingredient.title()}")
    
    # Validate user input for selecting an ingredient
    try:
        while True:
            choice = int(input("\nEnter the number of the ingredient to search: "))
            if 1 <= choice <= len(all_ingredients):
                ingredient_searched = all_ingredients[choice-1]
                break
            print(f"Please enter a number between 1 and {len(all_ingredients)}.")
        
        # Find recipes containing the chosen ingredient
        recipes_with_ingredient = [recipe for recipe in data["recipes_list"] if ingredient_searched in recipe["ingredients"]]
        num_recipes = len(recipes_with_ingredient)

        # Display count of found recipes
        recipe_word = "Recipe" if num_recipes == 1 else "Recipes"

        decoration = "-" * (len(f"{num_recipes} {recipe_word} found containing {ingredient_searched.title()}") + 2)
        print(f"\n{decoration}")
        print(f" {num_recipes} {recipe_word} found containing {ingredient_searched.title()} ")
        print(f"{decoration}")

        # Display each found recipes
        for recipe in recipes_with_ingredient:
            display_recipe(recipe)

    # Handle invalid inputs
    except ValueError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("No such ingredient number.")

# Main script execution
print_header()  
filename = input("Enter the filename of your recipe data: ")

# Load data from the file and search for recipes
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
else:
    search_ingredient(data)