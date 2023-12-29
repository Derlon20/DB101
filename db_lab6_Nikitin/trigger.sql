DROP TRIGGER IF EXISTS upper_game_name ON Game;

--Назва гри додається у верхньому регістрі

CREATE OR REPLACE FUNCTION upper_game_name()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE game SET name = UPPER(name)
	WHERE game.name = NEW.name;
    RETURN NULL;
END;
$$;

CREATE TRIGGER upper_game_name
AFTER INSERT ON game
FOR EACH ROW EXECUTE FUNCTION upper_game_name();

INSERT INTO game (Game_id,Name,Year,Min_Player,Max_Player,Time,Min_Age,Owned) 
VALUES (89, 'draftosaurs',2019, 2,5,15,8,12045);

select * from game;