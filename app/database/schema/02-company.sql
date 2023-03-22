--A company has a name, mission, NUIS (identifing number).

CREATE TABLE company(
   nuis INT NOT NULL,
   name VARCHAR(255) NOT NULL,
   mission VARCHAR(255),
   PRIMARY KEY (nuis)
);