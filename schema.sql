CREATE TABLE Users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Quizs(
    id SERIAL PRIMARY KEY,
    subject TEXT UNIQUE,
    private BOOLEAN,
    creator_id INTEGER
);

CREATE TABLE Questions(
    id SERIAL PRIMARY KEY,
    question TEXT,
    answer TEXT,
    option_1 TEXT,
    option_2 TEXT,
    option_3 TEXT,
    quiz_id INTEGER
);

CREATE TABLE Highscores(
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER,
    user_id INTEGER,
    score INTEGER
);

CREATE TABLE Answerank(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    amount INTEGER,
    level TEXT
);

CREATE TABLE Createrank(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    level TEXT
);
