CREATE TABLE IF NOT EXISTS "club"(
	id UUID PRIMARY KEY,
    name VARCHAR(255),
    about VARCHAR(255),
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

CREATE TABLE IF NOT EXISTS "club_coach"(
	id UUID PRIMARY KEY,
    coach_id UUID,
    club_id UUID
);
CREATE TABLE IF NOT EXISTS "competition" (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    about VARCHAR(255),
    price float,
    date timestamp,
    prize_pool float,
    limit_boxers INT,
    country VARCHAR(255),
    region VARCHAR(255),
    city VARCHAR(255),
    organizer_id UUID,
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

CREATE TABLE IF NOT EXISTS "competition_boxer" (
    id UUID PRIMARY KEY,
    boxer_id UUID,
    competition_id UUID
);


CREATE TABLE IF NOT EXISTS "score" (
    id UUID PRIMARY KEY,
    fight_id UUID,
    score_value INT,
    judge_id UUID
);

CREATE TABLE IF NOT EXISTS "fight" (
    id UUID PRIMARY KEY,
    competition_id UUID,
    fighter_one UUID,
    fighter_two UUID,
    winner UUID,
    date timestamp
);

ALTER TABLE "club_coach" ADD FOREIGN KEY (club_id) REFERENCES "club" (id);

ALTER TABLE "competition_boxer" ADD FOREIGN KEY (competition_id) REFERENCES "competition" (id);

ALTER TABLE "score" ADD FOREIGN KEY (fight_id) REFERENCES "fight" (id);

ALTER TABLE "fight" ADD FOREIGN KEY (competition_id) REFERENCES "competition" (id);
