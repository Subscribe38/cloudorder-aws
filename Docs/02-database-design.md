# CloudOrder - Database Design

## 1. Database Technology

CloudOrder will use PostgreSQL as its relational database.

PostgreSQL was selected because the application contains structured and related data such as users, products, orders and order items.

## 2. Database Tables

### Users

Stores customer and administrator account information.

Fields:

- id - Primary Key
- name
- email
- password_hash
- role

### Products

Stores products available for purchase.

Fields:

- id - Primary Key
- name
- description
- price
- stock

### Orders

Stores customer order information.

Fields:

- id - Primary Key
- user_id - Foreign Key referencing Users
- total_amount
- status
- created_at

### Order_Items

Stores individual products included in each order.

Fields:

- id - Primary Key
- order_id - Foreign Key referencing Orders
- product_id - Foreign Key referencing Products
- quantity
- price

## 3. Relationships

- One user can create many orders.
- One order can contain many order items.
- One product can appear in many order items.

## 4. Database Design Objective

The database is designed to maintain structured relationships between users, products and orders while avoiding unnecessary duplication of data.
