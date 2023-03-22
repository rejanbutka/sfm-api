CREATE TABLE panel_dimensions(
   id INT GENERATED ALWAYS AS IDENTITY,
   length NUMERIC(7, 2) NOT NULL,
   width NUMERIC(7, 2) NOT NULL,
   height NUMERIC(7, 2) NOT NULL,
   PRIMARY KEY (id)
);