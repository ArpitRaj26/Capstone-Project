SELECT SUM(total_price) FROM orders;

SELECT customer_name, SUM(total_price)
FROM orders
GROUP BY customer_name;

SELECT product, SUM(quantity)
FROM orders
GROUP BY product;