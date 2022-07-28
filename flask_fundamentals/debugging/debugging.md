# Common Error types
## 405 method not allowed
### What's the problem?
> You tried to submit a post request to a get route or get request to a post route.
### Possible causes:
- You redirected to a post route in your controller
- You did not set the right method type on your form in the HTML
- You are not accepting the right method types in your controller route
----------------
## 404 Not Found
### What's the problem?
> You tried going to a route that has not been registered.
### Possible causes:
- You have a typo in your form action path or link href
- You have a typo in your redirect in your controller
- You forgot to pass a required variable into the route
- You forgot to import your controller files into your server
---------------
## Key Error __
### What's the problem?
> You tried to access a dictionary with a key that does not currently exist.
### Possible causes:
- The names of your inputs in your html form do not match with the keys you are trying to access in request.form
- You are accessing a key in session before you instantiate it
---------------
## View function mapping is overwriting an existing endpoint function
### What's the problem?
> You have multiple route functions with the same name
### Possible causes:
- You have the same route in both of your controllers
- You copy pasted a route and forgot to change the name of the function
--------------
## The view function did not return a valid response
### What's the problem?
> You did not return from your route function properly
## Possible causes:
- You have a condition in your route function, and only return in one of the scenarios
- You are returning something of an invalid type
-------------
## ___ is not iterable
### What's the problem?
> You are iterating (looping) over something other than a list,dictionary, or tuple
### Possible causes:
- You are attempting to loop over a single object instead of a list of objects
- Your model method returned you either False or None due to your query failing, when you were expecting to recieve a list
------------
## Datatype is not subscriptable
### What's the problem?
> You are attempting to access a key or index of something other than a list,dictionary or tuple
### Possible causes:
- You are using square brackets to access an attribute of object instead of dot notation
- Your model method returned you either False or None due to your query failing, when you were expecting to recieve a list
-------------
## Unexpected end of template
### What's the problem?
> You didn't properly close a code block in your jinja template
### Possible causes:
- You simply forgot to put the `{% endfor %}` or `{% endif %}` in your template
- You put a space between the words in your closing tag
- You had a nested for loop or conditional and only closed one of them
## Datatype has no method _____
### What's the problem?
> You are attempting to call a method that hasn't been defined yet for that class
### Possible causes:
- You have a typo in the method name either in your invokation, or where it was defined
- You simply forgot to create that method in your class
- Your indentation for the method is incorrect, making it unable to be seen by the class
------------------
## Template cannot be found
### What's the problem?
> The HTML file you are attempting to render cannot be found by flask.
### Possible causes:
- You have a typo in the filename
- Your HTML file is not inside the templates folder
- Your templates folder is in the wrong location
-----------------
## Something went wrong: Format requires a mappping
### What's the problem?
> The SQL query you made uses a prepared statement, but you didn't provide it the data to format with.
### Possible causes:
- You forgot to pass in data to your `query_db` method
- you passed in something other than a dictionary into data
- you have a '%' somewhere in your query string other than in a prepared statement, and forgot to remove the data from the execute method in your `mysqlconnection.py` file
-----------------

TODO
