from django.test import TestCase
from .models import Category, Recipe
from datetime import datetime

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(str(self.category), "Desserts")

    def test_category_iter(self):
        self.assertEqual(list(self.category), ["Desserts"])

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="A delicious cake",
            instructions="Mix and bake",
            ingredients="Flour, sugar, cocoa",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Chocolate Cake")
        self.assertEqual(self.recipe.description, "A delicious cake")
        self.assertEqual(self.recipe.instructions, "Mix and bake")
        self.assertEqual(self.recipe.ingredients, "Flour, sugar, cocoa")
        self.assertEqual(self.recipe.category, self.category)
        self.assertEqual(str(self.recipe), "Chocolate Cake")

    def test_recipe_timestamps(self):
        self.assertIsInstance(self.recipe.created_at, datetime)
        self.assertIsInstance(self.recipe.updated_at, datetime)