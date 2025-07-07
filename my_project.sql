-- SELECT * FROM expense_manager.expenses where expense_date="2024-08-25"

SELECT * FROM expense_manager.expenses where expense_date="2024-08-01"

/*
SELECT  category, SUM(amount) as total
FROM  expenses 
WHERE expense_date
BETWEEN "2024-08-01" and "2024-08-05" 
GROUP BY category;
*/
