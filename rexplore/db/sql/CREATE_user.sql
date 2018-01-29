CREATE TABLE IF NOT EXISTS user (
	id				VARCHAR(6) NOT NULL,
	name			VARCHAR(20) NOT NULL,

	pull_ts 		DATETIME NOT NULL,
	created_utc 	DATETIME,

	link_karma 		INT,
	comment_karma 	INT,

	is_employee 	BOOLEAN,
	is_mod 			BOOLEAN,
	verified 		BOOLEAN,

	PRIMARY KEY (id)
)