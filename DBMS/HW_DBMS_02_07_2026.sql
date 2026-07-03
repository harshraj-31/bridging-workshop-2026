/*=========================================================
        CINESTAR MULTIPLEX DATABASE
        SQL TABLES + SAMPLE DATA + QUERIES

        Author : Harshrajsinh Zala
=========================================================*/


/*=========================================================
                    CREATE TABLES
=========================================================*/

-- Movie Table
CREATE TABLE Movie (
    movie_id INT PRIMARY KEY,
    title VARCHAR(50),
    genre VARCHAR(30),
    language VARCHAR(20),
    duration INT,
    release_date DATE
);

-- Screen Table
CREATE TABLE Screen (
    screen_id INT PRIMARY KEY,
    screen_name VARCHAR(20),
    capacity INT,
    screen_type VARCHAR(20)
);

-- Booking Table
CREATE TABLE Booking (
    booking_id INT PRIMARY KEY,
    screen_id INT,
    tickets_booked INT,
    total_amount DECIMAL(10,2),
    booking_date DATE
);


/*=========================================================
                    INSERT RECORDS
=========================================================*/

-- Movie Records
INSERT INTO Movie VALUES
(1,'Pushpa 2','Action','Hindi',180,'2024-12-05'),
(2,'Kalki 2898 AD','Sci-Fi','Hindi',175,'2024-06-27'),
(3,'Leo','Action','Tamil',165,'2023-10-19');

-- Screen Records
INSERT INTO Screen VALUES
(1,'Screen A',200,'2D'),
(2,'Screen B',150,'3D'),
(3,'Screen C',250,'Dolby');

-- Booking Records
INSERT INTO Booking VALUES
(101,1,50,12500,CURDATE()),
(102,2,40,10000,CURDATE()),
(103,3,60,18000,CURDATE());


/*=========================================================
                    DISPLAY TABLES
=========================================================*/

-- Display Movie Table
SELECT * FROM Movie;

-- Display Screen Table
SELECT * FROM Screen;

-- Display Booking Table
SELECT * FROM Booking;


/*=========================================================
                    REQUIRED QUERIES
=========================================================*/

-- 1. Look up any movie's details
SELECT title, genre, language, duration, release_date
FROM Movie
WHERE title = 'Pushpa 2';


-- 2. View every screen's capacity and type
SELECT screen_id, screen_name, capacity, screen_type
FROM Screen;


-- 3. Check seats left for a show
SELECT capacity - SUM(tickets_booked) AS seats_left
FROM Screen, Booking
WHERE Screen.screen_id = Booking.screen_id
GROUP BY capacity;


-- 4. Generate today's ticket revenue report
SELECT SUM(total_amount) AS today_revenue
FROM Booking
WHERE booking_date = CURDATE();