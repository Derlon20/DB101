-- 1.Вивести жанри тих ігор, в які можна грати самому
SELECT DISTINCT(d.domain)
FROM domains d
JOIN domain_of_game dog ON dog.domain_id = d.domain_id
JOIN game g ON g.game_id = dog.game_id
WHERE g.min_player = 1;

-- 2.Вивести найдавнішу гру з жанром 'Стратегія'
SELECT g.Name
FROM game g
JOIN domain_of_game dog ON g.Game_id = dog.Game_id
JOIN domains d ON dog.domain_id = d.domain_id
WHERE d.domain = 'Strategy Games'
ORDER BY g.Year
LIMIT 1;

-- 3. Вивести найдовший час серед ігор з більш ніж одним жанром
SELECT g.time
FROM game g
JOIN domain_of_game dog ON g.game_id = dog.game_id
GROUP BY g.game_id
HAVING COUNT(DISTINCT dog.domain_id) > 1
ORDER BY g.Time desc
LIMIT 1;
