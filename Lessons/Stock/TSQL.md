
# Working with T-SQL

```sql
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(20),
    Address VARCHAR(255)
);
```

```sql
SELECT * FROM Customer
```

```sql
-- Inserting data into the Customer table
INSERT INTO Customer (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
VALUES
    (1, 'John', 'Doe', 'johndoe@email.com', '123-456-7890', '123 Main St'),
    (2, 'Jane', 'Smith', 'janesmith@email.com', '987-654-3210', '456 Elm St'),
    (3, 'Bob', 'Johnson', 'bobjohnson@email.com', '555-123-4567', '789 Oak Ave');
```

```sql
UPDATE Customer
SET PhoneNumber = '123-456-7899'
WHERE CustomerID = 1;
```

---

```sql
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT
);
```

```sql
-- Inserting data into the Product table
INSERT INTO Product (ProductID, ProductName, Category, Price, StockQuantity)
VALUES
    (1, 'Laptop', 'Electronics', 999.99, 50),
    (2, 'Smartphone', 'Electronics', 499.99, 100),
    (3, 'Desk Chair', 'Furniture', 149.99, 30),
    (4, 'Coffee Maker', 'Appliances', 39.99, 75),
    (5, 'Tennis Racket', 'Sports', 79.99, 20);

```

```sql
SELECT TOP 3 *
FROM Product;

```

---
```sql
CREATE TABLE [Order] (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    TotalAmount DECIMAL(10, 2),
    
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
```

```sql
-- Inserting sample transactions into the Order table
INSERT INTO [Order] (OrderID, CustomerID, ProductID, OrderDate, Quantity, TotalAmount)
VALUES
    (1, 1, 1, '2024-01-31', 2, 1999.98),
    (2, 2, 2, '2024-01-31', 3, 1499.97),
    (3, 1, 3, '2024-01-30', 1, 149.99),
    (4, 3, 4, '2024-01-30', 2, 79.98),
    (5, 2, 5, '2024-01-29', 1, 79.99),
    (6, 1, 1, '2024-01-29', 2, 1999.98),
    (7, 2, 2, '2024-01-28', 3, 1499.97),
    (8, 3, 3, '2024-01-27', 1, 149.99),
    (9, 2, 4, '2024-01-26', 2, 79.98),
    (10, 1, 5, '2024-01-25', 1, 79.99),
    (11, 3, 1, '2024-01-24', 2, 1999.98),
    (12, 3, 2, '2024-01-23', 3, 1499.97),
    (13, 2, 3, '2024-01-22', 1, 149.99),
    (14, 2, 4, '2024-01-21', 2, 79.98),
    (15, 1, 5, '2024-01-20', 1, 79.99);
```

```sql
SELECT *
FROM [Order];
```

---

```sql
SELECT
    C.CustomerID,
    C.FirstName,
    C.LastName,
    P.ProductName,
    O.Quantity,
    O.OrderDate
FROM
    Customer AS C
JOIN
    [Order] AS O ON C.CustomerID = O.CustomerID
JOIN
    Product AS P ON O.ProductID = P.ProductID;
```

```sql
SELECT
    C.CustomerID,
    C.FirstName,
    C.LastName,
    P.ProductName,
    O.Quantity,
    O.OrderDate
FROM
    Customer AS C
JOIN
    [Order] AS O ON C.CustomerID = O.CustomerID
JOIN
    Product AS P ON O.ProductID = P.ProductID
WHERE
    C.CustomerID = 1;
```

```sql
SELECT
    P.ProductID,
    P.ProductName,
    SUM(O.Quantity) AS TotalSold,
    SUM(O.TotalAmount) AS TotalRevenue
FROM
    Product AS P
LEFT JOIN
    [Order] AS O ON P.ProductID = O.ProductID
GROUP BY
    P.ProductID,
    P.ProductName
ORDER BY
    TotalRevenue DESC;
```

```sql
SELECT
    P.ProductID,
    P.ProductName,
    C.CustomerID,
    C.FirstName,
    C.LastName,
    O.Quantity,
    O.OrderDate,
    O.TotalAmount
FROM
    Product AS P
JOIN
    [Order] AS O ON P.ProductID = O.ProductID
JOIN
    Customer AS C ON O.CustomerID = C.CustomerID
WHERE
    P.ProductName = 'Laptop'
ORDER BY
    P.ProductID,
    O.OrderDate;

```

```sql
SELECT
    C.CustomerID,
    C.FirstName,
    C.LastName,
    SUM(O.Quantity) AS TotalQuantityPurchased,
    SUM(O.TotalAmount) AS TotalAmountSpent
FROM
    Customer AS C
JOIN
    [Order] AS O ON C.CustomerID = O.CustomerID
JOIN
    Product AS P ON O.ProductID = P.ProductID
WHERE
    P.ProductName = 'Laptop'
GROUP BY
    C.CustomerID,
    C.FirstName,
    C.LastName
ORDER BY
    C.CustomerID;
```

---
Bad
```sql
SELECT
    P.ProductID,
    P.ProductName,
    C.CustomerID,
    C.FirstName,
    C.LastName,
    O.Quantity,
    O.OrderDate,
    O.TotalAmount
FROM
    Product AS P
JOIN
    [Order] AS O ON P.ProductID = O.ProductID
JOIN
    Customer AS C ON O.CustomerID = C.CustomerID
WHERE
    P.ProductName = 'Laptop'
ORDER BY
    P.ProductID,
    O.OrderDate;

```

Optimmum
```sql
SELECT
    P.ProductID,
    P.ProductName,
    C.CustomerID,
    C.FirstName,
    C.LastName,
    O.Quantity,
    O.OrderDate,
    O.TotalAmount
FROM
    Product AS P
JOIN
    [Order] AS O ON P.ProductID = O.ProductID
JOIN
    Customer AS C ON O.CustomerID = C.CustomerID
WHERE
    P.ProductID IN (
        SELECT ProductID
        FROM Product
        WHERE ProductName = 'Laptop'
    )
ORDER BY
    P.ProductID,
    O.OrderDate;
    
```