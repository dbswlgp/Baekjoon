-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A
INNER JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
WHERE INGREDIENT_TYPE = 'fruit_based' and TOTAL_ORDER > 3000
ORDER BY TOTAL_ORDER DESC