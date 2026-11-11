# Python Lectures
##### pythonLec1.py
- input output
- variables
- data types
- operators
##### pythonLec2.py
- strings : stores a sequence of characters
- conditional statements
##### pythonLec3.py
- Lists : stores elements of different types
- Tuples
##### pythonLec4.py
- Dictionary : stores data values in key:value pair
- Sets : collection of unordered unique values
##### pythonLec5.py
- Loops : used for repeat instructions
##### pythonLec6.py
- Functions : block of statements that perform a specific task
- Recursion : when a function calls itself
##### pythonLec7.py
- File I/O : used to perform operations on a file (read/write)
    - text files : .txt, .docx, .log etc
    - binary files : .mp4, .mov, .png, jpeg etc
    - Modes:
        - r: reading (default)
        - w: writing,truncating the file first (overwrite all file)
        - x: create new file and open for writing
        - a: open for writing,appending to the end of the file if exists
        - b: binary mode
        - t: text mode (default)
        - +: open a disk file for updating (reading & writing)
##### pythonLec8.py and pythonLec9.py
- OOP : using objects to map with real world problems
    - Class : blueprint for creating object
    - Objects : instances of class
    - 4 pillars : Abstraction,Encapsulation,Inheritance,Polymorphism
        - Abstraction : Hiding the implementation details of class and only showing the essential features to the users.
        - Encapsulation : Wrapping data and functions into a single unit (object)
        - Inheritance : When one class(child) inherits the properties and methods of another class(parent)
        - Polymorphism : operator overloading (When the same operator is allowed to have diff meaning)
# MongoDB
- NoSQL document database
- Databases contain collections, and collections contain documents
- CRUD operations : Create, Read, Update, Delete
- Queries : find and filter documents
- Indexes : improve query performance
# PyMongo
- `main.py`: verifies the MongoDB connection and reads records from `ecommerce.sales`
- Python driver for connecting to and working with MongoDB
- `1_Create_db_collection.py`: connects to the local MongoDB server, drops the `store` database, and inserts sample books into the `books` collection
- `2_Read.py`: reads all books and demonstrates filtering by title, author, year range, and projection
- `3_Update.py`: demonstrates single and multiple document updates, adding an array value, and assigning sequential `record_id` values
- `4_Delete.py`: demonstrates deleting one matching book and deleting books by year
