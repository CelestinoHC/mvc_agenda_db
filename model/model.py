from mysql import connector

class Model:

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """ZIP Methods"""

    def create_zip(self, zip, city, state):
        try:
            sql = 'INSERT INTO zips (`zip`, `z_city`, `z_state`) VALUES(%s, %s, %s)'
            vals = (zip, city, state)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_zip(self, zip):
        try:
            sql = 'SELECT * FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM zips'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_zips_city(self, city):
        try:
            sql = 'SELECT * FROM zips WHERE z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_zip(self, fields, vals):
        try:
            sql = 'UPDATE zips SET '+','.join(fields)+'WHERE zip = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_zip(self, zip):
        try:
            sql = 'DELETE FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """"Contacts Methods"""

    def create_contact(self, name, sname1, sname2, street, noext, noint, col, zip, email, phone):
        try:
            sql = 'INSERT INTO contacts (`c_fname`, `c_sname1`, `c_sname2`, `c_street`, `c_noext`, `c_noint`, `c_col`, `c_zip`, `c_email`, `c_phone`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (name, sname1, sname2, street, noext, noint, col, zip, email, phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err

    def read_a_contact(self, id_contact):
        try:
            sql = 'SELECT contacts.*, zips.z_city,zips.z_state FROM contacts JOIN zips ON contacts.c_zip = zips.zip AND contacts.id_contact = %s'
            vals = (id_contact,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_contacts(self):
        try:
            sql = 'SELECT contacts.*, zips.z_city,zips.z_state FROM contacts JOIN zips ON contacts.c_zip = zips.zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_contacts_zip(self, zip):
        try:
            sql = 'SELECT contacts.*, zips.z_city, zips.z_state FROM contacts JOIN zips ON contacts.c_zip = zips.zip AND contacts.c_zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_contacts_city(self, city):
        try:
            sql = 'SELECT contacts.*, zips.z_city, zips.z_state FROM contacts JOIN zips ON contacts.c_zip = zips.zip AND zips.z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_contact(self, fields, vals):
        try:
            sql = 'UPDATE contacts SET '+','.join(fields)+' WHERE id_contact = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_contact(self, id_contact):
        try:
            sql = 'DELETE FROM contacts WHERE id_contact = %s'
            vals = (id_contact,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """Appointments Methods"""

    def create_appointment(self, id_contact, affair, place, date, hour):
        try:
            sql = 'INSERT INTO appointment (`id_contact`, `a_affair`, `a_place`, `a_date`, `a_hour`) VALUES(%s, %s, %s, %s, %s)'
            vals = (id_contact, affair, place, date, hour)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_appointment(self, id_appointment):
        try:
            sql =  'SELECT appointment.*, contacts.*, zips.* FROM appointment JOIN contacts ON contacts.id_contact = appointment.id_contact AND appointment.id_appointment = %s JOIN zips ON zips.zip = contacts.c_zip'
            vals = (id_appointment,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_appointments(self):
        try:
            sql = 'SELECT appointment.*, contacts.*, zips.* FROM appointment JOIN contacts ON contacts.id_contact = appointment.id_contact JOIN zips ON zips.zip = contacts.c_zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_appointments_place(self, place):
        try:
            sql = 'SELECT appointment.*, contacts.*, zips.* FROM appointment JOIN contacts ON contacts.id_contact = appointment.id_contact AND appointment.a_place = %s JOIN zips ON zips.zip = contacts.c_zip'
            vals = (place,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_appointments_date(self, date):
        try:
            sql = 'SELECT appointment.*, contacts.*, zips.* FROM appointment JOIN contacts ON contacts.id_contact = appointment.id_contact AND appointment.a_date = %s JOIN zips ON zips.zip = contacts.c_zip'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_appointment(self, fields, vals):
        try:
            sql = 'UPDATE appointment SET '+','.join(fields)+' WHERE id_appointment = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_appointment(self, id_appointment):
        try:
            sql = 'DELETE FROM appointment WHERE id_appointment = %s'
            vals = (id_appointment,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



