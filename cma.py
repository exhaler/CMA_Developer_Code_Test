import requests
from pymongo import MongoClient
from uuid import uuid4

# CONSTANT
URI = "<YOUR_CONNECTION_STRING>"
DB_NAME = "<YOUR_DATABASE_NAME>"
COLLECTION_NAME = "<YOUR_COLLECTION_NAME>"
API_URL = "https://openaccess-api.clevelandart.org/api/artworks"

# Create a new client and connect to the server
client = MongoClient(URI, uuidRepresentation="standard")

# Select the database and collection
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# remove all documents from collection
collection.delete_many({})


def find_highlight_artwork(exhibition_keyword, created_after):
    params = {"q": exhibition_keyword, "created_after": created_after, "limit": 100}

    r = requests.get(API_URL, params=params)
    data = r.json()

    # Filter artworks from the exhibition with at least 8 works
    exhibition_artworks = [artwork for artwork in data["data"]]
    if len(exhibition_artworks) < 8:
        print("The exhibition does not have enough artworks.")
        return

    # Choose the highlight artworks based on creation date greater than 1500
    highlight_artwork = None
    for artwork in exhibition_artworks:
        if artwork.get("creation_date_earliest"):
            if artwork["creation_date_earliest"] > 1500:
                highlight_artwork = artwork
                break

    return highlight_artwork


def find_related_artworks(exhibition_keyword, created_after):
    params = {"q": exhibition_keyword, "created_after": created_after, "limit": 5}

    r = requests.get(API_URL, params=params)
    data = r.json()

    return data["data"]


def insert_to_mongodb(collection, artwork):
    mini_exhibition_id = uuid4()
    # Create a document to insert into the collection
    document = {
        "athena_id": artwork["id"],
        "accession_number": artwork["accession_number"],
        "tombstone": artwork["tombstone"],
        "image": artwork["images"]["web"]["url"],
        "creation_date_earliest": artwork["creation_date_earliest"],
        "mini_exhibition_id": mini_exhibition_id,
    }

    # Insert the document into the collection
    collection.insert_one(document)
    print(f"Inserted: {artwork['tombstone']} with Unique ID: {mini_exhibition_id}")


if __name__ == "__main__":
    exhibition_keyword = "Animals in Japanese Art"
    created_after = 1500

    # Find the highlight artwork
    highlight_artwork = find_highlight_artwork(exhibition_keyword, created_after)
    # Find the related artworks
    related_artworks = find_related_artworks(exhibition_keyword, created_after)
    if related_artworks:
        for artwork in related_artworks:
            insert_to_mongodb(collection, artwork)
