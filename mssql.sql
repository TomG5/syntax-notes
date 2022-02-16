----    SQL SERVER 2019 / SQL SYNTAX   ----

---- Structure
1) Database

2) Schema

3) Table
3.1) Column/Attribute   | The collection of these is called Degree
3.2) Row/Tuple          | The collection of these is called Cardinality

---- Uses
OLTP (Online Transactional Processing)  | Serves the daily operations dataflow

OLAP (Online Analytical Processing)     | Serves the data analysis for insights

---- Keys
Primary Key     | Column(s) with unique identifiers of records in a table

Foreign Key     | Column(s) referencing identifiers of primary keys from the same or another table

Super Key       | Combination of attributes to identify a record

Candidate Key   | Minimum combination of attributes necessary to reference a record

---- Data Types (Most commom)
CHAR(n)                     | Fixed length with space padding (n = size of bytes)
VARCHAR(n)                  | Limited length without padding (n = size of bytes)
TEXT                        | Unlimited length
SMALLINT                    | -32768 to 32767
INT                         | -2147483648 to 2147483647
BIGINT                      | Big integer numbers
FLOAT(n)/REAL               | 6 decimals (n = 1-24) / 15 decimals (n = 25-53) 
DECIMAL(p,s)/NUMERIC(p,s)   | Numbers with specified precision and scale
BIT                         | [1 / 0 / null]
ARRAY                       | Set of elements of the same type          Ex.: INT[]
DATE                        | Dates in 'yyyy-mm-dd'
DATETIME                    | Dates in 'yyyy-mm-dd hh:mm:ss'
TIME                        | Times in 'hh:mm:ss'

---- Custom Data Type
CREATE DOMAIN Score SMALLINT CHECK (VALUE >=1 AND VALUE <= 5);                          | Conditional check for inputs
CREATE TYPE Account AS (id UUID, full_name VARCHAR(25), balance DECIMAL, score Score);  | General Syntax
CREATE TYPE "status" AS ENUM ('Open', 'Closed');                                        | Commom custom type

---- Constraints
NOT NULL        | ...
PRIMARY KEY     | ...
FOREIGN KEY     | ...
UNIQUE          | ...
CHECK           | Verify a condition
DEFAULT         | Sets default value

---- Logical Operators (In order of precedence)
NOT / AND / OR

---- Comparison Operators
>
<
>=
<=
=
<> or !=
!> (not greater than)
!< (not smaller than)

---- Casting (changing data type)
CAST(column AS type);
CONVERT(column AS type);

---- Types of Commands
1) DCL (Data Control Language)
GRANT / REVOKE

2) DDL (Data Definition Language)
CREATE / ALTER / DROP / RENAME / TRUNCATE / COMMENT

3) DML (Data Modification Language)
INSERT / UPDATE / DELETE / MERGE / CALL / EXPLAIN PLAN / LOCK TABLE

4) DQL (Data Query Language)
SELECT

---- Types of Functions
1) Aggregate  | Works with all the data in the column and generate a single result (examples below)

AVG           | Calculate average of records  | AVG(values)
COUNT         | Count records                 | COUNT(values)
MIN           | Calculate minimum of records  | MIN(values) 
MAX           | Calculate maximum of records  | MAX(values)
SUM           | Calculate sum of records      | SUM(values)

2) Scalar     | Works with each separate row in the column and generate the respective result (examples below)

RIGHT         | Get characters from the right             | RIGHT(string, number of chars)
LEFT          | Get characters from the left              | LEFT(string, number of chars)
LEN           | Get total length                          | LEN(string)
RTRIM         | Remove spaces from the right              | RTRIM(string)
LTRIM         | Remove spaces from the left               | LTRIM(string)
REPLACE       | Replace string with another               | REPLACE(string, old part, new part)
REVERSE       | Reverse the order of a string             | REVERSE(string)
SUBSTRING     | Return part of a string                   | SUBSTRING(string, starting index, number of chars)
LOWER         | Transform string characters in lowercase  | LOWER(string)
UPPER         | Transform string characters in uppercase  | UPPER(string)

DAY           | Return the day of date      | DAY(date)
MONTH         | Return the month of date    | MONTH(date)
YEAR          | Return the year of date     | YEAR(date)

FLOOR         | Round value down            | FLOOR(value)
CEILING       | Round value up              | CEILING(value)
ROUND         | Round at decimal length     | ROUND(value, decimals)

    -- Role Attributes
LOGIN
SUPERUSER
CREATEDB
CREATEROLE
PASSWORD

---- Define an interval for operations
INTERVAL '1 year 4 months 2 weeks 3 days 5 hours 20 minutes';
INTERVAL '4 weeks ago';

---- Commom DCL Commands
    -- Grant privileges
GRANT ALL PRIVILEGES ON mytable TO thisuser;
GRANT ALL ON ALL TABLES IN SCHEMA myschema TO thisuser;
GRANT SELECT, INSERT, UPDATE ON mytable IN SCHEMA myschema TO thisuser;

    -- Revoke privileges
REVOKE ALL PRIVILEGES ON mytable FROM thisuser;
REVOKE ALL ON ALL TABLES IN SCHEMA myschema FROM thisuser;
REVOKE SELECT, INSERT, UPDATE ON mytable IN SCHEMA myschema FROM thisuser;

---- Commom DDL Commands
    -- Structural Commands
CREATE DATABASE mydb;
CREATE SCHEMA myschema;
CREATE TABLE mytable (id INT NOT NULL, "name" VARCHAR(32) PRIMARY KEY, active BOOLEAN REFERENCES othertable(active));
CREATE TABLE #temporary_table (id INT NOT NULL, newsalary FLOAT4 NOT NULL);                                            | Discarded at the end of the owner session
CREATE TABLE ##global_temporary_table (id INT NOT NULL, newsalary FLOAT4 NOT NULL);                                    | Discarded at the end of the owner session, available to all sessions until ended
CREATE ROLE myrole [LOGIN, CREATEDB etc.];
CREATE USER myuser WITH ENCRYPTED PASSWORD 'asdf';

    -- Define type of timestamp for field
CREATE TABLE mytable (col1 TIMESTAMP WITHOUT TIME ZONE, col2 TIMESTAMP WITH TIME ZONE);

    -- Change timezone
SET TIME ZONE '';                       | Session level change
ALTER USER postgres SET timezone = '';  | User level change

    -- Change tables
ALTER TABLE mytable ADD new_column UUID DEFAULT gen_random_uuid();  | Example using extension 'pgcrypto'
ALTER TABLE mytable ALTER my_column TYPE TEXT;
ALTER TABLE mytable ALTER my_column SET NOT NULL;
ALTER TABLE mytable RENAME old_name TO new_name;
ALTER TABLE mytable DROP new_column;

    -- Remove objects
DROP DATABASE mydb;
DROP SCHEMA myschema;
DROP TABLE mytable;

    -- Truncate table (Delete all records)
TRUNCATE TABLE mytable;

---- Commom DML Commands
    -- Insert data to table
INSERT INTO mytable (myname, age, salary, birth_day) VALUES ('Joe Doe', 32, 55000, '1990-01-01'::DATE), ('Jane Doe', 30, 56000, '1994-01-01'::DATE);

    -- Update data in table
UPDATE mytable SET begin_date = '2021-01-01'::DATE WHERE begin_date IS NULL;
UPDATE mytable SET target_region = CASE WHEN "state" = 'NY' THEN 1 ELSE 0 END;

    -- Delete data in table
DELETE FROM mytable WHERE begin_date IS NULL;

---- Commom DQL Commands
    -- Rename a column in a query
SELECT f_name AS "First Name" FROM mytable;

    -- Filter records
SELECT * FROM mytable WHERE (full_name = 'Joe Doe' AND age = 32) OR (full_name = 'Jane Doe' AND age = 30);
SELECT * FROM mytable WHERE (state = 'NY' OR state = 'NJ') AND gender = 'F';
SELECT * FROM mytable WHERE NOT salary <= 10000;

    -- Filter records by range (Inclusive)
SELECT * FROM mytable WHERE age BETWEEN 20 AND 50;
SELECT * FROM mytable WHERE country BETWEEN 'Argentina' AND 'Denmark';  | Alphabetic search

    -- Filter records by presence in a list/set
SELECT * FROM mytable WHERE id IN (id1, id2, id4, id9);
SELECT * FROM mytable WHERE id NOT IN (id1, id2, id4, id9);

    -- Filter records by pattern matching
SELECT * FROM mytable WHERE first_name LIKE 'J%';               | (Anything starting with J)
SELECT * FROM mytable WHERE first_name NOT LIKE 'J%';           | (Anything not starting with J)
SELECT * FROM mytable WHERE first_name LIKE '[JKL]%';           | (Anything starting with J, K or L)
SELECT * FROM mytable WHERE first_name LIKE '[A-D]%';           | (Anything starting with A, B, C or D)
SELECT * FROM mytable WHERE first_name LIKE '[^A-D]%';          | (Anything not starting with A, B, C or D)
SELECT * FROM mytable WHERE first_name LIKE '_ean';             | (Anything ending with 'ean')
SELECT * FROM mytable WHERE discount LIKE '15!%' ESCAPE '!';    | (Anything containing '15%' -> '!' is the escape character)

    -- Filter records by ample matching
SELECT products FROM mytable WHERE prodID = ANY (SELECT prodID FROM mytable2 WHERE sales > 10000);      |   Returns any matching records 
SELECT products FROM mytable WHERE prodID = ANY (SELECT prodID FROM mytable2 WHERE supplier = 'XYZ');   |   Returns if all records match

    -- Remove duplicates
SELECT DISTINCT profession FROM mytable;

    -- Concatenate columns
SELECT CONCAT(f_name, ' ',l_name) AS "Full Name";

    -- Order results
SELECT * FROM mytable ORDER BY first_name ASC, last_name DESC;

    -- Join columns from multiple tables
SELECT table1.name AS "Name", table2.salary AS "Salary" FROM table1 INNER JOIN table2 ON table1.name = table2.name ORDER BY table1.name;    | Inner Join
SELECT table1.name AS "Name", table2.salary AS "Salary" FROM table1 INNER JOIN table2 USING("name") ORDER BY table1.name;                   | Inner Join
SELECT A.id, A.name AS "Emp Name", B.manager AS "Manager" FROM table1 AS A, table1 AS B WHERE A.managerid = B.id;                           | Self Join
SELECT * FROM table1 AS A LEFT JOIN table2 AS B ON A.id = B.id;                                                                             | Left Join (Incl. intersection)
SELECT * FROM table1 AS A RIGHT JOIN table2 AS B ON A.id = B.id;                                                                            | Right Join (Incl. intersection)
SELECT * FROM table1 CROSS JOIN table2;                                                                                                     | Cross Join (Cartesian Product)
SELECT * FROM table1 AS A FULL JOIN table2 AS B ON A.id = B.id;                                                                             | Full Join

    -- Union records from multiple queries
SELECT * FROM mytable1 UNION SELECT * FROM mytable2;            | Union without duplicates
SELECT * FROM mytable1 UNION ALL SELECT * FROM mytable2;        | Union with duplicates
SELECT * FROM mytable1 INTERSECT [ALL] SELECT * FROM mytable2;  | Union records in commom
SELECT * FROM mytable1 EXCEPT [ALL] SELECT * FROM mytable2;     | Union records exclusive to table1 

    -- Group records by distinct values
SELECT department, COUNT(id) FROM mytable GROUP BY department;

    -- Filter groups
SELECT department, COUNT(id) FROM mytable GROUP BY department HAVING COUNT(id) > 1000;

    -- Filter by subgroups
SELECT	EXTRACT(YEAR FROM orderdate) AS "Year", EXTRACT(MONTH FROM orderdate) AS "Month", EXTRACT(DAY FROM orderdate) AS "Day", SUM(totalamount) AS "Total_Amount" FROM mytable

GROUP BY 
	ROLLUP (
		EXTRACT(YEAR FROM orderdate), 
		EXTRACT(MONTH FROM orderdate), 
		EXTRACT(DAY FROM orderdate)
		);

    -- Use Subqueries
SELECT * FROM mytable WHERE age > (SELECT AVG(age) FROM mytable2);

    -- Calculate values by partitions of records (Window Function)
SELECT department, emp, salary, AVG(salary) OVER (PARTITION BY department ORDER BY department) FROM mytable;
SELECT department, emp, salary, AVG(salary) OVER W1 FROM mytable WINDOW W1 AS (PARTITION BY department);
SELECT vendor, RANK() OVER(ORDER BY sales DESC) AS "Rank" FROM mytable;
SELECT id, vendor, ROW_NUMBER() OVER(ORDER BY id) AS "RN" FROM mytable;
SELECT vendor, DENSE_RANK() OVER(ORDER BY sales DESC) AS "Rank" FROM mytable;   | Maintains natural sequence without skipping ranks even with ties

SELECT temp.number FROM (SELECT "number", LAG(number) OVER() AS "Last", LEAD(number) OVER() AS "Next", LEAD(number, 2) OVER() AS "Following Next" 
FROM mytable) AS temp WHERE temp."Last" = "number" AND temp."Next" = "number";

SELECT AVG(time) OVER(PARTITION BY racer ORDER BY race_date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) FROM mytable;
SELECT AVG(time) OVER(PARTITION BY racer ORDER BY race_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM mytable;

    -- Conditional statements
SELECT product, price = CASE WHEN price > 100 THEN 'Sell' WHEN price BETWEEN 50 AND 100 THEN 'Hold' ELSE 'Buy' END FROM mytable;
SELECT CASE WHEN col1 < 123 THEN NULL ELSE col1 END AS col1, col2, col3 FROM mytable1, mytable2 WHERE col3 BETWEEN x AND y ORDER BY col2 DESC, col1, col3;

    -- Check if results exist in subquery
SELECT supplier FROM mytable WHERE EXISTS (SELECT ProductName FROM mytable2 WHERE mytable2.SupplierID = mytable.supplierID AND Price < 200);

    -- Check for NULL values
SELECT * FROM mytable WHERE last_name IS NULL;

    -- Ignore NULL values
SELECT * FROM mytable WHERE last_name IS NOT NULL;

    -- Substitute NULL values
SELECT ISNULL("name", 'No name provided') FROM mytable;

    -- Conditional NULL return
SELECT NULLIF(value1, value2);  | Null if value1 = value2 else returns value1

    -- Pivot rows in tables
SELECT [Doctor], [Professor], [Singer], [Actor] FROM (SELECT ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) num, [Name], [Occupation] FROM mytable) AS source
PIVOT (MAX([Name]) FOR [Occupation] IN ([Doctor],[Professor],[Singer],[Actor])) AS pv ORDER BY num;

    -- Check actual date and/or time
SELECT now();           | Date, time and time zone
SELECT now()::date;     | Just date
SELECT CURRENT_DATE;    | Just date

    -- Format date
SELECT TO_CHAR(mydate, 'dd/mm/yyyy');
SELECT date '2021-01-01';

    -- Calculate age of date
SELECT AGE(date '2021-01-01');                      | Difference between date and today
SELECT AGE(date '2021-01-01', date '2021-06-01');   | Difference between dates

    -- Extract component of date
SELECT EXTRACT(DAY FROM date '2021-01-01') AS DAY;
SELECT EXTRACT(MONTH FROM date '2021-01-01') AS MONTH;
SELECT EXTRACT(YEAR FROM date '2021-01-01') AS YEAR;

    -- Truncate date to lowest period
SELECT DATE_TRUNC('year', date '2021-06-11');   | Returns '2021-01-01'
SELECT DATE_TRUNC('month', date '2021-06-11');  | Returns '2021-06-01'
SELECT DATE_TRUNC('month', date '2021-06-11');  | Returns '2021-06-11' -- plus truncates the time if it's a timestamp

    -- Limit or jump number of rows in output
SELECT TOP 50 id FROM mytable;                                                              | First 50 records
SELECT TOP 10 PERCENT id FROM mytable;                                                      | First 10% of records
SELECT id, price FROM mytable ORDER BY price DESC OFFSET 1 ROWS;                            | Get 2th highest record
SELECT id, price FROM mytable ORDER BY price DESC OFFSET 1 ROWS FETCH NEXT 10 ROWS ONLY;    | Get 2th up to the 11th highest record

    -- Analyze execution
EXPLAIN ANALYZE SELECT * FROM mytable;

---- Indexing references

    -- Index algorithms
B-TREE  | Best for comparisons
HASH    | Best for equalities
GIN     | Best for arrays
GIST    | Best for geometric data and text

    -- Creating indexes
CREATE INDEX idx1 ON mytable ("name", "role", salary);
CREATE INDEX idx1 ON mytable (salary) WHERE salary > 50000;
CREATE INDEX idx1 ON mytable (salary) USING HASH;

    -- Deleting indexes
DROP INDEX idx1;

---- Types of views
1) Materialized         | Stores data resulted from a query in disk (copy) and memory for fast execution, needing manual update

CREATE MATERIALIZED VIEW myview AS SELECT * FROM mytable;
CREATE TEMPORARY VIEW myview AS SELECT * FROM mytable;          | Temporary view, dropped when the session is ended

    -- Rename view

ALTER MATERIALIZED VIEW myview RENAME TO myview2;

    -- Delete view

DROP MATERIALIZED VIEW myview;

2) Non-Materialized     | Re-runs query to generate and make available its results for another operation

CREATE VIEW myview AS SELECT * FROM mytable;
CREATE OR REPLACE myview AS SELECT id, product FROM mytable;

    -- Rename view

ALTER VIEW myview RENAME TO myview2;

    -- Delete view

DROP VIEW myview;

---- Variables
    -- Declare variable
DECLARE @myvar INT;

    -- Initialize the variable
SET @myvar = 0;

---- Loopings
DECLARE @iter INT = 20;
    
WHILE @iter > 1 BEGIN SELECT REPLICATE('ABC', @iter) SET @iter = @iter - 1 END;

---- Stored Procedures (pre-programmed code)
    -- Create procedures
CREATE PROCEDURE myprocedure AS SELECT * FROM mytable GO;
CREATE PROCEDURE myprocedure2 @fieldname VARCHAR(30) AS SELECT * FROM mytable WHERE fieldname = @fieldname GO;  |   Procedure with a parameter

    -- Execute procedures
EXEC myprocedure;
EXEC myprocedure2 @fieldname = 'Value';

---- Notes
/*
# "" is used for Table/Column and '' is used for strings
# The order for operations is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
# The Collation configuration contains the case sensitiveness of the database installation instance
# SQL Server is by default configured at UTC time zone and uses it to store the data received
*/