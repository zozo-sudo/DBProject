DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Sugang;
DROP TABLE IF EXISTS VideoAndHomework;

CREATE TABLE "Class" (
	"cID"	INTEGER NOT NULL UNIQUE,
	"NumOfPerson"	INTEGER,
	"cName"	TEXT NOT NULL,
	PRIMARY KEY("cID")
);
CREATE TABLE "Student" (
	"sID"	INTEGER NOT NULL UNIQUE,
	"PW"	TEXT NOT NULL,
	"sName"	INTEGER NOT NULL,
	PRIMARY KEY("sID")
);
CREATE TABLE "Sugang" (
	"sID"	INTEGER,
	"cID"	INTEGER,
	foreign key (sID) references Student(sID) on delete CASCADE on update CASCADE,
	foreign key (cID) references Class(cID) on delete CASCADE on update CASCADE
);
CREATE TABLE "VideoAndHomework" (
	"cID"	INTEGER,
	"sID"	INTEGER,
	"VAHName"	TEXT,
	"DeadLine"	INTEGER,
	"Decision"	TEXT,
	FOREIGN KEY("cID") REFERENCES "Class"("cID") on delete CASCADE on update CASCADE
);