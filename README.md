# T2A3 - API Webserver Project
## Jonathan Ow 

[Github Repository](https://github.com/Jow17/API-Webserver-Jedi-Archives)

## Table of Contents:
-  [Installation Instructions](#installation-instructions)
- [R1 - Identifying the problem](#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)
- [R2 - Justifying the problem](#r2---why-is-it-a-problem-that-needs-solving)
- [R3 - Database System Pros/Cons](#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)
- [R4 - ORM Functionalities and benefits](#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)
- [R5 - API Endpoints](#r5---document-all-endpoints-for-your-api)
- [R6 - Entity Relationship Diagram (ERD)](#r6---an-erd-for-your-app)
- [R7 - 3rd party services used](#r7---detail-any-third-party-services-that-your-app-will-use)
- [R8 - Project models and relationships](#r8---describe-your-projects-models-in-terms-of-the-relationships-they-have-with-each-other)
- [R9 - Database relations](#r9---discuss-the-database-relations-to-be-implemented-in-your-application)
- [R10 - Task allocation and tracking](#r10---describe-the-way-tasks-are-allocated-and-tracked-in-your-project)

---
### **Installation Instructions**

#### **Open WSL command line and run the following commands:**
1. Start PostgreSQL server with:
```sh
sudo service postgresql start
```
2. Create database
```sh
create database Jedi-Archives
```
#### **Open second WSL command line and run the following commands:**
3. Create virtual environment
```sh
python3 -m venv .venv
```
4. If virtual environment is not automatically activated run:
```sh
source .venv/bin/activate
```
5. Finally, run the following cli commands to set up and run Flask application:
```sh
pip install -r requirements.txt
flask run
flask db create
flask db seed
```
6. Open postman and use localhost:5555 as port 5555 is set as the default port in .flaskenv

---
### **R1 - Identification of the problem you are trying to solve by building this particular app.**

<p align="center"><em>A long time ago in a galaxy far far away...<br>

It is the year 22Bby and the galaxy is on a knife's edge amidst ongoing political turmoil. The prestigious Jedi Order and its 10,000 strong Jedi Knights, the keepers of the peace are all that stands between the fragile Republic and all out war. <br>

Jedi Master Obi-Kenobi while investigating a plot to assasinate Senator Amidala has exposed some major flaws in the Jedi Archives as the planet Kamino had been inexplicably removed from the records by the former Jedi turned Sith Lord, Count Dooku, using the access codes of the now deceased Jedi Sifo Diyas. <br>

![Visble Confusion](docs/visible_confusion.jpg)

To ensure breaches likes this do not occur in the future, the Jedi council has ordered a full reconstruction of the archives database and its security systems, as well as making sure all 10,000 members of the order are assigned the approproate level of access and are properly accounted for at all times...
</em>

### **R2 - Why is it a problem that needs solving?**


### **R3 - Why have you chosen this database system. What are the drawbacks compared to others?**

### **R4 - Identify and discuss the key functionalities and benefits of an ORM**

### **R5 - Document all endpoints for your API**

### **R6 - An ERD for your app**

### **R7 - Detail any third party services that your app will use**

### **R8 - Describe your projects models in terms of the relationships they have with each other**

### **R9 - Discuss the database relations to be implemented in your application**

### **R10 - Describe the way tasks are allocated and tracked in your project**