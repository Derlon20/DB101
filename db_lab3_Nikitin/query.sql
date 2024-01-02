-- 1.Вивести жанри тих ігор, в які можна грати самому
select distinct(domain) from domains
join domain_of_game  on domain_of_game.domain_id = domains.domain_id
join game on game.game_id = domain_of_game.game_id
where game.min_player = 1;

-- 2.Вивести найдавнішу гру з жанром 'Стратегія'
select name from game 
join domain_of_game on game.game_id = domain_of_game.game_id
join domains on domain_of_game.domain_id = domains.domain_id
where domains.domain = 'Strategy Games'
order by game.year
limit 1;

-- 3. Вивести найдовший час серед ігор з більш ніж одним жанром
select time from game
join domain_of_game on game.game_id = domain_of_game.game_id
group by game.game_id
having count(distinct(domain_of_game.domain_id)) > 1
order by game.time desc
limit 1;
