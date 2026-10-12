# REST = principles for organizing that interface
# API = Is a way for one software to talk to another software(ingat seperti pelayan restoran)
# REST API = an API designed around REST principles

# CRUD --> C=Create, R=Read, U=Update, D=Delete
# CRUD are four basic operations in dataset,
# REST API use HTTP methods to implement CRUD:
# | CRUD  | Meaning | HTTP method     | Example                    |
# | ----- | ------- | --------------- | -------------------------- |
# | **C** | Create  | `POST`          | Add a new student          |
# | **R** | Read    | `GET`           | Get student information    |
# | **U** | Update  | `PUT` / `PATCH` | Change student information |
# | **D** | Delete  | `DELETE`        | Remove a student           |


# Entity in CRUD

# **Entity = jenis/objek data yang menjadi target untuk dilakukan CRUD.**

# In simple words:

# > **Entity = “WHAT data are we managing?”**  
# > **CRUD = “WHAT do we do with that data?”**

### Example: Notes App

# If we build a Notes application:

# Entity: Note

# A Note may have:
# id
# description
# status

# Example data:
# Note #1
# id = 1
# description = "Buy milk"
# status = "unfinished"

# We can perform CRUD on the **Note entity**:

# | CRUD       | Meaning          | Example          |
# |------------|------------------|------------------|
# | **Create** | Create new data  | Add a new Note   |
# | **Read**   | Read/view data   | View Note #1     |
# | **Update** | Change existing  | Change Note #1   |
# | **Delete** | Remove data      | Delete Note #1   |

# Another Example

# For a school system:

# Entity = Student

# CRUD:

# CREATE → Add a new student
# READ   → View student data
# UPDATE → Edit student data
# DELETE → Remove a student

# Easy way to remember
# ENTITY = WHAT?
# CRUD   = WHAT DO WE DO TO IT?


# Examples of entities:

# Notes App       → Note
# Online Shop     → Product
# School System   → Student
# Library System  → Book
# Bank System     → Account

# Important: An entity is not the CRUD operation itself. It is the type of data/object that the CRUD operations manage.