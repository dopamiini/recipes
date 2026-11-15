## Testing the Application

The application can be tested manually by following the checklist below. These tests cover the current functionalities of the application, these include user registration, authentication, recipe management, search, and navigation. This is mostly fairly intuitive. Here's a coverage of successful test cases.

### 1. Testing user registration

- Open the registration page by clicking **Register**.
- Register a new account and verify that it is created successfully.
- There is no enforcement for password complexity or rate limiting, as it is easier to test the app this way.
- Try submitting a registration form with invalid or missing information in some combination and verify that appropriate validation errors are displayed. For example, registering another account with the same username should fail and display an error message.

### 2. Testing login and logout

- Open the login page by clicking **Sign in**.
- Try logging in with the registered username and password, this should succeed.
- Try logging in with any combination of invalid or missing information and verify that appropriate validation errors are displayed. For example, a username that doesn't exist.

### 3. Testing recipe creation

*You must be logged in to create recipes.*

- Open the recipe creation page by clicking **Add recipe**.
- Enter the recipe title, description, ingredients, instructions, and categories. Click Add recipe. You should be redirected to the main page and your recipe is now added.
- Try submitting missing, invalid or excessively long inputs and verify that server-side validation works as expected.

### 4. Testing recipe viewing and navigation

- Click on a recipe title from the recipe list and verify that you can access the recipe's detailed page.
- Use the available navigation links and buttons to verify that they lead to 'appropriate' pages.
- You can create a second account and verify that the application enforces server-side access restrictions to pages that you are not supposed to be able to visit. 

### 5. Testing recipe editing and deletion

*You must be logged in and own the recipe to edit or delete it.*

- Open one of your own recipes and click **Edit**.
- Verify that the existing recipe information is displayed in the form.
- Change some information and save the changes. Verify that the updated information is displayed correctly.
- Try submitting a recipe that has some fields empty and note that server-side validation is enforced.
- Log in as another user and verify that you cannot edit or delete recipes belonging to someone else.
- Delete your own recipe and verify that it disappears from the recipe list. You can also check the database.

### 6. Testing recipe search

- Search for a recipe by its title, description or a relevant keyword and verify that matching recipes are displayed.
- Search for a term that does not match any recipes and verify that an appropriate empty result is displayed.
- Submit an empty search field and verify that all recipes are displayed.
- Try searching for recipes by entering a search term in the search field.
- Test searching while logged out to verify that public recipe browsing works similarly.

### 7. Testing Access Control and Security

- Verify that creating, editing, and deleting recipes requires authentication.
- Verify that users cannot modify or delete another user's recipes by accessing a URL directly.
- Submit forms without a valid CSRF token and verify that the requests are rejected.
- Enter unusual or malicious-looking text into form fields and verify that input validation and output escaping work correctly.
