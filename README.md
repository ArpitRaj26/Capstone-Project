# Smart Data Pipeline for E-Commerce Analytics

## Project Overview

This project implements an end-to-end ETL pipeline using Python and MySQL. It processes raw CSV data, performs data cleaning, loads it into a database, and runs SQL queries to generate insights.

---

## Tech Stack

* Python
* Pandas, NumPy
* MySQL
* SQLAlchemy
* PyMySQL

---

## Project Structure

```
capstone-project/
│── orders.csv
│── clean_orders.csv
│── data_cleaning.py
│── load_data.py
│── analysis.sql
│── requirements.txt
│── README.md
```

---

## Setup and Execution

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Create Database

Run in MySQL:

```
CREATE DATABASE ecommerce;
```

### 3. Configure Connection

Update in `load_data.py`:

```
mysql+pymysql://root:password@localhost:3306/ecommerce
```

### 4. Run Pipeline

```
python data_cleaning.py
python load_data.py
```

### 5. Run SQL Analysis

Execute queries from `analysis.sql` in MySQL Workbench.

---

## Sample Queries

```
SELECT customer_id, SUM(quantity) AS total_orders FROM orders GROUP BY customer_id;

SELECT product, SUM(quantity) AS total_sold FROM orders GROUP BY product ORDER BY total_sold DESC;

SELECT product, SUM(quantity) AS total_sold FROM orders GROUP BY product ORDER BY total_sold DESC LIMIT 7;
```

---

## Output

* Customer-wise order summary
* Product performance
* Daily order trends

---

## Author

Arpit Raj
23053265
