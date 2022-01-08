Recorded video demo: https://youtu.be/xLIyyMzol34

# Different Types of Association
In the last section we learned how we could pull data from two related tables with a single query, and connect them together with python objects in order to more efficiently retrieve and display the data we want. However, with there being multiple types of SQL relationships (one to one, one to many, many to many), the way that we do that association won't always look exactly the same. 
There are 4 forms of association that you might encounter
- [Many to One](#many-to-one)
- [One to Many](#one-to-many)
- [One to One](#one-to-one)
- [Many to Many](many_to_many.md)

It's important to note that just because you have a particular type of relationship in the database, it does not necessarily mean you will model the relationship the same when you do association.

# Many to One <a href="#" id="many-to-one"></a>
The first type of association, the many to one, is the way we handled it in the [last section](relationships.md). This form of association is used when you need to get all rows from a table that has a foreign key to another table. 
>Example:  get all recipes and their creators

```py
from flask_app.models import user_model#import the user_model file

class Recipe:
    #other methods removed for clarity
    @classmethod
    def get_all_recipes_with_creator(cls):
        query = '''
                SELECT * FROM recipes
                JOIN users
                ON recipes.creator_id = users.id
                '''
        results = connectToMySQL(DB).query_db(query)
        all_recipes = []#create empty list to hold recipe objects
        if results:
            for row in results:
                recipe = cls(row)#create recipe object
                creator_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                recipe.creator = user_model.User(creator_data)#create user object
                all_recipes.append(recipe)
        return all_recipes
```
# One to Many <a href="#" id="one-to-many"></a>
This next form of association is easy to get confused with the previous form, but instead of directly filling a list with objects, we first make a single object and assign it a new attribute with an empty list that then gets filled by our loop. This form of association is used when you want to get a single row from a table, and all of the rows from a different table that have a foreign key connecting to it. **Note that this form of association can also be used if you have a many to many relationship in the database**
>Example: get one user and all of the recipes that they have created
```py
from flask_app.models import recipe_model
class User:
    #other methods removed for clarity
    @classmethod
    def get_one_with_recipes_created(cls,data):
        query = '''
                SELECT * FROM users 
                LEFT JOIN recipes 
                ON users.id = recipes.creator_id
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            user = cls(results[0])#create user object
            user.recipes_created = []#create list in order to store the recipes
            for row in results:
                recipe_data = {
                    "id" : row['recipes.id'],
                    "name" : row['name'],
                    "description" : row['description'],
                    "instructions" : row['instructions'],
                    "under_30" : row['under_30'],
                    "date_made" : row['date_made'],
                    "creator_id" : row['creator_id'],
                    "created_at" : row['recipes.created_at'],
                    "updated_at" : row['recipes.updated_at']
                }
                recipe = recipe_model.Recipe(recipe_data)#create recipe object
                user.recipes_created.append(recipe)
            return user
```
# One to One <a href="#" id="one-to-one"></a>
This is by far the easiest form of association, as there is no loop required at all here. All we need to do is create one object for each table, and connect them with an attribute! **Note that even though the relationship is a one to many in the database, we are modeling it like a one to one for this particular situation.**
>Example: get one recipe with its creator
```py
from flask_app.models import user_model
class Recipe:
    @classmethod
    def get_one_with_creator(cls,data):
        query = '''
                SELECT * FROM recipes
                JOIN users 
                ON recipes.creator_id = users.id
                WHERE recipes.id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            row = results[0]#store the first row in a variable
            recipe = cls(row)#create the recipe object
            creator_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            recipe.creator = user_model.User(creator_data)#create the user object
            return recipe
```