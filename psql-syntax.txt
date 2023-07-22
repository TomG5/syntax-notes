----    POSTGRES 12.8 / SQL SYNTAX   ----

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
CHAR(N)                     | Fixed length with space padding
VARCHAR(N)                  | Limited length without padding
TEXT                        | Unlimited length
SMALLINT                    | -32768 to 32767
INT                         | -2147483648 to 2147483647
BIGINT                      | Big integer numbers
FLOAT4/REAL                 | 6 decimals
FLOAT8/DOUBLE PRECISION     | 15 decimals
DECIMAL/NUMERIC             | Big decimal numbers
BOOLEAN                     | [true/false/null, 1/0/null, yes/no/null]
ARRAY                       | Set of elements of the same type          Ex.: INT[]
UUID                        | Unique universal identifier
DATE                        | Dates in 'yyyy-mm-dd'

---- Custom Data Type
CREATE DOMAIN Score SMALLINT CHECK (VALUE >=1 AND VALUE <= 5);                          | Conditional check for inputs
CREATE TYPE Account AS (id UUID, full_name VARCHAR(25), balance DECIMAL, score Score);  | General Syntax
CREATE TYPE "status" AS ENUM ('Open', 'Closed');                                        | Commom custom type

---- Constraints
NOT NULL        | ...
PRIMARY KEY     | ...
UNIQUE          | ...
CHECK           | Verify a condition
REFERENCES      | Foreign Key

---- Logical Operators (In order of precedence)
NOT / AND / OR

---- Comparison Operators
>
<
>=
<=
=
!= or <>

---- Casting (changing data type)
CAST(column AS type); 
column::type;

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
1) Aggregate    | Works with all the data in the column and generate a single result

AVG           | Calculate average of records  | AVG(values)
COUNT         | Count records                 | COUNT(values)
MIN           | Calculate minimum of records  | MIN(values) 
MAX           | Calculate maximum of records  | MAX(values)
SUM           | Calculate sum of records      | SUM(values)

2) Scalar       | Works with each separate row in the column and generate the respective result

RIGHT         | Get characters from the right             | RIGHT(string, number of chars)
LEFT          | Get characters from the left              | LEFT(string, number of chars)
LENGTH/LEN    | Get total length                          | LENGTH(string)
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
CREATE TEMPORARY TABLE disposabletable (id INT NOT NULL, newsalary FLOAT4 NOT NULL);                                    | Discarded at the end of the session
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
SELECT * FROM mytable WHERE first_name LIKE 'J%';           | (Anything starting with J)
SELECT * FROM mytable WHERE first_name NOT LIKE 'J%';       | (Anything not starting with J)
SELECT * FROM mytable WHERE first_name LIKE '[JKL]%';       | (Anything starting with J, K or L)
SELECT * FROM mytable WHERE first_name LIKE '[A-D]%';       | (Anything starting with A, B, C or D)
SELECT * FROM mytable WHERE first_name LIKE '[!A-D]%';      | (Anything not starting with A, B, C or D)
SELECT * FROM mytable WHERE first_name ILIKE 'J%';          | (Anything starting with J - Case insensitive)
SELECT * FROM mytable WHERE salary::text LIKE '_00000';     | (Anything ending with 00000)

    -- Generate different tables for use
WITH tb1 AS (SELECT...), tb2 AS (SELECT...) SELECT * FROM tb1 INNER JOIN tb2 ON tb1.x = tb2.x

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
SELECT * FROM mytable1 EXCEPT [ALL] SELECT * FROM mytable2;     | Union records exclusive to query1 

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
SELECT vendor, DENSE_RANK() OVER(ORDER BY sales DESC) AS "Rank" FROM mytable;   | Maintains natural sequence without skipping ranks even with ties

SELECT temp.number FROM (SELECT "number", LAG(number) OVER() AS "Last", LEAD(number) OVER() AS "Next", LEAD(number, 2) OVER() AS "Following Next" 
FROM mytable) AS temp WHERE temp."Last" = "number" AND temp."Next" = "number";

SELECT AVG(time) OVER(PARTITION BY racer ORDER BY race_date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) FROM mytable;
SELECT AVG(time) OVER(PARTITION BY racer ORDER BY race_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM mytable;

    -- Conditional statements
SELECT product, price CASE WHEN price > 100 THEN 'Sell' WHEN price BETWEEN 50 AND 100 THEN 'Hold' ELSE 'Buy' END FROM mytable;

    -- Check for NULL values
SELECT * FROM mytable WHERE last_name IS NULL;

    -- Ignore NULL values
SELECT * FROM mytable WHERE last_name IS NOT NULL;

    -- Substitute NULL values
SELECT COALESCE("name", 'No name provided') FROM mytable;

    -- Conditional NULL return
SELECT NULLIF(value1, value2);  | Null if value1 = value2 else returns value1

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

    -- Limit number of rows in output
SELECT id FROM mytable LIMIT 100;               | First 100 records
SELECT id FROM mytable LIMIT 100 OFFSET 10;     | First 100 records after the 10th record

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

---- Notes
/*
# "" is used for Table/Column and '' is used for strings
# The order for operations is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
# PostgreSQL uses ISO-8601 standard to define how to manipulate dates and times | YYYY-MM-DDTHH:MM:SS+TMZONE
# PostgreSQL is by default configured at UTC time zone and uses it to store the data received
*/