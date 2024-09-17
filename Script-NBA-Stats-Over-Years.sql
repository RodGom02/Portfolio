-- Highest PPG player per team -- 
with HighestPPG as (
	select 
		player,
		team, 
		season,
		max(pts) over (partition by team) as MostPPG,
		row_number () over (partition by team order by pts desc) as PlayerRank
	from 
		portfolioprojects.nba_player_stats 
	where 
		Games > 65 
)
select 
	player,
	team,
	season,
	MostPPG
from 
	HighestPPG
where 
	PlayerRank=1
order by 
	MostPPG desc;

-- Player with the most FGA in every position-- 

with HighestFGA as (
	select 
		player, 
		season,
		pos,
		max(FGA) over (partition by pos) as MostFGA,
		row_number () over (partition by pos order by FGA desc) as PlayerRank
	from 
		portfolioprojects.nba_player_stats 
)
select 
	player,
	season,
	pos,
	MostFGA
from 
	HighestFGA
where 
	PlayerRank=1
order by 
	MostFGA desc 
limit 5;

-- Players with the Highest Free throws attempts per season-- 

with HighestFTA as (
	select 
		player, 
		team,
		season,
		max(FTA) over (partition by season) as MostFTA,
		row_number () over (partition by season order by (FTA) desc) as PlayerRank
	from 
		portfolioprojects.nba_player_stats 
)
select 
	player,
	team,
	season,
	MostFTA
from 
	HighestFTA
where 
	PlayerRank=1
order by 
	season desc;

-- Every year's highest Free Throw Attempted per game-- 

with points_per_year as (
	select 
		season,
		round(sum(PTS) over (partition by season),0) as Points_year
	from 
		portfolioprojects.nba_player_stats
)
select distinct 
	season, 
	Points_year
from 
	points_per_year
order by 
	season;



	
		

	
	