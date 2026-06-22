# Example Python Code to Insert a Document

from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus # To help with the '@' character in my password


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST='localhost', PORT=27017, DB='aac', COL='animals'): # Requires username and password to be passed, other arguments have defaults
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections.
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'Drink@123!'
        # HOST = 'localhost'
        # PORT = 27017
        # DB = 'aac'
        # COL = 'animals'
        #
        # Initialize Connection
        #
        
        escaped_pass = quote_plus(PASS) # This '"cleans" a password that may include a character like '@'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, escaped_pass, HOST, PORT)) #using the 'cleaned' version of my password
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

        # Create a method to return the next available record number for use in the create method

    # Completed create method - ML
    def create(self, data) -> bool: # Create method will return a boolean value
        if data is not None:
            try: # try-except block to catch any exceptions that may occur during the create operation
                result = self.collection.insert_one(data)  # Insert the document into the animals collection
                if result.acknowledged:  # Check if the insert was acknowledged by MongoDB
                    return True  # Return True if the document was acknowledged
                
                else:
                    
                    return False  # Return False if the document was not acknowledged
                
            except Exception as e: 
                print(f"Error occured trying during create function: {e}")
                
                return False
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Created read method - ML
    def read(self, query) -> list:  # Read method will return a list
        
        if query is not None:
            try: # try-except block to catch any exceptions that may occur during the read operation
                result = self.collection.find(query)  # Find documents in the animals collection that match the query
                return list(result)  # Return the result of the query as a list
            
            except Exception as e:
                print(f"Error occurred during read function: {e}")
                
                return []  # Return and empty list upon exception
            
        else:
            print("Query argument is empty.")
            
            return []  # Return an empty list if the query is None
    
    # Created update method - ML
    def update(self, query, data) -> int: # Update method will return an integer
        
        if query is not None and data is not None: # Confirm that both the search query and data which is to be updated is passed as arguments for this method
            try: # Try-except block to catch any exceptions which may occur during the update
                
                result = self.collection.update_many( # Find the documents m atching the query, and update documents specified data
                    query,
                    {"$set": data}
                )
                
                return result.modified_count # Return the number of objects modified by Mongo
            
            except Exception as e:
                print(f"Error occurred during update function: {e}")
                
                return 0 # Returns 0 upon exception
                
        else:
            
            print("Query and/or data argument is empty.") # If both query and data arent passed, return 0
            
            return 0
        
    # Created delete method - ML
    def delete(self, query) -> int: # Delete method will return an integer
        
        if query is not None: # Confirm a query has been passed as an argument for the delete method
            try: # Try-except block to catch any exceptions which may occur during delete method
                
                result = self.collection.delete_many(query) # Find and delete the matching documents
                
                return result.deleted_count # return the number of deleted documents
            
            except Exception as e:
                print(f"Error occurred during delete function: {e}")
                
                return 0 # Returns 0 upon exception
            
        else:
            print("Query argument is empty.") # If query is not passed, return 0
            
            return 0