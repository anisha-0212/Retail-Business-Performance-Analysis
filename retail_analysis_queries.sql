-- 1. Total Sales and Profit
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales;


-- 2. Profit by Product Category
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales
GROUP BY Category
ORDER BY Total_Profit DESC;


-- 3. Sales by Region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY Region
ORDER BY Total_Sales DESC;


-- 4. Loss-making Sub-Categories
SELECT
    "Sub-Category",
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales
GROUP BY "Sub-Category"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit;


-- 5. Average Profit by Discount
SELECT
    Discount,
    ROUND(AVG(Profit), 2) AS Average_Profit
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;