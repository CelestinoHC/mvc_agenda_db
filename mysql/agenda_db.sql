
#Create the database
CREATE DATABASE IF NOT EXISTS agenda_db;

#Select the database to work with
USE agenda_db;

CREATE TABLE IF NOT EXISTS zips(
	zip VARCHAR(6) NOT NULL,
	z_city VARCHAR(35) NOT NULL,
    z_state VARCHAR(35) NOT NULL,
    PRIMARY KEY(zip)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS contacts(
	id_contact INT NOT NULL AUTO_INCREMENT,
    c_fname VARCHAR(35) NOT NULL,
    c_sname1 VARCHAR(35) NOT NULL,
    c_sname2 VARCHAR(35),
    c_street VARCHAR(35) NOT NULL,
    c_noext VARCHAR(7) NOT NULL,
    c_noint VARCHAR(7),
    c_col VARCHAR(50),
    c_zip VARCHAR(6),
    c_email VARCHAR(20),
    c_phone VARCHAR(13),
    PRIMARY KEY(id_contact),
    CONSTRAINT fkzip_contacts FOREIGN KEY(c_zip)
		REFERENCES zips(zip)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS appointment(
	id_appointment INT NOT NULL AUTO_INCREMENT,
    id_contact INT NOT NULL,
    a_affair VARCHAR(85),
    a_place VARCHAR(35),
    a_date DATE NOT NULL,
    a_hour VARCHAR(5) NOT NULL,
    PRIMARY KEY(id_appointment),
    CONSTRAINT fkcont_appointment FOREIGN KEY(id_contact)
		REFERENCES contacts(id_contact)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

