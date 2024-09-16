select * 
from portfolioprojects.laligastats2019;



-- Trying to Get the player with most minutes per team--

WITH RankedPlayers AS (
    SELECT
        Team,
        Name,
        MAX(Minutes_played) OVER (PARTITION BY Team) AS MostMinutes,
        ROW_NUMBER() OVER (PARTITION BY Team ORDER BY Minutes_played DESC) AS PlayerRank
    FROM
        portfolioprojects.laligastats2019 
) 
SELECT
    Team,
    Name,
	MostMinutes
FROM
    RankedPlayers
where 
PlayerRank=1
order by 
MostMinutes desc;

	

