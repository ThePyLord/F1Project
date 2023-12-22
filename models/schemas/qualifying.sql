-- qualifying table

CREATE TABLE qualifying (
    "qualifyingId" INTEGER PRIMARY KEY,
    raceId INTEGER NOT NULL REFERENCES races(raceId),
    driverId INTEGER NOT NULL REFERENCES drivers(driverId),
    constructorId INTEGER NOT NULL REFERENCES constructors(constructorId),
    "number" INTEGER,
    "position" INTEGER,
    "q1" TEXT,
    "q2" TEXT,
    "q3" TEXT
)