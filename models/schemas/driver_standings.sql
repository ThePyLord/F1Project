-- driver_standings table

CREATE TABLE driver_standings (
	"driverStandingsId"	INTEGER NOT NULL PRIMARY KEY,
	"raceId"	INTEGER NOT NULL REFERENCES races(raceId),
	"driverId"	INTEGER NOT NULL REFERENCES drivers(driverId),
	"points"	INTEGER NOT NULL,
	"position"	INTEGER NOT NULL,
	"positionText"	TEXT NOT NULL
)