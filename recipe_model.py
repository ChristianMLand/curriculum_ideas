from flask_app.config import connectToMySQL
from flask_app import DB
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
        return user_model.User.get_one({"id":self.creator_id})
# --------------------- Commonly needed -----------------------#
    @classmethod
    def get_one_with_creator(cls,data):# modeled like a one to one
        query = '''
                SELECT * FROM recipes
                JOIN users ON creator_id = users.id
                WHERE recipes.id = %(id)s;
                '''
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            row = results[0]
            one_recipe = cls(row)
            user_data = {
                **row,
                "id" : row['users.id'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
            one_recipe.creator = user_model.User(user_data)
            return one_recipe

    @classmethod
    def get_one_with_favoriters(cls,data): # modeled like a one to many
        query = ''
        results = connectToMySQL(DB).query_db(query,data)

    @classmethod
    def get_all_with_creator(cls): # modeled like many to one
        query = '''
                SELECT * FROM recipes
                JOIN users ON users.id = creator_id;
                '''
        results = connectToMySQL(DB).query_db(query)
        if results:
            all_recipes = []
            for row in results:
                one_recipe = cls(row)
                user_data = {
                    **row,
                    "id" : row['users.id'],
                    "created_at" : row['users.created_at'],
                    "updated_at" : row['users.updated_at']
                }
                one_recipe.creator = user_model.User(user_data)
                all_recipes.append(one_recipe)
            return all_recipes

# ------------------ Not commonly needed ----------------------#
    @classmethod
    def get_all_with_favoriters(cls): # modeled like many to many
        query = ''
        results = connectToMySQL(DB).query_db(query)
# -------------------------------------------------------------#
