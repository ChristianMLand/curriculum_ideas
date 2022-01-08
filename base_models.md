# Creating A Reusable Base Model
We saw in an earlier section how we could make our `get_one` and `get_all` methods more dynamic, so that they could work with any data we want to filter by. The goal of this was to reduce repeated code, so that way we could have just one or two methods to handle all of our `SELECT` query needs. However, you might have noticed that although we did reduce our code duplication by quite a bit, we are still repeating code across our different models. In the previous example, both the `Recipe` class and the `User` class had `get_one` and `get_all` methods, which had nearly identical code. Any time we notice we have duplicate code somewhere, we should always be looking for  ways to reduce it, so how exactly can we go about doing that here? 

If you think back to when we first covered the four pillars of OOP, we talked about inheritance, which is where a class can *inherit* methods and attributes from a parent class. Since we know that we want all of our models to be able to have `get_all` and `get_one` methods we could create a base class that defines those methods, and then have all our models inherit from it. This will make it so we only need to write those methods once, greatly reducing our code duplication!

Currently the only difference between the `get_one` in the `Recipe` class and the `get_one` in the `User` class, is the table name inside the query. In order to make these methods work for our base model, we need to figure out how we can make that table name dynamic as well. There are multiple approaches we can take, but f the most straightforward is making the table name a class attribute in our model classes. 
```py
class Model:
    @classmethod
    def get_one(cls,data):
        query = f'SELECT * FROM {cls.table} WHERE '
        query += 'AND '.join(f'{key} = %({key})s ' for key in data)
        query += 'LIMIT 1;'
        results = connectToMySQL(DB).query_db(query)
        if results:
            return cls(results[0])

    @classmethod
    def get_all(cls,data=None):
        query = f'SELECT * FROM {cls.table}'
        if data:
            query += ' WHERE '
            query += 'AND '.join(f'{key} = %({key})s ' for key in data)
        query += ';'
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            return [cls(row) for row in results]

...

class User(Model):
    table = "users"
    def __init__(self,data):
        ...

class Recipe(Model):
    table = "recipes"
    def __init__(self,data):
        ...
```
By using this approach we are now able to inherit the `get_one` and `get_all` methods from our base model, so we no longer need to rewrite those methods for each model we create!

We just saw how we could make our `SELECT` queries dynamic and abstract them into a base class, however what about the other types of queries we might need to do? Lets take a look at how we can apply those same concepts to our create, update, and delete methods.

## Create
```py
@classmethod
def create(cls,data):
    query = f'INSERT INTO {cls.table} ('#pass in the table name
    query += ', '.join(key for key in data)#join the column names together seperated by comma
    query += ') VALUES ('
    query += ', '.join(f'%({key})s' for key in data)#create prepared statements for column names
    query += ');'#terminate query
    return connectToMySQL(DB).query_db(query,data)
```

## Update
```py
@classmethod
def update(cls,data):
    query = f'UPDATE {cls.table} SET '#pass in the table name
    query += ', '.join(f'{key} = %({key})s' for key in data)#join the column names together seperated by comma
    query += ' WHERE '
    query += 'id = %(id)s;'
    return connectToMySQL(DB).query_db(query,data)
```

## Delete
```py
@classmethod
def delete(cls,data=None):
    query = f'DELETE FROM {cls.table}'#pass in the table name
    if data:
        query += ' WHERE '
        query += ' AND '.join(f'{key} = %({key})s' for key in data)#join the column names together seperated by comma
    query += ';'#terminate query
    return connectToMySQL(DB).query_db(query,data)
```
