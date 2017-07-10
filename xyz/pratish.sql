--1:
 select count(*) from customers;

--2:
 select distinct city from customers;

--3: 
select  count(distinct state) from customers;

--4:
select customer_id,lower(first_name) as fname,upper(last_name) as lname
from customers
where customer_id>=80 and customer_id<=150

--5
select last_name,len(last_name)
from customers
	where len(last_name)>9

--6
select state,city,count(customer_id)
from customers
group by state,city
order by state,city

--7
select max(monthly_payment) as max,sector_id
from packages
group by sector_id

--8
select first_name,last_name,monthly_discount,
case 
					when monthly_discount>=0 and monthly_discount<=10 then 'A'
					when monthly_discount>=11 and monthly_discount<=20 then 'B'
					when monthly_discount>=21 and monthly_discount<=30 then 'C'
					else 'D'
end as b
from customers

--9
select first_name,birth_date,datediff(year,birth_date,'2017-01-01') as age
from customers
where datediff(year,birth_date,'2017-01-01')>50

--10
select * from customers
where datediff(day,join_date,'2007-01-01')>0

--11
select customer_id,first_name,state,city,pack_id
from customers
where pack_id not in (27,10,3)

--12
select first_name,join_date,monthly_discount,pack_id
from customers 
where last_name not like '%a%' and pack_id is not NULL
order by pack_id

--13
select * from customers
where (state like 'New York' and monthly_discount between 30 and 40) or (pack_id not in (8,19,30) and datediff(day,join_date,'2007-01-01')>0)

--14

select c.first_name,c.last_name,p.pack_id,p.speed
from customers c,packages p
where p.pack_id=c.pack_id

--15

select c.first_name,c.last_name,p.pack_id,p.speed
from customers c,packages p
where p.pack_id=c.pack_id and p.pack_id in (22,27)
order by c.last_name

--16

select last_name,first_name,monthly_discount from customers
where monthly_discount<(select monthly_discount from customers where customer_id=103)

--17
select last_name,first_name,join_date from customers
where join_date>(select join_date from customers where customer_id=540)


--18

select c.first_name,c.monthly_discount,p.pack_id,c.main_phone_num,c.secondary_phone_num
from customers c,packages p, sectors s
where c.pack_id=p.pack_id and p.sector_id=s.sector_id and s.sector_name like 'Business'

--19

 select pack_id,speed,strt_date
 from packages
 where datediff(year,strt_date,(select strt_date from packages where pack_id=7))=0



