# Expense Tracking App
The Expense Tracking App is an application designed to enable users to effortlessly monitor their expenses. 
With this app, users can easily manage their finances by creating and deleting cost 
categories and expense records, as well as conducting searches for existing categories 
and expenses. Additionally, users have the flexibility to select their preferred currency
for recording their incurred expenses. To access the features offered by the app, users 
are required to authenticate. The  project was created for educational purposes. </br >

### Table Of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Technology Stack](#technology-stack)

### Installation
Clone the repository. </br>
```git clone https://github.com/lylich0/track-your-expenses.git``` 

Build the Docker image. </br>
```docker build -t app:latest .```

Run the Docker Container. </br>
```docker run -it app:latest```

### Usage
The program provides the user with the following options.  </br >
```
- Registering a user;
- Creating a cost category;
- Creating a record of expenses;
- Creating a currency and automatic assignment of it to the user;
- Obtainig a list of categories;
- Obtaining a list of records for a specific user;
- Obtaining a list of records in a category for a specific user;
- Obtaining a list of currencies.
```
### API Endpoints

**POST /user** </br>
Registr a new user in the system.

```
{
  "username": "user",
  "password": "password"
}
```

**POST /login** </br>
Authorize a user and obtain an access token for authentication.

```
{
  "username": "user",
  "password": "password"
}
```

**GET /user** </br>
Get the list of all users.

**GET /user/{id}** </br>
Get a user by ID.

**DELETE /user/{id}** </br>
Delete a user.

**GET /category** </br>
Get the list of categories.

**GET /category/{id}** </br>
Get a category by ID.

**POST /category** </br>
Create a category.

```
{
    "name": "Medicine"
}
```

**DELETE /category/{id}** </br>
Delete a category by ID.

**GET /record/{id}** </br>
Get a record by user ID.

**GET /record/{user_id}/{category_id}** </br>
Get a record by user in a category.

**POST /record** </br>
Create a record. </br>
The default currency is Hryvnia.

```
{
    "user_id": 1,
    "category_id": 1,
    "amount": "10",
    "currency_type": "Euro"
}
```

**DELETE /record/{id}** </br>
Delete a record by ID.

**GET /currency** </br>
Get the list of currencies.

**POST /currency** </br>
Create a currency. </br>

```
{
    "name": "Pound"
}
```

### Technology Stack
Python with Flask, SQLAlchemy.