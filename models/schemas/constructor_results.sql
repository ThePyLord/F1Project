-- constructor_results table

CREATE TABLE constructor_results (
	"constructorResultsId"	INTEGER NOT NULL PRIMARY KEY,
	"raceId"	INTEGER NOT NULL REFERENCES races(raceId),
	"constructorId"	INTEGER NOT NULL REFERENCES constructors(constructorId),
	"points"	INTEGER NOT NULL,
	"status"	TEXT
);

