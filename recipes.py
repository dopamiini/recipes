"""Helper functions for recipe-related database operations."""
import db


def add_recipe(user_id, form):
    """Add a recipe and its categories to the database."""
    sql = """INSERT INTO recipes
             (user_id, title, description, ingredients, instructions)
             VALUES (?, ?, ?, ?, ?)"""

    db.execute(sql, [
        user_id,
        form["title"],
        form["description"],
        form["ingredients"],
        form["instructions"],
    ])


def get_recipes():
    """Helper function for an empty search field."""
    sql = "SELECT id, user_id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)


def get_recipe(recipe_id):
    """Helper function to display recipe contents for several pages."""
    sql = """SELECT users.username,
                    users.id AS user_id,
                    recipes.id,
                    recipes.title,
                    recipes.description,
                    recipes.ingredients,
                    recipes.instructions
             FROM recipes, users
             WHERE recipes.user_id = users.id AND 
                   recipes.id = ?"""
    res = db.query(sql, [recipe_id])
    return res[0] if res else None
