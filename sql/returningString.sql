-- Write a select statement that takes name from person table and return "Hello, <name> how are you doing today?" results in a column named greeting
--
-- [Make sure you type the exact thing I wrote or the program may not execute properly]


--person table has name data
Select Concat('Hello, ',name,' how are you doing today?') As greeting
From person
