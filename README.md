# Documentation

## Usage

Make sure you are running Python 3.10+ by running the following command:

```
py --version
```

### Install Dependencies

```
pip install pymongo
pip install requests
```

### MongoDB

Set up a data source in MongoDB Atlas. If you don’t have an account, you can sign up for a free one here: https://www.mongodb.com/cloud/atlas/register.

1. Make sure to copy the username and password to use in the database connection.
1. You can get the connection string during database creation, and replace `<YOUR_CONNECTION_STRING>` with it.
1. Replace `<YOUR_DATABASE_NAME>` with your database name.
1. Replace `<YOUR_COLLECTION_NAME>` with your collection name.

### Run the Python script

```
py cma.py
```

In the terminal you should see the 5 artworks inserted into the MongoDB, if you browse the collection online you will also see them.

# Questions

### How did you approach this problem and why you end up with the solution you did?

I approached the problem by breaking it down into smaller tasks and identifying the key requirements. Here's an overview of my approach:

1. Connect to MongoDB: I used the `pymongo` library to establish a connection to MongoDB using the provided connection string.
1. Define Constants: I defined constants for the MongoDB URI, database name, collection name, and the Open Access API URL.
1. Find Highlight Artwork: I implemented a function `find_highlight_artwork` that retrieves artworks from the Open Access API based on the exhibition keyword and the creation date criteria. It filters the artworks to find the highlight artwork that meets the specified criteria.
1. Find Related Artworks: I implemented a function `find_related_artworks` that retrieves related artworks from the Open Access API based on the exhibition keyword and the creation date criteria.
1. Insert to MongoDB: I implemented a function `insert_to_mongodb` that inserts an artwork document into the MongoDB collection. It generates a unique mini exhibition ID using `uuid4()` and constructs the document with the required fields.

### How long did it take you to complete?

Around 10 hours.

### How would you change your solution in order to scale it up to a web application where users can select an exhibition, highlight and similarity criteria, and receive results?

1. Set up a web application framework: Choose a web framework to handle the HTTP requests and responses.
1. Design the user interface: Create web pages or forms where users can select an exhibition, highlight and similarity criteria.
1. Handle user input: Extract the selected criteria from the user's input and use them to make requests to the Open Access API.
1. Process and display results: Receive the API responses and process the data to extract the highlight artwork and related artworks based on the specified criteria. Render the results on the web page for the user to view.
1. Incorporate database operations: Connect to the MongoDB database using the provided connection string. Perform insertions and retrievals based on the user's actions and the generated artwork data.
1. Enhance user experience: Implement features like pagination, filtering, sorting, and additional functionality based on the requirements of the web application.

### How would you set this up as a process that runs daily, with different results, and posts them to social media platforms via API?

1. Schedule the process: Use a task scheduling system like cron or a job scheduler library to schedule the script execution daily.
1. Generate random criteria: Modify the code to generate random exhibition keywords, highlight criteria, and similarity criteria each day.
1. Execute the script: Run the script with the generated criteria to find the highlight artwork and related artworks.
1. Use social media APIs: Integrate with the APIs of the desired social media platforms (e.g., Twitter, Facebook, Instagram) to post the results. You'll need to authenticate the application with the respective API, create the posts with the relevant artwork data, and schedule them to be posted.
1. Repeat the process: Set up the script execution as a recurring daily task, ensuring that it generates different criteria each day and posts the results to social media platforms.
