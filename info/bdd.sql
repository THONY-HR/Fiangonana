CREATE DATABASE fiangonana;
\c fiangonana;

CREATE TABLE Olona(
    idOlona SERIAL PRIMARY KEY,
    nomOlona VARCHAR(50),
    anneeDeNaissance DATE,
    idStatut INT
);


CREATE TABLE Statut(
    idStatut SERIAL PRIMARY KEY,
    nomStatut VARCHAR(50)
);

CREATE TABLE Rakitra(
    idRakitra SERIAL PRIMARY KEY,
    volaRakitra double precision,
    dateRakitra Date
);

CREATE TABLE Trosa(
    idTrosa SERIAL PRIMARY KEY,
    idOlona int,
    volaTrosa double precision,
    dateTrosa Date
);

CREATE OR REPLACE VIEW fiangonanaVola AS
SELECT COALESCE(SUM(Rakitra.volaRakitra), 0) as volaFiangonana
FROM Rakitra;

CREATE OR REPLACE VIEW fiangonanaTrosa AS
SELECT COALESCE(SUM(Trosa.volaTrosa), 0) as trosa
FROM Trosa;

CREATE OR REPLACE VIEW fiangonanaResteVola AS
SELECT fiangonanaVola.volaFiangonana - fiangonanaTrosa.trosa AS resteVolaFiangonana
FROM fiangonanaVola
CROSS JOIN fiangonanaTrosa;

SELECT 
    EXTRACT(YEAR FROM dateRakitra) AS Annee, 
    AVG(volaRakitra) AS Moyenne_Vola
FROM 
    Rakitra
WHERE 
    dateRakitra < '2024-03-15'
GROUP BY 
    EXTRACT(YEAR FROM dateRakitra);

CREATE VIEW infOlona AS
SELECT Olona.idOlona, Olona.idStatut, Trosa.idTrosa, Olona.nomOlona, Olona.anneeDeNaissance, Trosa.volaTrosa, Trosa.dateTrosa 
FROM Olona
JOIN Trosa ON Olona.idOlona = Trosa.idOlona
ORDER BY Olona.idStatut;

CREATE OR REPLACE VIEW moyenne_vola_par_lahady AS
SELECT
    EXTRACT(year FROM dateRakitra) AS annee,
    AVG(volaRakitra) AS moyenneVolaLahady
FROM Rakitra
GROUP BY
    EXTRACT(year FROM dateRakitra)
ORDER BY
    EXTRACT(year FROM dateRakitra) DESC;
    

INSERT INTO Olona (nomOlona, anneeDeNaissance, idStatut) VALUES
    ('Olona1', '1990-05-12', 1),
    ('Olona2', '1987-09-25', 1),
    ('Olona3', '1995-03-18', 1),
    ('Olona4', '1988-11-30', 1),
    ('Olona5', '1992-07-08', 1),
    ('Olona6', '1998-02-14', 1),
    ('Olona7', '1985-04-23', 1),
    ('Olona8', '1991-10-06', 1),
    ('Olona9', '1989-12-19', 1),
    ('Olona10', '1997-08-02', 1);

INSERT INTO Olona (nomOlona, anneeDeNaissance, idStatut) VALUES
    ('Olona11', '1994-06-12', 2),
    ('Olona12', '1999-09-25', 2),
    ('Olona13', '2001-03-18', 2),
    ('Olona14', '1992-11-30', 2),
    ('Olona15', '1996-07-08', 2);

INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1785347,'2022-01-02');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2493554,'2022-01-09');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1943028,'2022-01-16');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1224778,'2022-01-23');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2123103,'2022-01-30');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(863170,'2022-02-06');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1456140,'2022-02-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1750274,'2022-02-20');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1868880,'2022-02-27');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1680000,'2022-03-06');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1443484,'2022-03-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1251760,'2022-03-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2240582,'2022-03-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1383943,'2022-04-03');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2482869,'2022-04-10');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1635536,'2022-04-17');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1408553,'2022-04-24');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2136155,'2022-05-01');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1288352,'2022-05-08');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1288998,'2022-05-15');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(966183,'2022-05-22');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1915968,'2022-05-29');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1181604,'2022-06-05');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1172188,'2022-06-12');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(974678,'2022-06-19');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2116528,'2022-06-26');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(963836,'2022-07-03');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1948753,'2022-07-10');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1740897,'2022-07-17');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1980008,'2022-07-24');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1000336,'2022-07-31');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1575679,'2022-08-07');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(831672,'2022-08-14');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1509647,'2022-08-21');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1063296,'2022-08-28');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1258767,'2022-09-04');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1175881,'2022-09-11');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2085613,'2022-09-18');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2265460,'2022-09-25');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1146522,'2022-10-02');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1256339,'2022-10-09');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2288269,'2022-10-16');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2057056,'2022-10-23');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2278999,'2022-10-30');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1547634,'2022-11-06');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2052875,'2022-11-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2351552,'2022-11-20');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2330102,'2022-11-27');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1313146,'2022-12-04');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1028230,'2022-12-11');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2091938,'2022-12-18');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1981938,'2022-12-25');

delete from Rakitra where extract(year from dateRakitra)=2023;

INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1034717,'2023-01-01');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2088480,'2023-01-08');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2268591,'2023-01-15');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2248062,'2023-01-22');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1511873,'2023-01-29');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1252042,'2023-02-05');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1052193,'2023-02-12');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1618762,'2023-02-19');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1333933,'2023-02-26');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1894582,'2023-03-05');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1610751,'2023-03-12');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2036055,'2023-03-19');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(898038,'2023-03-26');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1203923,'2023-04-02');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1538451,'2023-04-09');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1018612,'2023-04-16');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1318840,'2023-04-23');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2014014,'2023-04-30');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1635913,'2023-05-07');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1047601,'2023-05-14');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1651479,'2023-05-21');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2272309,'2023-05-28');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1246328,'2023-06-04');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(893238,'2023-06-11');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1928502,'2023-06-18');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1840343,'2023-06-25');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(970042,'2023-07-02');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1908845,'2023-07-09');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2393482,'2023-07-16');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2100838,'2023-07-23');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2251352,'2023-07-30');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1944293,'2023-08-06');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1999351,'2023-08-13');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1046293,'2023-08-20');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1155558,'2023-08-27');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1833945,'2023-09-03');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(927862,'2023-09-10');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1453844,'2023-09-17');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1931819,'2023-09-24');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1895531,'2023-10-01');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(878072,'2023-10-08');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1409053,'2023-10-15');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2287849,'2023-10-22');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2135902,'2023-10-29');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2066375,'2023-11-05');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1627350,'2023-11-12');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2086252,'2023-11-19');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(2197180,'2023-11-26');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1978387,'2023-12-03');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1335976,'2023-12-10');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1709069,'2023-12-17');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1992546,'2023-12-24');
INSERT INTO Rakitra(volaRakitra, dateRakitra) values(1990000,'2023-12-31');

insert into Rakitra(volaRakitra,dateRakitra) values (2224761,'2024-01-07');
insert into Rakitra(volaRakitra,dateRakitra) values (2782304,'2024-01-14');
insert into Rakitra(volaRakitra,dateRakitra) values (1554495,'2024-01-21');
insert into Rakitra(volaRakitra,dateRakitra) values (2633209,'2024-01-28');
insert into Rakitra(volaRakitra,dateRakitra) values (2394950,'2024-02-04');
insert into Rakitra(volaRakitra,dateRakitra) values (1515962,'2024-02-11');
insert into Rakitra(volaRakitra,dateRakitra) values (2213440,'2024-02-18');
insert into Rakitra(volaRakitra,dateRakitra) values (2220491,'2024-02-25');
insert into Rakitra(volaRakitra,dateRakitra) values (2188935,'2024-03-03');
insert into Rakitra(volaRakitra,dateRakitra) values (1890000,'2024-03-10');

INSERT INTO Trosa (idOlona,volaTrosa,dateTrosa) VALUES (-1,194783345,'2001-08-02');


INSERT INTO Statut (nomStatut) VALUES 
	('Mpivavaka'),
	('Mpandray');


SELECT EXTRACT(YEAR FROM dateRakitra) AS Annee, AVG(volaRakitra) AS Moyenne_Vola FROM Rakitra WHERE dateRakitra < '2024-03-15' GROUP BY EXTRACT(YEAR FROM dateRakitra);
\dv afficher view
\dt afficher table