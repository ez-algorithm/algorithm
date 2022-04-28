select sub.name as Employee
from Employee as sub
left join (select id, salary from Employee) as boss
on sub.managerId = boss.id
where sub.salary > boss.salary;
