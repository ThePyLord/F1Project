-- circuits table

CREATE TABLE circuits (
    "circuitId" INTEGER PRIMARY KEY,
    "circuitRef" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "country" TEXT NOT NULL,
    "lat" REAL,
    "lng" REAL,
    "alt" INTEGER,
    "url" TEXT
);