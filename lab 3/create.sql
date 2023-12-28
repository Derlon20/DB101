CREATE TABLE Game
(
  Game_id INT NOT NULL,
  Name CHAR (100) NOT NULL,
  Year INT NOT NULL,
  Min_Player INT NOT NULL,
  Max_Player INT NOT NULL,
  Time INT NOT NULL,
  Min_Age INT NOT NULL,
  Owned INT NOT NULL,
  PRIMARY KEY (Game_id)
);

CREATE TABLE Domains
(
  domain_id INT NOT NULL,
  domain CHAR (50) NOT NULL,
  PRIMARY KEY (domain_id)
);

CREATE TABLE Domain_of_Game
(
  Game_id INT NOT NULL,
  domain_id INT NOT NULL,
  PRIMARY KEY (Game_id, domain_id),
  FOREIGN KEY (Game_id) REFERENCES Game(Game_id),
  FOREIGN KEY (domain_id) REFERENCES Domains(domain_id)
);
