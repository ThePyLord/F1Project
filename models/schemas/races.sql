-- races table

CREATE TABLE races (
    "raceId" INTEGER PRIMARY KEY NOT NULL,
    "year" INTEGER NOT NULL,
    "round" INTEGER NOT NULL,
    "circuitId" INTEGER NOT NULL REFERENCES circuits(circuitId),
    "name" TEXT NOT NULL,
    "date" TEXT NOT NULL,
    "time" TEXT,
    "url" TEXT,
    "fp1_date" TEXT,
	"fp1_time" TEXT,
	"fp2_date" TEXT,
	"fp2_time" TEXT,
	"fp3_date" TEXT,
	"fp3_time" TEXT,
	"quali_date" TEXT,
	"quali_time" TEXT,
	"sprint_date" TEXT,
	"sprint_time" TEXT
);