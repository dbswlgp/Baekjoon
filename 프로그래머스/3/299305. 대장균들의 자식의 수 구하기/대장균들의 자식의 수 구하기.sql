SELECT PARENT.ID, COUNT(CHILD.PARENT_ID) AS CHILD_COUNT
FROM ECOLI_DATA PARENT
LEFT OUTER JOIN ECOLI_DATA CHILD
ON PARENT.ID = CHILD.PARENT_ID
GROUP BY PARENT.ID
ORDER BY PARENT.ID