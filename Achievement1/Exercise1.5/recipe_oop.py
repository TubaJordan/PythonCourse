class Recipe:
    all_ingredients = set() # Class variable to store all unique ingredients across all recipes

    def __init__(self, name, cooking_time):
        self.name = name # Name of the recipe
        self.ingredients = [] # List to store ingredients of this recipe
        self.cooking_time = cooking_time # Cooking time in minutes
        self.difficulty = None # Difficulty level, calculated based on ingredients and cooking time

    def add_ingredients(self, *args):
        # Adds ingredients to the recipe and updates overall ingredient list
        for ingredient in args:
            self.ingredients.append(ingredient)
            self.update_all_ingredients(ingredient)
        self.calculate_difficulty() # Recalculate difficulty after adding new ingredients

    def calculate_difficulty(self):
        # Determines the difficulty of the recipe based on number of ingredients and cooking time
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10:
            self.difficulty = "Easy" if num_ingredients < 4 else "Medium"
        else:
            self.difficulty = "Intermediate" if num_ingredients < 4 else "Hard"

    def get_name(self):
        # Returns the name of the recipe
        return self.name
    
    def set_name(self, name):
        # Sets a new name for the recipe
        self.name = name

    def get_cooking_time(self):
        # Returns the cooking time of the recipe
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        # Sets a new cooking time and recalculates difficulty
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    def get_ingredients(self):
        # Returns the list of ingredients for the recipe
        return self.ingredients

    def get_difficulty(self):
        # Returns the difficulty level, calculates it first if not already set
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        # Checks if an ingredient is in the recipe
        return ingredient in self.ingredients
    
    def update_all_ingredients(self, ingredient):
        # Updates the class variable with new ingredients
        Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        # String representation of the recipe
        return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} mins\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.difficulty}\n"
    
def recipe_search(recipes, search_term):
    # Searches for a given ingredient in a list of recipes
    for recipe in recipes:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Main code
            
# Creating recipe instances and adding ingredients
print("--------------------------------------------------")
print("# Creating recipe instances and adding ingredients")  
print("--------------------------------------------------\n")        

tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)


# Creating a list of recipes and searching for an ingredient
recipes_list = [tea, coffee, cake, banana_smoothie]


# Searching for recipes containing specific ingredients
print("-------------------------------------------------------")
print("# Searching for recipes containing specific ingredients")
print("-------------------------------------------------------")

print("---------------------")
print("Recipes with Water:")
print("---------------------")
recipe_search(recipes_list, "Water")

print("---------------------")
print("Recipes with Sugar:")
print("---------------------")
recipe_search(recipes_list, "Sugar")

print("---------------------")
print("Recipes with Bananas:")
print("---------------------")
recipe_search(recipes_list, "Bananas")