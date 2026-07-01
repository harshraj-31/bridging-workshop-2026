/*====================================================
   ORDER MANAGEMENT SYSTEM
   SQL QUERIES ONLY
====================================================*/


-- 1. Display list of all customers

SELECT *
FROM Customer;


------------------------------------------------------

-- 2. Display list of all available product names

SELECT ProductName
FROM Product;


------------------------------------------------------

-- 3. Display total products purchased by each customer

SELECT
    c.CustomerName,
    SUM(o.Quantity) AS Total_Products
FROM Customer c
JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName;


------------------------------------------------------

-- 4. Display quantity of each product purchased by a
--    particular customer (Example: Rahul)

SELECT
    c.CustomerName,
    p.ProductName,
    o.Quantity
FROM Customer c
JOIN Orders o
ON c.CustomerID = o.CustomerID
JOIN Product p
ON o.ProductID = p.ProductID
WHERE c.CustomerName = 'Rahul';


------------------------------------------------------

-- 5. Customer Invoice

SELECT
    c.CustomerName,
    p.ProductName,
    p.Price,
    o.Quantity,
    o.TotalAmount,
    o.OrderDate
FROM Customer c
JOIN Orders o
ON c.CustomerID = o.CustomerID
JOIN Product p
ON o.ProductID = p.ProductID;


------------------------------------------------------

-- 6. Customers who purchased products worth more than ₹5000

SELECT
    c.CustomerName,
    o.TotalAmount
FROM Customer c
JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.TotalAmount > 5000;


------------------------------------------------------

-- 7. Generate Invoice for a Particular Customer
-- (Example: Rahul)

SELECT
    c.CustomerName,
    p.ProductName,
    p.Price,
    o.Quantity,
    o.TotalAmount,
    o.OrderDate
FROM Customer c
JOIN Orders o
ON c.CustomerID = o.CustomerID
JOIN Product p
ON o.ProductID = p.ProductID
WHERE c.CustomerName = 'Rahul';