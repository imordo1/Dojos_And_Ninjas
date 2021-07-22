# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


#### ---------------- Dojo Class --------- ######
# model the class after the friend table from our database
class Dojo:

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one(cls,data): 
        query = "SELECT * FROM dojos where id=%(id)s ;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls(results[0]) 
        return dojo

# Let's add the functionality that allows us to create a friend. 
    # class method to save our friend to the database
    #### --------- SAVE to the database ---------- ####
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

#### ---------------- NINJA Class --------- ######

class Ninja:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Now we use class methods to query our database
    @classmethod
    def get_all_ninjas_by_dojo_id(cls,data):
        query = "SELECT * FROM ninjas WHERE %(dojo_id)s = ninjas.dojo_id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

# Let's add the functionality that allows us to create a nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnew Ni. 
    # class method to save our friend to the database
    #### --------- SAVE to the database ---------- ####
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name , last_name, age, dojo_id,created_at, updated_at ) VALUES ( %(first_name)s ,%(last_name)s ,%(age)s ,%(dojo_id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )



