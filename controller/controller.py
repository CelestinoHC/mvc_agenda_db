from model.model import Model
from view.view import View
from datetime import date

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """General Controllers"""

    def main_menu(self):
        o = '0'
        while o != '4':
            self.view.main_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.zips_menu()
            elif o == '2':
                self.contacts_menu()
            elif o == '3':
                self.appointment_menu()
            elif o == '4':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v !='':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """Controllers for zips"""

    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_a_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city, state]

    def create_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'agregó')
        else:
            if out.errno == 1062:
                self.view.error('El CP está repetido')
            else:
                self.view.error('No se pudo agregar el CP. Verifica.')
        return

    def read_a_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Problema al leer el CP. Verifica.')
        return

    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_zip_header(' Todos los CPs ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Problema al leer los CPs. Verifica.')
        return
        
    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header(' CPs para la ciudad '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Problema al leer los CPs. Verifica.')
        return

    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Problema al leer el CP. Verifica.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_zip()
        fields, vals = self.update_lists(['z_city', 'z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'actualizó')
        else:
            self.view.error('No se pudo actuaizar el CP. Verifica')
        return

    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count !=0:
            self.view.ok(i_zip, 'borró')
        else:
            if count == 0:
                self.view.error('El CP no existe')
            else:
                self.view.error('Problema al borrar el CP. Verifica')
        return

    """Controllers for Contacts"""

    def contacts_menu(self):
        o = '0'
        while o != '7':
            self.view.contacts_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_contact()
            elif o == '2':
                self.read_a_contact()
            elif o == '3':
                self.read_all_contacts()
            elif o == '4':
                self.read_contacts_zip()
            elif o == '5':
                self.read_contacts_city()
            elif o == '6':
                self.update_contact()
            elif o == '7':
                self.delete_contact()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_contact(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido Paterno: ')
        sname1 = input()
        self.view.ask('Apellido Materno: ')
        sname2 = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No Exterior: ')
        noext = input()
        self.view.ask('No Interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        return [name, sname1, sname2, street, noext, noint, col, zip, email, phone]

    def create_contact(self):
        name, sname1, sname2, street, noext, noint, col, zip, email, phone = self.ask_contact()
        out = self.model.create_contact(name, sname1, sname2, street, noext, noint, col, zip, email, phone)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agregó')
        else:
            self.view.error('No se pudo agregar el contacto. Verifica.')
        return

    def read_a_contact(self):
        self.view.ask('ID de contacto: ')
        id_contact = input()
        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al leer el contacto. Verifica.')
        return

    def read_all_contacts(self):
        contacts = self.model.read_all_contacts()
        if type(contacts) == list:
            self.view.show_contact_header(' Todos los contactos ')
            for contact in contacts:
                self.view.show_a_contact_brief(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('Problema al leer los contactos. Verifica.')
        return

    def read_contacts_zip(self):
        self.view.ask('CP: ')
        zip = input()
        contacts = self.model.read_contacts_zip(zip)
        if type(contacts) == list:
            self.view.show_contact_header(' Contactos en el CP '+zip+' ')
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('Problema al leer los contactos. Verifica.')
        return

    def read_contacts_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        contacts = self.model.read_contacts_city(city)
        if type(contacts) == list:
            self.view.show_contact_header(' Contactos en '+city+' ')
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('Problema al leer los contactos. Verifica.')
        return

    def update_contact(self):
        self.view.ask('ID de contacto a modificar: ')
        id_contact = input()
        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al leer el contacto. Verifica.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_contact()
        fields, vals = self.update_lists(['c_fname', 'c_sname1', 'c_sname2', 'c_street', 'c_noext', 'c_noint', 'c_col', 'c_zip', 'c_email', 'c_phone'], whole_vals)
        vals.append(id_contact)
        vals = tuple(vals)
        out = self.model.update_contact(fields, vals)
        if out == True:
            self.view.ok(id_contact, 'actualizó')
        else:
            self.view.error('No se pudo actuaizar el contacto. Verifica')
        return

    def delete_contact(self):
        self.view.ask('ID de contacto a borrar: ')
        id_contact = input()
        count = self.model.delete_contact(id_contact)
        if count !=0:
            self.view.ok(id_contact, 'borró')
        else:
            if count == 0:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al borrar el contacto. Verifica')
        return

    """Appointments Controllers"""

    def appointment_menu(self):
        o = '0'
        while o != '8':
            self.view.appointment_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_appointment()
            elif o == '2':
                self.read_a_appointment()
            elif o == '3':
                self.read_all_appointments()
            elif o == '4':
                self.read_appointments_place()
            elif o == '5':
                self.read_appointments_date()
            elif o == '6':
                self.update_appointment()
            elif o == '7':
                self.delete_appointment()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_appointment(self):
        self.view.ask('Asunto de la cita: ')
        affair = input()
        self.view.ask('Lugar de la cita: ')
        place = input()
        self.view.ask('Fecha de la cita: ')
        date = input()
        self.view.ask('Hora de la cita: ')
        hour = input()
        return [affair, place, date, hour]

    def create_appointment(self):
        self.view.ask('ID de contacto: ')
        id_contact = input()
        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header(' Datos del contacto '+id_contact+' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al leer el contacto. Verifica.')
            return
        affair, place, date, hour = self.ask_appointment()
        out = self.model.create_appointment(id_contact, affair, place, date, hour)
        if out == True:
            self.view.ok(affair, 'agregó')
        else:
            self.view.error('No se pudo agregar la cita. Verifica.')
        return

    def read_a_appointment(self):
        self.view.ask('ID de la cita: ')
        id_appointment = input()
        appointment = self.model.read_a_appointment(id_appointment)
        if type(appointment) == tuple:
            self.view.show_appointment_header(' Datos de la cita '+id_appointment+' ')
            self.view.show_appointment(appointment)
            self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            if appointment == None:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al leer la cita. Verifica.')
        return
    
    def read_all_appointments(self):
        appointments = self.model.read_all_appointments()
        if type(appointments) == list:
            self.view.show_appointment_header(' Todas las citas ')
            for appointment in appointments:
                self.view.show_appointment(appointment)
                self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('Problema al leer las citas. Verifica.')
        return

    def read_appointments_place(self):
        self.view.ask('Lugar de la cita: ')
        place = input()
        appointments = self.model.read_appointments_place(place)
        if type(appointments) == list:
            self.view.show_appointment_header(' Citas en el lugar '+place+' ')
            for appointment in appointments:
                self.view.show_appointment(appointment)
                self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('Problema al leer las citas. Verifica.')
        return

    def read_appointments_date(self):
        self.view.ask('Fecha de la cita: ')
        date = input()
        appointments = self.model.read_appointments_date(date)
        if type(appointments) == list:
            self.view.show_appointment_header(' Citas en la fecha '+date+' ')
            for appointment in appointments:
                self.view.show_appointment(appointment)
                self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            self.view.error('Problema al leer las citas. Verifica.')
        return

    def update_appointment(self):
        self.view.ask('ID de cita a modificar: ')
        id_appointment = input()
        appointment = self.model.read_a_appointment(id_appointment)
        if type(appointment) == tuple:
            self.view.show_appointment_header(' Datos de la cita '+id_appointment+' ')
            self.view.show_appointment(appointment)
            self.view.show_appointment_midder()
            self.view.show_appointment_footer()
        else:
            if appointment == None:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al leer la cita. Verifica.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        self.view.ask('ID de contacto: ')
        id_contact = input()
        self.view.ask('Asunto: ')
        a_affair = input()
        self.view.ask('Lugar: ')
        a_place = input()
        self.view.ask('Fecha(yyyy-mm-dd): ')
        a_date = input()
        self.view.ask('Hora(24hrs): ')
        a_hour = input()
        whole_vals = [id_contact, a_affair, a_place, a_date, a_hour]
        fields, vals = self.update_lists(['id_contact', 'a_affair', 'a_place', 'a_date', 'a_hour'], whole_vals)
        vals.append(id_appointment)
        vals = tuple(vals)
        out = self.model.update_appointment(fields, vals)
        if out == True:
            self.view.ok(id_appointment, 'actualizó')
        else:
            self.view.error('No se pudo actuaizar la cita. Verifica')
        return

    def delete_appointment(self):
        self.view.ask('ID de la cita a borrar: ')
        id_appointment = input()
        count = self.model.delete_appointment(id_appointment)
        if count !=0:
            self.view.ok(id_appointment, 'borró')
        else:
            if count == 0:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al borrar la cita. Verifica')
        return