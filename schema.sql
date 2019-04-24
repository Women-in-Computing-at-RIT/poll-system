DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS polls;
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS votes;

CREATE TABLE users (slack_id TEXT PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, is_admin INTEGER);
CREATE TABLE polls (poll_id TEXT PRIMARY KEY, author TEXT NOT NULL, title TEXT NOT NULL, description TEXT NOT NULL, can_add INTEGER NOT NULL, multi_select INTEGER NOT NULL, timestamp INTEGER NOT NULL, type TEXT NOT NULL, FOREIGN KEY (author) REFERENCES users(slack_id));
CREATE TABLE options (option_id TEXT PRIMARY KEY, poll_id TEXT NOT NULL, option_text TEXT NOT NULL, FOREIGN KEY (poll_id) REFERENCES polls(poll_id));
CREATE TABLE votes (vote_id INTEGER PRIMARY KEY AUTOINCREMENT, slack_id TEXT NOT NULL, option_id TEXT NOT NULL, FOREIGN KEY (slack_id) REFERENCES users(slack_id), FOREIGN KEY (option_id) REFERENCES options(option_id));

SELECT * FROM polls;

COMMIT;