DROP PROCEDURE IF EXISTS insert_domain(char);
DROP FUNCTION IF EXISTS insert_domain(char); 

--Додати нові можливі жанри ігор (рядок у таблицю domains)

CREATE OR REPLACE PROCEDURE insert_domain(IN new_domain_id INT, IN new_domain CHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
IF EXISTS (SELECT 1 FROM domains WHERE domain_id = new_domain_id OR domain = new_domain) THEN
        RAISE EXCEPTION 'Wrong. Part of data already in table';
ELSE
    INSERT INTO domains (domain_id, domain)
    VALUES (new_domain_id, new_domain);
	END IF;

END;
$$;

CALL insert_domain(65, 'Economic Games');

select * from domains
