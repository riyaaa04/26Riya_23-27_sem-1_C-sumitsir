#Design a recipe management system with classes for recipes, ingredients, andusers. Implement methods for adding recipes, searching by ingredients
class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient.name}")
        print("Instructions:")
        print(self.instructions)
        print()

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            if any(ingredient.name.lower() == ingredient_name.lower() for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

# Example usage with user input:
recipe_manager = RecipeManager()

while True:
    print("1. Add Recipe")
    print("2. Search by Ingredient")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter recipe name: ")
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break
            ingredient = Ingredient(ingredient_name)
            ingredients.append(ingredient)
        instructions = input("Enter recipe instructions: ")
        recipe = Recipe(name, ingredients, instructions)
        recipe_manager.add_recipe(recipe)
        print("Recipe added successfully!\n")

    elif choice == "2":
        ingredient_name = input("Enter ingredient to search for: ")
        matching_recipes = recipe_manager.search_by_ingredient(ingredient_name)
        if matching_recipes:
            print("\nMatching Recipes:")
            for recipe in matching_recipes:
                recipe.display_recipe()
        else:
            print(f"No recipes found with {ingredient_name}\n")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
