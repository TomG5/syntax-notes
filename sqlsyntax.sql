----    RBDMS / SQL SYNTAX   ----

-- Structure
1) Database

2) Schema

3) Table
3.1) Column/Attribute   | The collection of these is called Degree / The datatype limitation is called Constraint
3.2) Row/Tuple          | The collection of these is called Cardinality

-- Keys
Primary | Unique identifiers of records in a table

Foreign | Reference identifiers of primary keys from another or same table

-- Uses
OLTP (Online Transactional Processing)  | Serves the daily operations dataflow

OLAP (Online Analytical Processing)     | Serves the data analysis for insights

-- Commom Commands
1) DCL (Data Control Language)
GRANT
REVOKE

2) DDL (Data Definition Language)
CREATE
ALTER
DROP
RENAME
TRUNCATE
COMMENT

3) DQL (Data Query Language)
SELECT

4) DML (Data Modification Language)
INSERT
UPDATE
DELETE
MERGE
CALL
EXPLAIN PLAN
LOCK TABLE

-- Types of Functions
1) Aggregate    | Works with all the data in the column and generate a single result

AVG()           | Calculate average of records  | AVG(values)
COUNT()         | Count records                 | COUNT(values)
MIN()           | Calculate minimum of records  | MIN(values) 
MAX()           | Calculate maximum of records  | MAX(values)
SUM()           | Calculate sum of records      | SUM(values)

2) Scalar       | Works with each separate row in the column and generate the respective result

RIGHT()         | Get characters from the right             | RIGHT(string, number of chars)
LEFT()          | Get characters from the left              | LEFT(string, number of chars)
LEN()           | Get total length                          | LEN(string)
RTRIM()         | Remove spaces from the right              | RTRIM(string)
LTRIM()         | Remove spaces from the left               | LTRIM(string)
REPLACE()       | Replace string with another               | REPLACE(string, old part, new part)
REVERSE()       | Reverse the order of a string             | REVERSE(string)
SUBSTRING()     | Return part of a string                   | SUBSTRING(string, starting index, number of chars)
LOWER()         | Transform string characters in lowercase  | LOWER(string)
UPPER()         | Transform string characters in uppercase  | UPPER(string)

DATEADD()       | Add a period to a date        | DATEADD(time unit, quantity, date)
DATEDIFF()      | Return difference of dates    | DATEDIFF(time unit, date1, date2)
DAY()           | Return the day of date        | DAY(date)
MONTH()         | Return the month of date      | MONTH(date)
YEAR()          | Return the year of date       | YEAR(date)
GETDATE()       | Return the current date       | GETDATE()

FLOOR()         | Round value down              | FLOOR(value)
CEILING()       | Round value up                | CEILING(value)
ROUND()         | Round at decimal length       | ROUND(value, decimals)

-- Logical Operators (In order of precedence)
NOT
AND
OR

-- Comparison Operators
>
<
>=
<=
=
!= OR <>

-- Casting
CAST(column AS type); 
column::type;

-- Commom Functions and Operations
    -- Rename a column in a query
SELECT f_name AS "First Name" FROM mytable;

    -- Filter records
SELECT * FROM mytable WHERE full_name = 'Joe Doe' AND age = 32 OR full_name = 'Jane Doe' AND age = 30;
SELECT * FROM mytable WHERE (state = 'NY' OR state = 'NJ') AND gender = 'F';
SELECT * FROM mytable WHERE NOT salary <= 10000;

    -- Filter records by range (Inclusive)
SELECT * FROM mytable WHERE age BETWEEN 20 AND 50;

    -- Filter records by presence in a list/set
SELECT * FROM mytable WHERE id IN (id1, id2, id4, id9);
SELECT * FROM mytable WHERE id NOT IN (id1, id2, id4, id9);

    -- Filter records by pattern matching
SELECT * FROM mytable WHERE first_name LIKE 'J%';           | (Anything post J)
SELECT * FROM mytable WHERE first_name ILIKE 'J%';          | (Anything post J - Case insensitive)
SELECT * FROM mytable WHERE salary::text LIKE '_00000';     | (Any salary from 100000)

    -- Remove duplicates
SELECT DISTINCT profession FROM mytable;

    -- Concatenate columns
SELECT CONCAT(f_name, ' ',l_name) AS "Full Name";

    -- Order results
SELECT * FROM mytable ORDER BY first_name ASC, last_name DESC;

    -- Join columns from multiple tables
SELECT table1.name AS "Name", table2.salary AS "Salary" FROM table1 INNER JOIN table2 ON table1.name = table2.name ORDER BY table1.name;    | Inner Join
SELECT table1.name AS "Name", table2.salary AS "Salary" FROM table1 INNER JOIN table2 USING(name) ORDER BY table1.name;                     | Inner Join
SELECT A.id, A.name AS "Emp Name", B.manager AS "Manager" FROM table1 AS A, table1 AS B WHERE A.managerid = B.id;                           | Self Join
SELECT * FROM table1 AS A LEFT JOIN table2 AS B ON A.id = B.id;                                                                             | Left Join
SELECT * FROM table1 AS A RIGHT JOIN table2 AS B ON A.id = B.id;                                                                            | Right Join
SELECT * FROM table1 CROSS JOIN table2;                                                                                                     | Cross Join (Cartesian Product)
SELECT * FROM table1 AS A FULL JOIN table2 AS B ON A.id = B.id;                                                                             | Full Join

    -- Group records by distinct values
SELECT department, COUNT(id) FROM mytable GROUP BY department;

    -- Filter groups
SELECT department, COUNT(id) FROM mytable GROUP BY department HAVING COUNT(id) > 1000;

    -- Filter by subgroups
SELECT	EXTRACT(YEAR FROM orderdate) AS Year, EXTRACT(MONTH FROM orderdate) AS Month, EXTRACT(DAY FROM orderdate) AS Day, SUM(totalamount) AS totalamount FROM mytable

GROUP BY 
	ROLLUP (
		EXTRACT(YEAR FROM orderdate), 
		EXTRACT(MONTH FROM orderdate), 
		EXTRACT(DAY FROM orderdate)
		);

    -- Use Subqueries
SELECT * FROM mytable WHERE age > (SELECT AVG(age) FROM mytable2);

    -- Calculate values by partitions of records (Window Function)
SELECT department, emp, salary, AVG(salary) OVER (PARTITION BY department) FROM mytable;
SELECT department, emp, salary, AVG(salary) OVER W1 FROM mytable WINDOW W1 AS (PARTITION BY department);

    -- Conditional statements
SELECT product, price CASE WHEN price > 100 THEN 'Sell' WHEN price BETWEEN 50 AND 100 THEN 'Hold' ELSE 'Buy' END FROM mytable;

    -- Check for NULL values
SELECT * FROM mytable WHERE last_name IS NULL;

    -- Ignore NULL values
SELECT * FROM mytable WHERE last_name IS NOT NULL;

    -- Substitute NULL values
SELECT COALESCE(name, 'No name provided') FROM mytable;

    -- Conditional NULL return
SELECT NULLIF(value1, value2);  | NULL if value1 = value2 else returns value1

    -- Check actual date and/or time
SELECT now();           | Date, time and time zone
SELECT now()::date;     | Just date
SELECT CURRENT_DATE;    | Just date

    -- Format date
SELECT TO_CHAR(mydate, 'dd/mm/yyyy');
SELECT date '2021-01-01';

    -- Change timezone
SET TIME ZONE '';                       | Alteração a nível de sessão
ALTER USER postgres SET timezone = '';  | Alteração a nível de usuário

    -- Types of timestamps for fields
CREATE TABLE mytable (col1 TIMESTAMP WITHOUT TIME ZONE, col2 TIMESTAMP WITH TIME ZONE);

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

    -- Define an interval for operations
INTERVAL '1 year 4 months 2 weeks 3 days 5 hours 20 minutes';
INTERVAL '4 weeks ago';

    -- Limit number of rows in output
SELECT id FROM mytable LIMIT 100;   | 100 first records

    -- Analyze execution
EXPLAIN ANALYZE SELECT * FROM mytable;

-- Indexing references

    -- Index algorithms
B-TREE  | Best for comparisons
HASH    | Best for equalities
GIN     | Best for arrays
GIST    | Best for geometric data and text

    -- Creating indexes
CREATE INDEX idx1 ON mytable (name, role, salary);
CREATE INDEX idx1 ON mytable (salary) WHERE salary > 50000;
CREATE INDEX idx1 ON mytable (salary) USING HASH;

    -- Deleting indexes
DROP INDEX idx1;

-- Types of views
1) Materialized         | Stores data resulted from a query and keep it updated when main tables change

CREATE VIEW myview AS SELECT * FROM mytable;
CREATE OR REPLACE myview AS SELECT id, product FROM mytable;

    -- Rename view

ALTER VIEW myview RENAME TO myview2;

    -- Delete view

DROP VIEW myview;

2) Non-Materialized     | Re-run query to generate and make available its results for another operation

-- Notes
/*
# "" is used for Table/Column and '' is used for strings
# The order for operations is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER
# PostgreSQL uses ISO-8601 standard to define how to manipulate dates and times | YYYY-MM-DDTHH:MM:SS+TMZONE
# PostgreSQL is by default configured at UTC time zone and uses it to store the data received

*/