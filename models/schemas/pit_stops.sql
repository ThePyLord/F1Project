-- pit_stops table

CREATE TABLE pit_stops (
    "raceId" INTEGER NOT NULL REFERENCES races(raceId),
    "driverId" INTEGER NOT NULL REFERENCES drivers(driverId),
    "stop" INTEGER NOT NULL,
    "lap" INTEGER NOT NULL,
    "time" TEXT,
    "duration" TEXT,
    "milliseconds" INTEGER,
    PRIMARY KEY ("raceId", "driverId")
);