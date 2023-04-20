CREATE TABLE IF NOT EXISTS users (
  id serial PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS brands (
  id serial PRIMARY KEY,
  brand VARCHAR(20),
  description VARCHAR(500),
  s3_logo_url VARCHAR(100),
  flask_href VARCHAR(100)
);