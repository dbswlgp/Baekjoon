-- 코드를 입력하세요
-- 코드를 입력하세요
select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT from online_sale
where month(SALES_DATE) = 3
union all
select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT from offline_sale
where month(SALES_DATE) = 3
order by SALES_DATE,PRODUCT_ID,USER_ID