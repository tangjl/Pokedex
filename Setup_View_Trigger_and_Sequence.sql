CREATE TABLE Region
(
  Name VARCHAR(25) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE Type
(
  Name VARCHAR(10) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE User
(
  username VARCHAR(25) NOT NULL,
  Password VARCHAR(25) NOT NULL,
  PRIMARY KEY (username)
);

CREATE TABLE Weakness
(
  Type.Name VARCHAR(10) NOT NULL,
  WeakType.Name VARCHAR(10) NOT NULL,
  PRIMARY KEY (Type.Name, WeakType.Name),
  FOREIGN KEY (Type.Name) REFERENCES Type(Name),
  FOREIGN KEY (WeakType.Name) REFERENCES Type(Name)
);

CREATE TABLE Strength
(
  Type.Name VARCHAR(10) NOT NULL,
  WeakType.Name VARCHAR(10) NOT NULL,
  PRIMARY KEY (Type.Name, WeakType.Name),
  FOREIGN KEY (Type.Name) REFERENCES Type(Name),
  FOREIGN KEY (WeakType.Name) REFERENCES Type(Name)
);

CREATE TABLE Trainer
(
  Name VARCHAR(25) NOT NULL,
  numRegions INT NOT NULL,
  Region VARCHAR(25) NOT NULL,
  username VARCHAR(25) NOT NULL,
  PRIMARY KEY (username),
  FOREIGN KEY (Region) REFERENCES Region(Name),
  FOREIGN KEY (username) REFERENCES User(username)
);

CREATE TABLE Pokemon
(
  Number INT NOT NULL,
  Name VARCHAR(25) NOT NULL,
  Region VARCHAR(25) NOT NULL,
  Evolves_from INT NOT NULL,
  Evolves_into INT NOT NULL,
  PRIMARY KEY (Number),
  FOREIGN KEY (Region) REFERENCES Region(Name),
  FOREIGN KEY (Evolves_from) REFERENCES Pokemon(Number),
  FOREIGN KEY (Evolves_into) REFERENCES Pokemon(Number),
  UNIQUE (Name)
);

CREATE TABLE Stats
(
  HP INT NOT NULL,
  Attack INT NOT NULL,
  Defense INT NOT NULL,
  Special_Attack INT NOT NULL,
  Special_Defense INT NOT NULL,
  Speed INT NOT NULL,
  Pokemon.Number INT NOT NULL,
  PRIMARY KEY (Pokemon.Number),
  FOREIGN KEY (Pokemon.Number) REFERENCES Pokemon(Number)
);

CREATE TABLE PokeCollection
(
  username VARCHAR(25) NOT NULL,
  Number INT NOT NULL,
  PRIMARY KEY (username, Number),
  FOREIGN KEY (username) REFERENCES User(username),
  FOREIGN KEY (Number) REFERENCES Pokemon(Number)
);

CREATE TABLE PokemonType
(
  Pokemon.Number INT NOT NULL,
  Type.Type VARCHAR(10) NOT NULL,
  PRIMARY KEY (Pokemon.Number, Type.Type),
  FOREIGN KEY (Pokemon.Number) REFERENCES Pokemon(Number),
  FOREIGN KEY (Type.Type) REFERENCES Type(Name)
);
------------------------------
create view Kanto (number, name, region) as
select number, name, region_name
from Pokemon
where region = "Kanto"
with check option constraint pok_kanto;

create trigger Update_Stats
After Update on Stats
Referencing old row as old, new row as new
for each row
insert into Updated_Stats_Log
Values(New.HP-Old.HP, New.Attack-Old.Attack, New.Defense-Old.Defense, New.SpecialAttack-Old.SpecialAttack, New.SpecialDefense-Old.SpecialDefense, New.Speed-Old.Speed);

Create Sequence regionsTraveled
start with 1
increment by 1
maxvalue 6
cycle;
INSERT into Trainer("Gen", regionsTraveled.nextVal, "Kanto", "rohatgia");

