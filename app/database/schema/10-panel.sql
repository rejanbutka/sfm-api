--The panels in a farm have also their own specifications: Brand, dimenstions, material

CREATE TABLE panel(
   id INT GENERATED ALWAYS AS IDENTITY,
   brand_id INT,
   dimensions_id INT,
   material_id INT,
   farm_id INT,
   PRIMARY KEY (id),
   CONSTRAINT fk_brand_id FOREIGN KEY(brand_id) REFERENCES panel_brand(id),
   CONSTRAINT fk_dimensions_id FOREIGN KEY(dimensions_id) REFERENCES panel_dimensions(id),
   CONSTRAINT fk_material_id FOREIGN KEY(material_id) REFERENCES panel_material(id),
   CONSTRAINT fk_farm_id FOREIGN KEY(farm_id) REFERENCES farm(id)
);