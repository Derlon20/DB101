--1. Час кожної гри
SELECT g.name, g.time
FROM Game g
ORDER BY Time DESC;

--2. Розподіл ігор за жанрами
SELECT D.domain, COUNT(DG.Game_id) AS GameCount
FROM Domains D
LEFT JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
GROUP BY D.domain
ORDER BY GameCount DESC;

--3. Середній час ігор кожного жанру
SELECT D.domain, AVG(G.Time) AS AverageTime
FROM Domains D
JOIN Domain_of_Game DG ON D.domain_id = DG.domain_id
JOIN Game G ON DG.Game_id = G.Game_id
GROUP BY D.domain
ORDER BY AverageTime DESC;