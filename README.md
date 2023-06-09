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

Request Body
```
{
  "username": "user",
  "password": "password"
}
```

Response Body
```
{
	"currency_type": "Hryvnia",
	"id": 1,
	"password": "$pbkdf2-sha256$29000$7F3LGWPsndP6H2MMwVjr/Q$TMlIk/Bxgv7AK5ez7P1UdSo65W2syA8WACwM71dKXQE",
	"username": "user"
}
```

**POST /login** </br>
Authorize a user and obtain an access token for authentication.

Request Body
```
{
  "username": "user",
  "password": "password"
}
```

Response Body
```
{
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjMyMTM0OSwianRpIjoiMTQ3NzA0YjEtNTkyMC00ZWIwLTgwZTItNjdjMzhmYTM0NmM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg2MzIxMzQ5LCJleHAiOjE2ODYzMjIyNDl9.tVpIIcIvKnnU5sDowjVa76i9FW62MjoRc1xeCVJK3p0"
}
```

**GET /user** </br>
Get the list of all users.

Response Body
```
[
	{
		"currency_type": "Hryvnia",
		"id": 1,
		"password": "$pbkdf2-sha256$29000$HWPsfe99710rRSglREipFQ$9nMZ2/.ILqisUzgCSyxlKQvepfG2Tm9mnMJAXnxoXyY",
		"username": "user"
	},
	{
		"currency_type": "Hryvnia",
		"id": 2,
		"password": "$pbkdf2-sha256$29000$fq.1VipljDEm5JwzJmTMeQ$Uuz3tF3lOiYylwc26hXXI2RZ6GVEockPthEp4o.cJGw",
		"username": "user2"
	},
	{
		"currency_type": "Hryvnia",
		"id": 3,
		"password": "$pbkdf2-sha256$29000$g1AK4XwPQQjh/N.bMyYkxA$FkwEZTv.5KjN.GQf.8f4wJfikO5GdJj9SE5HdAhPw6Q",
		"username": "user3"
	}
]
```

**GET /user/{id}** </br>
Get a user by ID.

Response Body
```
{
	"currency_type": "Hryvnia",
	"id": 3,
	"password": "$pbkdf2-sha256$29000$g1AK4XwPQQjh/N.bMyYkxA$FkwEZTv.5KjN.GQf.8f4wJfikO5GdJj9SE5HdAhPw6Q",
	"username": "user3"
}
```

**DELETE /user/{id}** </br>
Delete a user.

Response Body
```
{
	"currency_type": "Hryvnia",
	"id": 3,
	"password": "$pbkdf2-sha256$29000$g1AK4XwPQQjh/N.bMyYkxA$FkwEZTv.5KjN.GQf.8f4wJfikO5GdJj9SE5HdAhPw6Q",
	"username": "user3"
}
```

**GET /category** </br>
Get the list of categories.

Response Body
```
[
	{
		"id": 1,
		"name": "Education"
	},
	{
		"id": 2,
		"name": "Traveling"
	},
	{
		"id": 3,
		"name": "Medicine"
	}
]
```

**GET /category/{id}** </br>
Get a category by ID.

Response Body
```
{
	"id": 1,
	"name": "Education"
}
```

**POST /category** </br>
Create a category.

```
{
    "name": "Medicine"
}
```

Response Body
```
{
	"id": 3,
	"name": "Medicine"
}
```

**DELETE /category/{id}** </br>
Delete a category by ID.

Response Body
```
{
	"id": 3,
	"name": "Medicine"
}
```

**GET /record/{id}** </br>
Get a record by user ID.

Response Body
```
[
	{
		"amount": "15",
		"category_id": 1,
		"currency_type": "Dollar",
		"date": "2023-06-09 14:40:59",
		"id": 1,
		"user_id": 1
	},
	{
		"amount": "10",
		"category_id": 2,
		"currency_type": "Euro",
		"date": "2023-06-09 14:41:45",
		"id": 2,
		"user_id": 1
	}
]
```

**GET /record/{userId}/{categoryId}** </br>
Get a record by user in a category.

Response Body
```
[
	{
		"amount": "15",
		"category_id": 1,
		"currency_type": "Dollar",
		"date": "2023-06-09 14:40:59",
		"id": 1,
		"user_id": 1
	}
]
```

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

Response Body
```
{
	"amount": "15",
	"category_id": 1,
	"currency_type": "Dollar",
	"date": "2023-06-09 14:40:59",
	"id": 1,
	"user_id": 1
}
```

**DELETE /record/{id}** </br>
Delete a record by ID.

Response Body
```
{
	"amount": "15",
	"category_id": 1,
	"currency_type": "Dollar",
	"date": "2023-06-09 14:40:59",
	"id": 1,
	"user_id": 1
}
```

**GET /currency** </br>
Get the list of currencies.

Response Body
```
[
	{
		"id": 1,
		"name": "Hryvnia"
	},
	{
		"id": 2,
		"name": "Dollar"
	},
	{
		"id": 3,
		"name": "Euro"
	}
]
```

**POST /currency** </br>
Create a currency. </br>

```
{
    "name": "Pound"
}
```

Response Body
```
{
	"id": 4,
	"name": "Pound"
}
```

### Technology Stack
Python with Flask, SQLAlchemy.