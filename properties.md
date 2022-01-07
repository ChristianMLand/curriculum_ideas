# Association with Properties
So previously, we learned how we could associate two tables together through joins and parsing the data in to different objects. That approach works great for most situations, but it does have a few flaws of its own. For starters, there's a fair amount of repeated logic between the different methods. Even though the functions are structured a bit differently, a lot of the core logic is the same for all of them. Another issue we saw, was how much more logic was required for modeling data as a many to many relationship when following that approach. So if that approach isn't perfect either, then what other options do we have available to use for handling association? 

Introducing the property decorator! The `property` decorator is similar to the `classmethod` and `staticmethod` decorators, in that you apply it to a method inside of a class. What's different about it, is that you can access methods that use the `property` decorator as if they were attributes, and their values will be calculated only when you attempt to access them, rather than upon object creation. To better illustrate why that's useful for us, let's take a look at an example of how it in action.

```py
from flask_app.models import user_model
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator_id = data['creator_id']

    @property
    def creator(self):
        user_data = {
            'id' : self.creator_id
        }
        return user_model.User.get_one(user_data)#retrieves a user object based on the recipes creator_id
...
class User:
    @classmethod
    def get_one(cls,data):
        query = '''
                SELECT * FROM users
                WHERE id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            return cls(results[0])
```
Immediately you might recognize that we no longer need to join the tables together at all, and we also no longer need to parse out the individual table data into seperate objects. All we need to do is call the `get_one` method that we have already created for the `User` class and return the result from our property method. Now nothing needs to change in terms of the way we access our data in our controllers and templates and we know can use that `creator` property on every single recipe object no matter if we call the `get_one` method or the `get_all` method in the `Recipe` class since we have *de-coupled* the association from the methods that handle querying the database!

As you can probably guess, we can do the same thing for all our other forms of association. However, in order to replace all of our associations with properties, we need to change the way we structure our `get_one` and `get_all` methods in order to make them a bit more dynamic. 

Here's a reminder of how our `get_all` and `get_one` methods might look up to this point
```py
class User:
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DB).query_db(query)
        all_users = []
        if results:
            for row in results:
                all_users.append(cls(row))
        return all_users

    @classmethod
    def get_one(cls,data):
        query = '''
                SELECT * FROM users
                WHERE id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query)
        if results:
            return cls(results[0])
```
The current implementations worked great for our purposes up until this point, but their main issue is that they aren't very flexible. Our `get_all` method always retrieves everything no matter what, but what if we wanted to get all users with a `first_name` equal to Chris? What if we wanted to get one user by `email` instead of by `id`? With the way we have currently implemented these methods, our only option would be to simply make a seperate function for each possibility. Our next iteration of these methods will aim to solve that problem, so that no matter how we want to filter the data, we can use the same methods!

Let's first look at how we can modify our `get_all` method so that we can optionally filter our results by any column we want. Our first draft of this new version adds quite a bit of logic in order to dynamically generate our query string, but we will look at how we shorten it right after.
```py
class User:
    @classmethod
    def get_all(cls,data=None):# add an optional data parameter 
        query = 'SELECT * FROM users'# the base query stays the same
        if data:# check if data exists
            query += ' WHERE '#concatenate the ' WHERE ' keyword to our query string if it does
            for i,key in enumerate(data):#enumerate the data dictionary so we can get both the index as well as the key
                query += f'{key} = %({key})s'#concatenate an f-string that formats the key into a prepared statement
                if i < len(data) - 1:#check to see if we are on the last key yet
                    query += f' AND '# if not, concatenate an ' AND ' to our query string in order to seperate out multiple WHERE clauses.
        query += ';'#concatenate a semicolon to terminate our query string
        results = connectToMySQL(DB).query_db(query)# the rest of the logic remains the same!
        all_users = []
        if results:
            for row in results:
                all_users.append(cls(row))
        return all_users
```
Now this version definitely accomplishes what we need, and is very explicit in the process of generating the query, however there's a lot going on and it loses a bit of readability. We can actually shorten this logic even further using a combination of the `join` function and a generator expression. For our purposes, we don't really need to worry too much about the specifics of how generator expressions work, we can simply consider them as a way of doing an inline for loop that applies some expression on each iteration. The expression we are using is essentailly creating a string for each key in our data dictionary and then passing in the all of those strings into the join function. The join function then joins all of the strings together on the provided seperator, which in our case is ' AND '. With these improvements we've cut down our code quite a lot, while stil remaining dynamic!
```py
class User:
    @classmethod
    def get_all(cls,data=None):# add an optional data parameter 
        query = 'SELECT * FROM users'# the base query stays the same
        if data:# check if data exists
            query += ' WHERE '#concatenate the ' WHERE ' keyword to our query string
            # for each key in the data dictionary, create a prepared statement, and then join all of the strings together with an ' AND ' in-between them
            query += ' AND '.join(f'{key} = %({key})s' for key in data)
        query += ';'#concatenate a semicolon to terminate our query string
        results = connectToMySQL(DB).query_db(query)# the rest of the logic remains the same
        all_users = []
        if results:
            for row in results:
                all_users.append(cls(row))
        return all_users
```
The same trick can be used on our `get_one` method. However, since we always need some sort of data to filter by, if we are getting a single object, it makes the logic even simpler!
```py
class User:
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE '# the base query 
         # for each key in the data dictionary, create a prepared statement, and then join all of the strings together with an ' AND ' in-between them
        query += ' AND '.join(f'{key} = %({key})s' for key in data)
        query += ';'#concatenate a semicolon to terminate our query string
        results = connectToMySQL(DB).query_db(query)# the rest of the logic remains the same
        if results:
            return cls(results[0])
```
Now that we have these new and improved methods, we can use properties to handle that messy many to many modeling we encountered previously in a much shorter and cleaner way.
```py
from flask_app.models import recipe_model
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @property
    def recipes_created(self):
        return recipe_model.Recipe.get_all({'creator_id':self.id})
```
