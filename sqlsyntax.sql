----    RBDMS / SQL SYNTAX   ----

-- Structure
1) Database

2) Schema

3) Table
3.1) Column/Attribute   | The collection of these is called Degree / The datatype limitation is called Constraint
3.2) Row/Tuple          | The collection of these is called Cardinality

-- Keys
Primary | Unique identifiers of records in a table

Foreign | Reference identifiers of primary keys from another table

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
1) Aggregate   | Work with all the data in the column and generate a single result
AVG()
COUNT()
MIN()
MAX()
SUM()

2) Scalar      | Work with each separate row in the column and generate the respective result

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
CAST(column AS type) 'or' column::type


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
SELECT * FROM mytable WHERE id IN (id1, id2, id4, id9)

    -- Filter records by pattern matching
SELECT * FROM mytable WHERE first_name LIKE 'J%';           | (Anything post J)
SELECT * FROM mytable WHERE first_name ILIKE 'J%';          | (Anything post J - Case insensitive)
SELECT * FROM mytable WHERE salary::text LIKE '_00000';     | (Any salary from 100000)

    -- Remove duplicates
SELECT DISTINCT profession FROM mytable;

    -- Concatenate columns or texts in a query
SELECT CONCAT(f_name, ' ',l_name) AS "Full Name";

    -- Order results
SELECT * FROM mytable ORDER BY first_name ASC, last_name DESC;

    -- Check for NULL values
SELECT * FROM mytable WHERE last_name IS NULL;

    -- Ignore NULL values
SELECT * FROM mytable WHERE last_name IS NOT NULL;

    -- Substitute NULL values
SELECT COALESCE(name, 'No name provided') FROM mytable;

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

-- Notes
/*
# "" is used for Table/Column and '' is used for strings
# PostgreSQL uses ISO-8601 standard to define how to manipulate dates and times | YYYY-MM-DDTHH:MM:SS+TMZONE
# PostgreSQL is by default configured at UTC time zone and uses it to store the data received

*/

