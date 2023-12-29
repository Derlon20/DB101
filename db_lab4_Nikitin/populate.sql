INSERT INTO domains (domain_id, domain)
VALUES
(1, 'Strategy Games'),
(2, 'Thematic Games'),
(3, 'Wargames'),
(4, 'Family Games'),
(5, 'Customizable games'),
(6, 'Party Games'),
(7, 'Abstract Games');


INSERT INTO game (game_id, name, year, min_player, max_player, time, min_age, owned)
VALUES
(1, 'Gloomhaven', 2017, 1, 4, 120, 14, 68323),
(2, 'Machi Koro', 2012, 2, 4, 30, 10, 40930),
(3, 'Rallyman', 2009, 1, 4, 45, 9, 3034),
(4, 'Spot it!', 2009, 2, 8, 15, 7, 24326),
(5, 'Brass: birmingham', 2018, 2, 4, 120, 14, 28785);

INSERT INTO domain_of_game (game_id, domain_id)
VALUES
(1, 1),
(1, 2),
(2, 4),
(3, 4),
(3, 2),
(4, 6),
(5, 1);