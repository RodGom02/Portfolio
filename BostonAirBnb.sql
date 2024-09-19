select *
from portfolioprojects.bostonlistings;

select Price, cast(replace(Price,'$','') as unsigned) as Price_clean
from portfolioprojects.bostonlistings;

-- Trying to get the top 20 AirBnB listings--

select 
	id,
	listing_url,
	name,
	30 - availability_30 as booked_out_30,
	cast(replace(Price,'$','') as unsigned) as price_clean,
	cast(replace(Price,'$','') as unsigned) * (30 - availability_30) as proj_rev_30
from 
	portfolioprojects.bostonlistings 
order by 
	proj_rev_30 desc
limit 20;
-- -- 

select * from portfolioprojects.bostonreviews
inner join portfolioprojects.bostonlistings on bostonreviews.listing_id = bostonlistings.id;

-- Finding the listings with most 'dirty' in the reviews-- 

select 
	host_id,
	host_url,
	host_name,
	count(*) as num_dirty_reviews
from 
	portfolioprojects.bostonreviews 
inner join 
	portfolioprojects.bostonlistings on bostonreviews.listing_id = bostonlistings.id
where 
	comments like '%dirty%'
group by 
	host_id,
	host_url,
	host_name
order by 
	num_dirty_reviews desc;
	