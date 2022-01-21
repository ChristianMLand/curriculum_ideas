# Caching
Last time we took a look at the property decorator and saw how it could simplify our code while also making it more dynamic at the same time. However, one issue that can arise when using the property decorator, is that since the properties get calculated upon access, it's very easy to create a situation where you end up querying for the same thing many times in the same request-response cycle.

One way we can deal with situations like that is by implementing caching for our queries. Essentially the first time a query is sent to our database, we should remember what we get back and store it somwhere, and then if we ever see that query again, we can instead just grab the value that we stored from the first time instead of calling the database again. The only other thing we need to consider, is that we want our cache to exist for just a single request response cycle at a time, as otherwise our data can fall out of sync with what is in the database.

So how do we actually go about implementing something like this?

TODO

```py


```