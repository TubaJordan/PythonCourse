import pickle

recipe = {
    "ingredient_name": "Tea",
    "ingredients": ["Tea Leaves", "Water", "Sugar"],
    "cooking_time": 5,
    "difficulty": "Easy"
}

my_file = open("recipe_binary.bin", "wb") 
pickle.dump(recipe, my_file)
my_file.close()