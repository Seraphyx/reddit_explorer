CREATE TABLE IF NOT EXISTS comment (
	id					VARCHAR(7) NOT NULL,

	author				VARCHAR(20) NOT NULL,
	author_id			VARCHAR(6) NOT NULL,
	name				VARCHAR(10),
	parent_id			VARCHAR(10),
	link_id				VARCHAR(10),
	subreddit_id		VARCHAR(6),

	pull_ts 			DATETIME NOT NULL,
	created_utc 		DATETIME NOT NULL,

	depth 				TINYINT,
	edited 				BOOLEAN,
	gilded		 		TINYINT,

	score		 		MEDIUMINT,
	ups		 			MEDIUMINT,
	downs		 		MEDIUMINT,
	controversiality	MEDIUMINT,
	score_hidden 		BOOLEAN,
	collapsed 			BOOLEAN,

	body 				TEXT,

	PRIMARY KEY (id)
)