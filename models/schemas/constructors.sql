-- constructors table

CREATE TABLE constructors (
    "constructorStandingsId" INTEGER NOT NULL PRIMARY KEY,
    "raceId" INTEGER NOT NULL REFERENCES "races"("raceId"),
    "constructorId" INTEGER NOT NULL REFERENCES "constructors"("constructorId"),
	"points" INTEGER NOT NULL,
	"position" INTEGER NOT NULL,
	"positionText" TEXT NOT NULL,
	"wins" INTEGER NOT NULL
);