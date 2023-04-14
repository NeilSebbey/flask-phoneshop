CREATE TABLE IF NOT EXISTS user (
  id serial PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);