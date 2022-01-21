from flask_app.config import connectToMySQL
from flask_app import DB
from flask_app.models import recipe_model

class User:
    def __init__(self,data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __eq__(self,other) -> bool:
        return self.id == other.id and type(self) is type(other)

    @property
    def recipes_created(self):
        return recipe_model.Recipe.get_all({"creator_id":self.id})

# -----------------------Commonly needed------------------------#
    @classmethod
    def get_one_with_recipes_created(cls,data):# modeled like a one to many
        query = '''
                SELECT * FROM users 
                LEFT JOIN recipes ON users.id = creator_id
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_user = cls(results[0])
            one_user.recipes_created = []
            for row in results:
                recipe_data = {
                    "id" : row['recipes.id'],
                    "created_at" : row['recipes.created_at'],
                    "updated_at" : row['recipes.updated_at'],
                    "name" : row['name'],
                    "description" : row['description'],
                    "instructions" : row['instructions'],
                    "under_30" : row['under_30'],
                    "date_made" : row['date_made'],
                    "creator_id" : row['creator_id']
                }
                recipe = recipe_model.Recipe(recipe_data)
                one_user.recipes_created.append(recipe)
            return one_user

    @classmethod
    def get_one_with_recipes_favorited(cls,data):# modeled like a one to many
        query = '''
                SELECT users.*,recipes.* FROM users
                LEFT JOIN favorites ON favoriter_id = users.id
                LEFT JOIN recipes ON recipe_id = recipes.id
                WHERE users.id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_user = cls(results[0])
            one_user.recipes_favorited = []
            for row in results:
                recipe_data = {
                    **row,
                    "id" : row['recipes.id'],
                    "created_at" : row['recipes.created_at'],
                    "updated_at" : row['recipes.updated_at'],
                }
                recipe = recipe_model.Recipe(recipe_data)
                one_user.recipes_favorited.append(recipe)
            return one_user
# --------------------Not commonly needed-----------------------#
    @classmethod
    def get_all_with_recipes_created(cls): # modeled like many to many
        query = '''
                SELECT * FROM users
                LEFT JOIN recipes ON users.id = creator_id;
                '''
        results = connectToMySQL(DB).query_db(query)
        if results:
            all_users = []
            for user in results:
                one_user = cls(user)
                if one_user not in all_users:
                    one_user.recipes_created = []
                    for recipe in results:
                        if recipe['creator_id'] == one_user.id:
                            recipe_data = {
                                **recipe,
                                "id" : recipe['recipes.id'],
                                "created_at" : recipe['recipes.created_at'],
                                "updated_at" : recipe['recipes.updated_at'],
                            }
                            one_recipe = recipe_model.Recipe(recipe_data)
                            one_user.recipes_created.append(one_recipe)
                    all_users.append(one_user)

    @classmethod
    def get_all_with_recipes_favorited(cls): # modeled like many to many
        query = ''
        results = connectToMySQL(DB).query_db(query)
# --------------------------------------------------------------#