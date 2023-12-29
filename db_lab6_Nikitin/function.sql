DROP Function IF EXISTS get_games_by_domain(varchar);

--Виведення ігор певного жанру

CREATE OR REPLACE FUNCTION get_games_by_domain(domain_name VARCHAR(50))
RETURNS TABLE (name CHAR(100)) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
        SELECT g.Name
        FROM Game g
        WHERE g.Game_id IN (SELECT Game_id FROM Domain_of_Game WHERE domain_id = (SELECT domain_id FROM Domains WHERE domain = domain_name));
END;
$$ ;

select * from get_games_by_domain('Party Games')

