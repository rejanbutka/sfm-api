--Each farm has a location, area, expected outpup, number of panels, landscape (mountain, hill, etc) and orientation (North, East, NE, SW etc)

CREATE TABLE farm(
   id INT GENERATED ALWAYS AS IDENTITY,
   location VARCHAR(255),
   area NUMERIC(7, 2),
   no_panels INT,
   landscape_id INT,
   orientation_id INT,
   company_nuis INT,
   PRIMARY KEY (id),
   CONSTRAINT fk_landscape_id FOREIGN KEY(landscape_id) REFERENCES farm_landscape(id),
   CONSTRAINT fk_orientation_id FOREIGN KEY(orientation_id) REFERENCES farm_orientation(id),
   CONSTRAINT fk_company_nuis FOREIGN KEY(company_nuis) REFERENCES company(nuis)
);