DO $$
 DECLARE
 counter int;
 BEGIN

     FOR counter IN 1..9
         LOOP
            INSERT INTO domains (domain_id, domain)
             VALUES (7+counter, 'New Type Number'||counter);
         END LOOP;
 END;
 $$;