
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

'''# Cloud
uri = "mongodb+srv://<usuario>:<senha>@pymongo.4bibv.mongodb.net/?retryWrites=true&w=majority&appName=pyMongo"
# Create a new client and connect to the server using the URI
conn = MongoClient(uri, server_api=ServerApi('1'))'''

# Create a new client and connect to the server LOCAL
conn = MongoClient()
