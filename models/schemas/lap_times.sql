-- lap_times table

CREATE TABLE lap_times (
    "raceId" INTEGER NOT NULL,
    "driverId" INTEGER NOT NULL REFERENCES drivers(driverId),
    "lap" INTEGER NOT NULL,
    "position" INTEGER,
    "time" TEXT,
    "milliseconds" INTEGER,
    PRIMARY KEY ("raceId", "driverId")
)