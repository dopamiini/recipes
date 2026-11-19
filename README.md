# Recipes
[![Pylint](https://github.com/dopamiini/recipes/actions/workflows/pylint.yml/badge.svg)](https://github.com/dopamiini/recipes/actions/workflows/pylint.yml)
[![djLint](https://github.com/dopamiini/recipes/actions/workflows/djlint.yml/badge.svg)](https://github.com/dopamiini/recipes/actions/workflows/djlint.yml)

Project for the course TiKaWe implemented with flask and python 3.12. Recipes is a web application that allows users to publish their food recipes. All users can browse and search all recipes. Only registered users can create recipes and manage them.

## Running the Application

You need Python version 3.12 and Flask version 3.1.x or later.

### 1. Clone the repository and navigate to the project directory

```bash
git clone https://github.com/dopamiini/recipes
cd recipes
```

### 2. Create a virtual environment and install Flask

**Linux and macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize the database

This command creates the database using the `schema.sql` and `init.sql` files.

**Linux and macOS:**

```bash
python3 seed.py
```

Windows users use `python` instead of `python3`. You can always reset the database by rerunning the command.

### 4. Start the application

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Basic Functionality
These are the minimum requirements to be implemented for functionality as listed in the course page.

- All users can view all recipes added to the application. ✔️
- All users can search for recipes using keywords. ✔️
- All users can filter recipes by category.
- Users can register an account and then login using that account. ✔️
- In the application, registered users can share their food recipes.
  - A registered user can add, edit and remove their own recipes. All recipe text fields are mandatory. ✔️
  - Each recipe includes a list of required ingredients and preparation instructions. ✔️
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

## Testing

Testing documentation and test cases can be found in the file [testing.md](documents/testing.md).

## Pylint

Pylint report will be added later. You can currently verify the pylint status of the code via the banner at the top of this page.

## Comments
The project currently covers Parts 1–11 of the video lectures. All requirements for the second interim submission should be implemented.
- TODO for next interim submission:
  - Peer evalutation. 
  - Refactor code to use flash() for messages.
  - Refactor html by adding a base.html template and use jinja template inheritance.
  - Look into and possibly expand CI checks with (pytest, coverage, bandit, pip-audit, html-validate, nu html checker).
