# Many to Many
This last form of association is by far the least common and you are not likely to need it, but it's still good to know about for sake of completeness. However before we get into it there's another thing we should cover first that will make the logic required a bit easier for us. Similar to how we've used `__init__` to handle our class contructor or `__repr__` to handle how our objects are represented in the console, there is another useful method we can use which is `__eq__`. The `__eq__` method handles checking whether two objects are considered equal or not, which allows us to do some very useful things such as checking whether a list contains a specific object or not. A very basic implementation we can use for just that purpose would look something like this: 
```py
def __eq__(self,other):
    return self.id == other.id and type(self) is type(other)
```
To break down what this function is doing, first we accept the parameters self and other to the function. Self is the current object, and other is the object we are comparing it to. Since `__eq__` expects us to return a boolean, we return an expression where, if the id's of the two objects are the same, and the types are also the same, then return `True`, otherwise return `False`.

With that piece of code to help us out we can then implement the following logic for our method.
1. Create a list to hold all of our user objects
2. Loop over the results from the database and create a user object for each row
3. Check if the user object already exists inside of the list we created
4. If it doesn't, create an attribute on the user object to hold a list of all the recipes that user has created
5. Loop over the results again and check if the users id matches a recipes creator_id
6. If they do match, create a recipe object and add it to the users list of created recipes
7. append user object to the all_users list
8. return the all_users list
```py
from flask_app.models import recipe_model
class User:
    #other methods removed for clarity
    def __eq__(self,other) -> bool:
        return self.id == other.id and type(self) is type(other)

    @classmethod
    def get_all_with_recipes_created(cls): # modeled like many to many
        query = '''
                SELECT * FROM users
                LEFT JOIN recipes ON users.id = creator_id;
                '''
        results = connectToMySQL(DB).query_db(query)
        if results:
            all_users = []
            for user_row in results:
                user = cls(user_row)
                if user not in all_users:# this only works due to our __eq__ method!
                    user.recipes_created = []
                    for recipe_row in results:
                        if recipe_row['creator_id'] == user.id:
                            recipe_data = {
                                "id" : recipe_row['recipes.id'],
                                "name" : recipe_row['name'],
                                "description" : recipe_row['description'],
                                "instructions" : recipe_row['instructions'],
                                "under_30" : recipe_row['under_30'],
                                "date_made" : recipe_row['date_made'],
                                "creator_id" : recipe_row['creator_id']
                                "created_at" : recipe_row['recipes.created_at'],
                                "updated_at" : recipe_row['recipes.updated_at']
                            }
                            recipe = recipe_model.Recipe(recipe_data)
                            user.recipes_created.append(recipe)
                    all_users.append(user)
                return all_users
```
Again this form of association is not needed very often, even if you have a many to many in the database, you are more likely to model it like a one to many when it comes to association between classes! Although we were able to make this work, you might notice that this solution has many of the same problems we originally ran into before we started implementing association between classes, and you might be wondering if there is an even better way. Coming up next we are going to learn about the property decorator and how we can use that to simplify our associations by a lot!