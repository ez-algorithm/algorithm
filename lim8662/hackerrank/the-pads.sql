select CONCAT(name, '(', LEFT(occupation, 1) ,')') 
from occupations 
order by name;

select CONCAT('There are a total of ', count(*), ' ', LOWER(occupation),'s.') as result 
from occupations 
group by occupation
order by result;