CREATE DATABASE userDB;
USE userDB;

CREATE TABLE user (
    userID int,
    FirstName varchar(255),
    LastName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO user (userID, FirstName, LastName, Address,City)
VALUES 
(1,"John","Ken","Umoja","Nairobi"),
(2,"kelly","kundu","karen","Nairobi"),
(3,"Adam","sylvia","utawala","Nairobi"),
(4,"Laren","Bramwel","kangemi","Nairobi"),
(5,"Mark","shiko","lavington","Nairobi"),
(6,"Cain","Jevy","thika","Nairobi");

SELECT FirstName,Lastname, Address
FROM user
ORDER BY FirstName DESC;

