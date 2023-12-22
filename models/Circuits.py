from app import db


class Circuits(db.Model):
    __tablename__ = 'circuits'
    circuitId = db.Column(db.Integer, primary_key=True)
    circuitRef = db.Column(db.String(255))
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    country = db.Column(db.String(255))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    alt = db.Column(db.Integer)
    url = db.Column(db.String(255))

    def __repr__(self):
        return '<Circuits %r>' % self.name

    def serialize(self):
        return {
            "circuitId": self.circuitId,
            "circuitRef": self.circuitRef,
            "name": self.name,
            "location": self.location,
            "country": self.country,
            "lat": self.lat,
            "lng": self.lng,
            "alt": self.alt,
            "url": self.url
        }


class ConstructorResults(db.Model):
    __tablename__ = 'constructor_results'
    constructorResultsId = db.Column(db.Integer, primary_key=True)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), nullable=False)
    constructorId = db.Column(db.Integer, db.ForeignKey('constructors.constructorId'), nullable=False)
    points = db.Column(db.Integer)
    status = db.Column(db.String(255))

    # Define relationship to constructor
    constructor = db.relationship('Constructors', backref='constructor_results', lazy=True)
    race_rel = db.relationship('Races', backref='constructor_results', lazy=True)

    def __repr__(self):
        return '<ConstructorResults %r>' % self.constructorResultsId

    def serialize(self):
        return {
            "constructorResultsId": self.constructorResultsId,
            "raceId": self.raceId,
            "constructorId": self.constructorId,
            "points": self.points,
            "status": self.status
        }


class ConstructorStandings(db.Model):
    __tablename__ = 'constructor_standings'
    constructorStandingsId = db.Column(db.Integer, primary_key=True, nullable=False)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), nullable=False)
    constructorId = db.Column(db.Integer, db.ForeignKey('constructors.constructorId'), nullable=False)
    points = db.Column(db.Integer)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))
    wins = db.Column(db.Integer)

    # Define relationship to constructor
    race = db.relationship('Races', backref='constructor_standings', lazy=True)
    constructor = db.relationship('Constructors', backref='constructor_standings', lazy=True)

    def __repr__(self):
        return '<ConstructorStandings %r>' % self.constructorStandingsId

    def serialize(self):
        return {
            "constructorStandingsId": self.constructorStandingsId,
            "raceId": self.raceId,
            "constructorId": self.constructorId,
            "points": self.points,
            "position": self.position,
            "positionText": self.positionText,
            "wins": self.wins
        }


class Constructors(db.Model):
    __tablename__ = 'constructors'
    constructorStandingsId = db.Column(db.Integer, primary_key=True)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), nullable=False)
    constructorId = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))
    wins = db.Column(db.Integer)

    # Define relationship to constructor
    race = db.relationship('Races', backref='constructors', lazy=True)
    # constructor = db.relationship('Constructors', backref='constructors', lazy=True)


    def __repr__(self):
        return '<Constructors %r>' % self.constructorStandingsId

    def serialize(self):
        return {
            'constructorStandingsId': self.constructorStandingsId,
            'raceId': self.raceId,
            'constructorId': self.constructorId,
            'points': self.points,
            'position': self.position,
            'positionText': self.positionText,
            'wins': self.wins
        }


class DriverStandings(db.Model):
    __tablename__ = 'driver_standings'
    driverStandingsId = db.Column(db.Integer, primary_key=True, nullable=False)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), nullable=False)
    points = db.Column(db.Integer)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))

    # Define relationship to driver
    races = db.relationship('Races', backref='driver_standings', lazy=True)
    driver = db.relationship('Drivers', backref='driver_standings', lazy=True)

    def __repr__(self):
        return '<DriverStandings %r>' % self.driverStandingsId

    def serialize(self):
        return {
            'driverStandingsId': self.driverStandingsId,
            'raceId': self.raceId,
            'driverId': self.driverId,
            'points': self.points,
            'position': self.position,
            'positionText': self.positionText
        }


class Drivers(db.Model):
    __tablename__ = 'drivers'
    driverId = db.Column(db.Integer, primary_key=True, nullable=False)
    driverRef = db.Column(db.String(255))
    number = db.Column(db.Integer)
    code = db.Column(db.String(255))
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    dob = db.Column(db.DateTime)
    nationality = db.Column(db.String(255))
    url = db.Column(db.String(255))

    def __repr__(self):
        return '<Drivers %r>' % self.driverId

    def serialize(self):
        return {
            'driverId': self.driverId,
            'driverRef': self.driverRef,
            'number': self.number,
            'code': self.code,
            'forename': self.forename,
            'surname': self.surname,
            'dob': self.dob,
            'nationality': self.nationality
        }


class LapTimes(db.Model):
    __tablename__ = 'lap_times'
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), primary_key=True, nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), primary_key=True, nullable=False)
    lap = db.Column(db.Integer)
    position = db.Column(db.Integer)
    time = db.Column(db.Time)
    milliseconds = db.Column(db.Integer)

    # Define relationship to driver
    driver = db.relationship('Drivers', backref='lap_times', lazy=True)
    race = db.relationship('Races', backref='lap_times', lazy=True)

    def __repr__(self):
        return '<LapTimes %r>' % self.raceId

    def serialize(self):
        return {
            'raceId': self.raceId,
            'driverId': self.driverId,
            'lap': self.lap,
            'position': self.position,
            'time': self.time,
            'milliseconds': self.milliseconds
        }


class PitStops(db.Model):
    __tablename__ = 'pit_stops'
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), primary_key=True, nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), primary_key=True, nullable=False)
    stop = db.Column(db.Integer)
    lap = db.Column(db.Integer)
    time = db.Column(db.Time)
    duration = db.Column(db.Time)
    milliseconds = db.Column(db.Integer)

    # Define relationship to driver
    driver = db.relationship('Drivers', backref='pit_stops', lazy=True)
    race = db.relationship('Races', backref='pit_stops', lazy=True)

    def __repr__(self):
        return '<PitStops %r>' % self.raceId

    def serialize(self):
        return {
            'raceId': self.raceId,
            'driverId': self.driverId,
            'stop': self.stop,
            'lap': self.lap,
            'time': self.time,
            'duration': self.duration,
            'milliseconds': self.milliseconds
        }


class Qualifying(db.Model):
    __tablename__ = 'qualifying'
    qualifyingId = db.Column(db.Integer, primary_key=True, nullable=False)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), nullable=False)
    constructorId = db.Column(db.Integer, db.ForeignKey('constructors.constructorId'), nullable=False)
    number = db.Column(db.Integer)
    position = db.Column(db.Integer)
    q1 = db.Column(db.Time)
    q2 = db.Column(db.Time)
    q3 = db.Column(db.Time)

    # Define relationship to driver
    race = db.relationship('Races', backref='qualifying', lazy=True)
    driver = db.relationship('Drivers', backref='qualifying', lazy=True)
    constructor = db.relationship('Constructors', backref='qualifying', lazy=True)

    def __repr__(self):
        return '<Qualifying %r>' % self.qualifyingId

    def serialize(self):
        return {
            'qualifyingId': self.qualifyingId,
            'raceId': self.raceId,
            'driverId': self.driverId,
            'constructorId': self.constructorId,
            'number': self.number,
            'position': self.position,
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3
        }


class Races(db.Model):
    __tablename__ = 'races'
    raceId = db.Column(db.Integer, primary_key=True, nullable=False)
    year = db.Column(db.Integer)
    round = db.Column(db.Integer)
    circuitId = db.Column(db.Integer, db.ForeignKey('circuits.circuitId'), nullable=False)
    name = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    time = db.Column(db.Time)
    url = db.Column(db.String(255))
    fp1_date = db.Column(db.Time)
    fp2_date = db.Column(db.Time)
    fp3_date = db.Column(db.Time)
    fp3_time = db.Column(db.Time)
    quali_date = db.Column(db.Time)
    quali_time = db.Column(db.Time)
    sprint_date = db.Column(db.Time)
    sprint_time = db.Column(db.Time)

    # Define relationship to circuit
    circuit = db.relationship('Circuits', backref='Races', lazy=True)

    def __repr__(self):
        return '<Races %r>' % self.raceId

    def serialize(self):
        return {
            'raceId': self.raceId,
            'year': self.year,
            'round': self.round,
            'circuitId': self.circuitId,
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'url': self.url,
            'fp1_date': self.fp1_date,
            'fp2_date': self.fp2_date,
            'fp3_date': self.fp3_date,
            'fp3_time': self.fp3_time,
            'quali_date': self.quali_date,
            'quali_time': self.quali_time,
            'sprint_date': self.sprint_date,
            'sprint_time': self.sprint_time
        }


class Results(db.Model):
    __tablename__ = 'results'
    resultId = db.Column(db.Integer, primary_key=True, nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), primary_key=True, nullable=False)
    constructorId = db.Column(db.Integer, db.ForeignKey('constructors.constructorId'), primary_key=True, nullable=False)
    number = db.Column(db.Integer)
    grid = db.Column(db.Integer)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))
    positionOrder = db.Column(db.Integer)
    points = db.Column(db.Integer)
    laps = db.Column(db.Integer)
    time = db.Column(db.Time)
    milliseconds = db.Column(db.Integer)
    fastestLap = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    fastestLapTime = db.Column(db.Time)
    fastestLapSpeed = db.Column(db.Float)
    statusId = db.Column(db.Integer, db.ForeignKey('status.statusId'), nullable=False)

    # Define relationship to driver
    driver = db.relationship('Drivers', backref='results', lazy=True)
    constructor = db.relationship('Constructors', backref='results', lazy=True)
    status = db.relationship('Status', backref='results', lazy=True)

    def __repr__(self):
        return '<Results %r>' % self.driverId

    def serialize(self):
        return {
            'resultId': self.resultId,
            'driverId': self.driverId,
            'constructorId': self.constructorId,
            'number': self.number,
            'grid': self.grid,
            'position': self.position,
            'positionText': self.positionText,
            'positionOrder': self.positionOrder,
            'points': self.points,
            'laps': self.laps,
            'time': self.time,
            'milliseconds': self.milliseconds,
            'fastestLap': self.fastestLap,
            'rank': self.rank,
            'fastestLapTime': self.fastestLapTime,
            'fastestLapSpeed': self.fastestLapSpeed,
            'statusId': self.statusId
        }


class Seasons(db.Model):
    __tablename__ = 'seasons'
    year = db.Column(db.Integer, primary_key=True, nullable=False)
    url = db.Column(db.String(255))

    def __repr__(self):
        return '<Seasons %r>' % self.year

    def serialize(self):
        return {
            'year': self.year,
            'url': self.url
        }


class SprintResults(db.Model):
    __tablename__ = 'sprint_results'
    resultId = db.Column(db.Integer, db.ForeignKey('results.resultId'), primary_key=True, nullable=False)
    raceId = db.Column(db.Integer, db.ForeignKey('races.raceId'), primary_key=True, nullable=False)
    driverId = db.Column(db.Integer, db.ForeignKey('drivers.driverId'), primary_key=True, nullable=False)
    grid = db.Column(db.Integer)
    position = db.Column(db.Integer)
    positionText = db.Column(db.String(255))
    positionOrder = db.Column(db.Integer)
    points = db.Column(db.Integer)
    time = db.Column(db.Time)
    milliseconds = db.Column(db.Integer)
    fastestLap = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    fastestLapTime = db.Column(db.Time)
    statusId = db.Column(db.Integer, db.ForeignKey('status.statusId'), nullable=False)

    # Define relationship to driver
    driver = db.relationship('Drivers', backref='sprint_results', lazy=True)
    result = db.relationship('Results', backref='sprint_results', lazy=True)
    race = db.relationship('Races', backref='sprint_results', lazy=True)
    status = db.relationship('Status', backref='sprint_results', lazy=True)

    def __repr__(self):
        return '<SprintResults %r>' % self.resultId

    def serialize(self):
        return {
            'resultId': self.resultId,
            'raceId': self.raceId,
            'driverId': self.driverId,
            'grid': self.grid,
            'position': self.position,
            'positionText': self.positionText,
            'positionOrder': self.positionOrder,
            'points': self.points,
            'time': self.time,
            'milliseconds': self.milliseconds,
            'fastestLap': self.fastestLap,
            'rank': self.rank,
            'fastestLapTime': self.fastestLapTime,
            'statusId': self.statusId
        }


class Status(db.Model):
    __tablename__ = 'status'
    statusId = db.Column(db.Integer, primary_key=True, nullable=False)
    status = db.Column(db.String(255))

    def __repr__(self):
        return '<Status %r>' % self.statusId

    def serialize(self):
        return {
            'statusId': self.statusId,
            'status': self.status
        }
