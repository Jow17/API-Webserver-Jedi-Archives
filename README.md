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

Start PostgreSQL server with:
```sh
sudo service postgresql start
```
Create database:
```sh
create database jedi-archives
```
#### **Open second WSL command line and run the following commands:**

Create virtual environment:
```sh
python3 -m venv .venv
```
If virtual environment is not automatically activated run:
```sh
source .venv/bin/activate
```
Finally, run the following cli commands to set up and run Flask application:
```sh
pip install -r requirements.txt
flask run
flask db create
flask db seed
```
Open postman and use localhost:5555 as port 5555 is set as the default port in .flaskenv

---
### **R1 - Identification of the problem you are trying to solve by building this particular app.**

<p align="center"><em><b>A long time ago, in a galaxy far far away...</b><br></em>

![Star wars logo](docs/Star_Wars_Logo.svg.png)

*It is the year 22Bby and the galaxy is on a knife's edge amidst ongoing political turmoil. The prestigious Jedi Order and its 10,000 strong Jedi Knights, the keepers of the peace, are all that stands between the fragile Republic and all out war.*

*Jedi Master Obi-Wan Kenobi, while investigating a plot to assasinate Senator Amidala, has exposed some major flaws in the Jedi Archives as the planet Kamino had been inexplicably removed from the records! It was later discovered that the culprit was non other than former Jedi turned Sith Lord, Count Dooku, using the access codes of the missing Jedi Sifo Dyas.*

*To protect the archives from future breaches, the Jedi council has ordered a full reconstruction of the archives including an overhaul of it's database record systems. The council also requests that that all members of the order are assigned the appropriate level of access and are properly accounted for at all times...*

---

### **R2 - Why is it a problem that needs solving?**

![Archives meme](docs/archives_meme.jpg)

The Jedi archives is the largest repository of records in the known galaxy containing history and information spanning tens of thousands of years. Unfortunately, this also means that its systems are equally as old as the content is stores with numerous flaws that will need to be addressed. Thus the archives are in dire need of an overhaul for a more civilized age.

- **Lack of mobile accessibility:** Whilst the archives are stored in a secure location in the heart of the Jedi temple, this however means that any Jedi needing to access records would have to physically be in the archives. Due to how vast the galaxy has become, this would not only make reading the records difficult and time-consuming as Jedi would have to make long travel times back to Corusant, but updating the current information is also quite inefficient. As the political turmoil throughout the Republic systems has dramatically increased since the invasion of Naboo, Jedi are becoming more and more busy and their effectiveness in the field would be significantly improved if they has ample access to the wealth of knowledge of the archives from anywhere in the galaxy. 

- **Very few authentication/authorisation measures:** Dooku's sudden and unexpected betrayal of the order has raised significant concerns surrounding the archives security systems. As it currently stands, Jedi only need to provide an access code to read and manipulate records. This massive flaw was exploited by Dooku as he used a dead Jedi's codes to delete an entire planet without rousing suspicion. Dooku's actions show that the order has too much blind faith in their members loyalties. Whilst chief librarian Jocusta Nu has done exemplary work in maintaining the archives over her many years of service, security measures will need to be more robust. Proper authorization and authentication should be implemented for all members of the order to ensure that breaches like this do not occur in the future. 

---

### **R3 - Why have you chosen this database system. What are the drawbacks compared to others?**
![Yoda meme](docs/Yoda_meme.jpg)

Using a PostgreSQL database system would successfully address the issues listed in the previous section. It is open source and free ensuring that the Order does not have to expend extra resources or credits to maintain. Data inside a PostgresSQL database is also easily manipulated using the SQL and JSON querying languages. PostgreSQL is suited for large enterprises such as the Jedi Archives as it is highly scalable and provides management for large amounts of data as well as users. Being open source, PostgreSQL has a large community which contribute to its continuous development and improvement. Because of this it has a highly touted reputation which proceeds itself like a certain 4 armed cyborg. Furthermore, PostgreSQL feature rich support for extensions means that additional features functionality and data types can be supported. Thanks to its large community, PostgreSQL has a large library of tools that are supported across different operating systems. 

One of the main reasons for using PostgreSQL specifically is its support for both vertical and horizontal scalling, which means extra data can be added to tables with relative ease. Because the archives contain an almost infinite amount of data, records will take some time to transfer over, however PostgreSQL's scalability will make the process much more efficient.

However, PostgreSQL is not without its flaws when compared to other database types. For starters, Because PostgreSQL is a relational database, it reads records in a table sequentially, meaning that the larger a table becomes, the slower it is to query data. Non relational databases such as MongoDB are more effecient when dealing with high read and write workloads. Data in MongoDB is also de-normalised meaning joins between tables are quicker and less costly. Whilst these are significant advantages over PostgreSQL, PostgreSQL is still the more useful database system as it can deal with large amounts of data far better and can handle complex queries thanks to the SQL language and its sophisticated query optimizations. As the archives grows in scale and complexity, it is important that data can be modified accordingly. 

### **R4 - Identify and discuss the key functionalities and benefits of an ORM**

Whilst querying a database using SQL is an essential part of manipulating data, the process is often complicated and time-consuming. By utilizing a technique called Object Relational Mapping, developers can utlise object oriented programming to connect an oject in an object oriented programming language such as python to an SQL database without needing to query it. ORM's essentially convert the code in the compiled language and translates it and generates SQL code for a relational database such as PostgreSQL to perform the standard CRUD operations such as reading and creating. 

ORM's are extremely useful as they enable developers to use the progamming language of their choice to build implement the necessary parameters for interacting with a database. This essentially removes one of the major drawbacks of a database system like PostgresSQL having a steep learning curve and complex querying methods. Furthermore, developers can easilt switch between different database types without having to modify their current code as ORM's will automatically translate accordingly depending on the database being used. 

Visually, ORMs are easier to read and code as it uses classes that define attributes and business related models. These are called models which are mapped to relational database tables and enables developers to work directly with objects.

### **R5 - Document all endpoints for your API**

### **R6 - An ERD for your app**

![Archives ERD](docs/Jedi_Archives_ERD.JPG)

### **R7 - Detail any third party services that your app will use**

### **R8 - Describe your projects models in terms of the relationships they have with each other**

### **R9 - Discuss the database relations to be implemented in your application**

### **R10 - Describe the way tasks are allocated and tracked in your project**