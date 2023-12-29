select * from get_games_by_domain('Party Games');

CALL insert_domain(66, 'Role-play');
select * from domains;

INSERT INTO game (Game_id,Name,Year,Min_Player,Max_Player,Time,Min_Age,Owned) 
VALUES (95, 'cars',2006, 2,5,15,8,12045);

select * from game;