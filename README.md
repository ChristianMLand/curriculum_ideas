# Relationships through association
![Erd](erd.png?raw=true "Erd Diagram")
______________________________________
When developing our websites, often times we will find ourselves in a situation where we want to display information from multiple tables in the same location. An example of this could be wanting to display a list of all recipes that have been created, alongside the user who created them. One way that we could accomplish that is to qeury for all the recipes in the data base, as well as all the users in the database. 
```py
class Recipe:
    #other methods removed for clarity
    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL(DB).query_db(query)
        all_recipes = []
        if results:#if the query succeeded and returned at least one row
            for row in results:
                recipe = cls(row)#create a recipe object using the row data
                all_recipes.append(recipe)
        return all_recipes

# same method would be created for the user class as well
```
Then we could have a nested for loop in our jinja template, where we first loop through each recipe, and then loop through each user, checking if the `creator_id` of the recipe matches the `id` of the user, and if so, display the recipe data and the corresponding user data to the page.

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Date Made</th>
            <th>Creator Name</th>
        </tr>
    </thead>
    <tbody>
        {% for recipe in all_recipes %}
        <tr>
            <td>{{recipe.name}}</td>
            <td>{{recipe.date_made}}</td>
            {% for user in all_users %}
                {% if user.id == recipe.user_id %}
                <td>{{user.first_name}}</td>
                {% endif %}
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>
```

Now, although using that approach would display the correct data, there are a few big problems with it. First off, we are potentially querying for a lot more data than we actually need. Remember, what we want is *all of the recipes*, as well as the *creator of each recipe*. However, with our approach, we are always querying for all of the users, even if they haven't created any recipes yet. Depending on the data in our database, that could be a huge amount of data we are querying for that we aren't actually interested in! The other major issue with this approach is that we need to have a nested for loop with a conditional, which is not very efficient, especially with large datasets. 

So if that approach is no good, what can we do better? Well the first step should come as no surprise. Instead of doing two seperate queries, we can do a join to get data from both tables in a single query. 
```sql
SELECT * FROM recipes
JOIN users
ON recipes.creator_id = users.id
```
This this is great, it will give us the recipe data, as well as the data for the user who created them! However, now there's now a new problem we need to address. The way we set up our `connectToMySQL.py` file determines that `SELECT` queries to the database will return us a tuple of dictionaries. One thing you might remember about dictionaries, is that they require all keys to be unique, and if we are wrapping up both recipe data and user data into the same dictionary theres going to be some overlap with keynames. The way that PyMySQL handles this, is the first instance of the column names (whatever the left table in your query is) will have the keys named normally, however any duplicate column names will have their corresponding table name prefixed to the column name as the key instead.
```py
from flask_app.models import user_model#import the user_model file

class Recipe:
    #other methods removed for clarity
    @classmethod
    def get_all_recipes(cls):
        query = '''
                SELECT * FROM recipes
                JOIN users
                ON recipes.creator_id = users.id
                '''
        results = connectToMySQL(DB).query_db(query)
        all_recipes = []
        if results:#if the query succeeded and returned at least one row
            for row in results:
                recipe = cls(row)
                #logic up to this point stays the same
                #now we need to parse out the user data from the row dictionary, making sure to specify the duplicate column names
                creator_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                recipe.creator = user_model.User(creator_data)#create a user object with the creator data, and connect it to the recipe object through an instance attribute
                all_recipes.append(recipe)
        return all_recipes

# no longer need to create a corresponding method for the User class
```
With these changes, we now are able to make a single query to the database, and also no longer need to manually filter the users to figure out which user is connected to a given recipe. So now to display this information in our jinja template all we need is a single loop, thus solving all of our original issues!
```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Date Made</th>
            <th>Creator Name</th>
        </tr>
    </thead>
    <tbody>
        {% for recipe in all_recipes %}
        <tr>
            <td>{{recipe.name}}</td>
            <td>{{recipe.date_made}}</td>
            <td>{{recipe.creator.first_name}}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```