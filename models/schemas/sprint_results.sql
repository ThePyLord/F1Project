-- sprint_results table

CREATE TABLE sprint_results (
    "resultId" INTEGER REFERENCES results("resultId"),
    "raceId" INTEGER REFERENCES races("raceId") ,
    "driverId" INTEGER REFERENCES drivers("driverId"),
    "constructorId" INTEGER REFERENCES constructors("constructorId"),
    "grid" INTEGER NOT NULL,
    "position" INTEGER NOT NULL,
    "positionText" TEXT NOT NULL,
    "positionOrder" INTEGER NOT NULL,
    "points" INTEGER NOT NULL,
    "laps" INTEGER NOT NULL,
    "time" TEXT,
    "milliseconds" INTEGER,
    "fastestLap" TEXT,
    "rank" INTEGER,
    "statusId" INTEGER REFERENCES status("statusId"),
    PRIMARY KEY ("resultId", "raceId", "driverId")
)