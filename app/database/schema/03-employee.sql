--The company has multiple employees whom have different roles

CREATE TABLE employee(
   id INT GENERATED ALWAYS AS IDENTITY,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255) NOT NULL,
   company_nuis INT NOT NULL,
   role_id INT NOT NULL,
   PRIMARY KEY (id),
   CONSTRAINT fk_company_nuis FOREIGN KEY(company_nuis) REFERENCES company(nuis),
   CONSTRAINT fk_role FOREIGN KEY(role_id) REFERENCES role(id)
);