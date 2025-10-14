CREATE SCHEMA IF NOT EXISTS sys;
CREATE SCHEMA IF NOT EXISTS items;

CREATE TABLE IF NOT EXISTS sys.users (
  id serial PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS items.phones (
  id serial PRIMARY KEY,
  model VARCHAR(30),
  brand VARCHAR(20),
  storage VARCHAR(10),
  colour VARCHAR(20),
  network VARCHAR(20),
  os VARCHAR(20),
  condition VARCHAR(20),
  price FLOAT,
  staticimg VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS items.brands (
  id serial PRIMARY KEY,
  brand VARCHAR(20),
  description VARCHAR(500),
  static_logo_url VARCHAR(200),
  flask_href VARCHAR(100)
);

/* GRANT */
GRANT ALL PRIVILEGES ON DATABASE fonexpert TO sebbey_com;
GRANT ALL PRIVILEGES ON SCHEMA fonexpert TO sebbey_com;
GRANT ALL PRIVILEGES ON TABLE fonexpert.brands TO sebbey_com;
GRANT ALL PRIVILEGES ON TABLE fonexpert.users TO sebbey_com;
GRANT ALL PRIVILEGES ON TABLE fonexpert.phone TO sebbey_com;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA fonexpert to sebbey_com;
