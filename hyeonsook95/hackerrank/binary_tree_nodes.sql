SELECT N, 
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN (SELECT COUNT(*)
             FROM BST AS CBST
             WHERE CBST.P = PBST.N) = 0 THEN 'Leaf'
        ELSE 'Inner'
    END
FROM BST AS PBST
ORDER BY N;