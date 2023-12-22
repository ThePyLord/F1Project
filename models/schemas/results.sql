-- results table

CREATE TABLE results (
    "resultId" INTEGER PRIMARY KEY,
    "driverId" INTEGER REFERENCES drivers("driverId"),
    "constructorId" INTEGER REFERENCES constructors("constructorId"),
    "number" INTEGER,
    "grid" INTEGER,
    "position" INTEGER,
    "positionText" TEXT,
    "positionOrder" INTEGER,
    "points" INTEGER,
    "laps" INTEGER,
    "time" TEXT,
    "milliseconds" INTEGER,
    "fastestLap" INTEGER,
    "rank" INTEGER,
    "fastestLapTime" TEXT,
    "fastestLapSpeed" TEXT,
    "statusId" INTEGER REFERENCES status("statusId")
);