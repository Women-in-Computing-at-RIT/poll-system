DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS poll;
DROP TABLE IF EXISTS options;

CREATE TABLE users (
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  is_admin INTEGER
);

CREATE TABLE poll (
  poll_id INTEGER PRIMARY KEY,
  FOREIGN KEY (author) REFERENCES users (username),
  title TEXT NOT NULL
);

CREATE TABLE options (
    option_id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (poll_id) REFERENCES poll (poll_id),
    option_text TEXT NOT NULL,
    option_image TEXT,
    tally INTEGER
);