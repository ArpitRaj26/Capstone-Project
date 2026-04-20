SELECT customer_id, SUM(quantity) AS total_orders FROM orders GROUP BY customer_id;


SELECT product, SUM(quantity) AS total_sold FROM orders GROUP BY product ORDER BY total_sold DESC;


SELECT product, SUM(quantity) AS total_sold FROM orders GROUP BY product ORDER BY total_sold DESC LIMIT 7;
