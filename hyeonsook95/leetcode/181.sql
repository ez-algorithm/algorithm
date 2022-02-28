SELECT e.name as Employee
FROM Employee as e
WHERE e.salary > (SELECT m.salary
                FROM Employee as m
                WHERE m.id = e.managerId  );