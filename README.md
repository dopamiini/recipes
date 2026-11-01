# Recipes
Project for the course TiKaWe. A web application that allows users to publish their food recipes.

## Basic Functionality
These are the minimum requirements to be implemented for functionality as listed in the course page.

- All users can view all recipes added to the application.
- All users can search for recipes using keywords and optionally filter recipes by category.
- Users can register an account and then login using that account.
- In the application, registered users can share their food recipes.
  - A registered user can add, edit and remove their own recipes. All recipe text fields are mandatory.
  - Each recipe includes a list of required ingredients and preparation instructions.
  - Registered users can optionally also add a picture to a recipe (png file format).
- The app has a user page that shows information about the user and their added recipes.
  - It shows the number of recipes the user has added.
  - It lists all the recipes the user has added.
- The user can assign one or more categories to a recipe. Categories are divided into the following types:
  - **Type**: Breakfast, Lunch, Dinner, Snack, Dessert
  - **Diet**: None, Keto, Dairy-free, Paleo, Vegan
- Registered users can comment and rate other recipes.
  - Recipes show user comments. Each user can add multiple comments to each recipe.
  - Recipes show the average rating score. Each user can only rate a single recipe once.

## Data Entities
The primary entity is a **recipe**, and the secondary entities are **comments** and **ratings** associated with a recipe.

## Extended Functionality
These are additional features that will be added.

- Pagination

## Comments
These may see updates during the course of the project.
