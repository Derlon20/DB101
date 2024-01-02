--1. Час кожної гри
select name, time from game
order by time desc;

--2. Розподіл ігор за жанрами
select domain, count(domain_of_game.Game_id) as GameCount
from Domains
left join domain_of_game on domains.domain_id = domain_of_game.domain_id
group by domains.domain
order by GameCount desc;

--3. Середній час ігор кожного жанру
select domain, avg(game.time) as AverageTime from domains 
join domain_of_game on domains.domain_id = domain_of_game.domain_id
join game on domain_of_game.game_id = game.game_id
group by domains.domain
order by AverageTime desc;
