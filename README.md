# ☁️ CloudOrder - AWS Cloud E-Commerce Application

## 1. Project Overview

CloudOrder is a cloud-based e-commerce and order management application designed to demonstrate how a modern business application can be developed, containerized, secured, and deployed on Amazon Web Services (AWS).

Customers will be able to browse products, manage their shopping cart, and place orders through a modern web interface. The backend provides REST APIs for product and order management, while PostgreSQL is used for persistent data storage.

The project is being developed incrementally, starting with local application development and progressing toward a highly available and scalable AWS architecture.

---

## 2. Project Objective

The main objective of CloudOrder is to build and deploy a production-oriented cloud application while demonstrating practical AWS and DevOps concepts.

The project demonstrates:

- Frontend application development
- REST API development
- PostgreSQL database integration
- Docker containerization
- AWS cloud deployment
- IAM and security
- High availability
- Scalability
- Application monitoring
- Logging
- CI/CD automation
- AWS architecture design

---

## 3. Customer Features

Customers will be able to:

- Browse available products
- Search products
- Filter products by category
- Add products to a shopping cart
- Increase or decrease product quantities
- Remove products from the cart
- View cart subtotal, tax, shipping and total
- Proceed through a simulated checkout process
- View a successful payment confirmation
- Maintain cart data using browser local storage

### Planned Customer Features

- Customer registration
- Customer login
- Product details page
- Order placement through backend API
- Order history

---

## 4. Administrator Features

Administrators will be able to manage the product catalog.

### Implemented

- Add products through the backend API
- View products from PostgreSQL

### Planned

- Update products
- Delete products
- View customer orders
- Manage product inventory
- Administrator authentication

---

## 5. Technology Stack

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- Responsive UI
- Browser Local Storage

### Backend

- Python
- FastAPI
- REST APIs
- Uvicorn

### Database

- PostgreSQL

### Containerization

- Docker
- Docker Compose

### Version Control

- Git
- GitHub

### CI/CD

- GitHub Actions

### Cloud Platform

- Amazon Web Services (AWS)

---

## 6. Planned AWS Architecture

The target AWS architecture will use managed and scalable AWS services.

### Networking

- Amazon VPC
- Public and private subnets
- Internet Gateway
- NAT Gateway
- Security Groups

### Application

- Amazon ECS
- AWS Fargate
- Application Load Balancer
- Amazon ECR

### Database

- Amazon RDS for PostgreSQL
- Multi-AZ deployment where appropriate
- Automated backups

### Frontend

- Amazon S3
- Amazon CloudFront

### Security

- AWS IAM
- AWS Secrets Manager
- AWS KMS
- AWS WAF

### Monitoring

- Amazon CloudWatch
- CloudWatch Logs
- CloudWatch Alarms

### DNS

- Amazon Route 53

---

## 7. Target Architecture

The planned production architecture is:


                         USERS
                           |
                           v
                     Amazon Route 53
                           |
                           v
                     Amazon CloudFront
                           |
                    +------+------+
                    |             |
                    v             v
              Amazon S3      Application Load
               Frontend        Balancer
                                  |
                                  v
                         Amazon ECS / Fargate
                         +---------------+
                         |               |
                         v               v
                    Container 1     Container 2
                      FastAPI         FastAPI
                         |               |
                         +-------+-------+
                                 |
                                 v
                         Amazon RDS
                         PostgreSQL
