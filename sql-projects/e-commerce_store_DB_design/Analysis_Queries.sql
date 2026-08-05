-- Analysis Queries

-- Total Revenue 

select sum(amount) as total_revenue from payments;

-- Revenue by Product

select p.product_name,sum(oi.quantity * p.price) as revenue from order_items oi 
join products p on p.product_id = oi.product_id
join orders o on o.order_id = oi.order_id
where order_status = 'delivered'
group by p.product_name order by revenue desc;

-- Top Customers by Spend

SELECT c.name,
       SUM(p.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- Best Selling Products 

select p.product_name,sum(io.quantity) as best_selling from order_items io
join products p on p.product_id = io.product_id 
group by p.product_name order by best_selling desc;

-- Cancelled Orders Count

select count(*) from orders
where order_status = 'cancelled';