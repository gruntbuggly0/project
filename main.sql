CREATE TABLE Products(
pid INT AUTO_INCREMENT PRIMARY KEY,
product VARCHAR(255) NOT NULL,
category CHAR(5) NOT NULL,
price DECIMAL(10,2),
stock CHAR(12) NOT NULL,
expiry_date DATE);

Create table employees(
Name varchar(50) not null,
eID varchar(10) not null,
Passwd varchar(10) not null,
Age int(2) not null,
Salary int(10)not null,
Position varchar(20) not null,
Primary key(eID)); 

CREATE TABLE customer_data(
C_ID int primary key,
Firstname varchar(255) not null,
Lastname varchar(255) not null,
Email varchar(255) UNIQUE,
PhoneNo varchar(15),
MembershipType varchar(50),
last_purchase int(20),
dateoflastpurchase date);

 insert into customer_data (C_ID,Firstname,Lastname,Email,PhoneNo,MembershipType) values (1234,'Manoj','Kumar','mk1994@gmail.com','123456789','Premium');
 insert into Products (product,category,price,stock,expiry_date) values ('packing tape big','HOUSP',150.02,'in stock',NULL),('pack of 10 gel pens','HOUSP',100.50,'in stock',NULL);

insert into products values 
(1, "Apple", "FRTVE", 20.50, "in stock", "2025-03-15"),
(2, "Banana", "FRTVE", 5.50, "in stock", "2025-02-25"),
(3, "Carrot", "FRTVE", 8.00, "in stock", "2025-03-10"),
(4, "Broccoli", "FRTVE", 40.25, "in stock", "2025-04-01"),
(5, "Potato", "FRTVE", 7.00, "in stock", "2025-03-20"),
(6, "Chicken", "MTSFD", 350.00, "in stock", "2025-03-05"),
(7, "Sausage", "MTSFD", 25.50, "in stock", "2025-03-12"),
(8, "Egg", "MTSFD", 6.00, "in stock", "2025-04-10"),
(9, "Fish", "MTSFD", 75.00, "in stock", "2025-03-04"),
(10, "Crab", "MTSFD", 300.00, "in stock", "2025-03-11"),
(11, "Packing Tape", "HOUSP", 150.02, "in stock", NULL),
(12, "Gel Pens (Pack of 10)", "HOUSP", 100.50, "in stock", NULL),
(13, "Batteries", "HOUSP", 100.00, "in stock", NULL),
(14, "Iron Nails", "HOUSP", 50.50, "in stock", NULL),
(15, "Paper Towels", "HOUSP", 20.50, "in stock", NULL),
(16, "Toothpaste", "PCARE", 40.00, "in stock", NULL),
(17, "Hand Sanitizer", "PCARE", 30.00, "in stock", NULL),
(18, "Coconut Oil", "PCARE", 40.00, "in stock", NULL),
(19, "Sunscreen", "PCARE", 200.00, "in stock", NULL),
(20, "Deodorant", "PCARE", 100.00, "in stock", NULL),
(21, "Storage Container", "KTCHW", 100.00, "in stock", NULL),
(22, "Measuring Cups", "KTCHW", 50.00, "in stock", NULL),
(23, "Plastic Wrap", "KTCHW", 20.25, "in stock", NULL),
(24, "Dish Soap", "KTCHW", 50.00, "in stock", NULL),
(25, "Oven", "KTCHW", 5000.25, "in stock", NULL);
