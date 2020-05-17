class View:
    def start(self):
        print("================================")
        print("=   ¡Bienvenido a la Agenda!   =")
        print("================================")

    def end(self):
        print("=================================")
        print("=       ¡Hasta la vista!        =")
        print("=================================")

    def main_menu(self):
        print('**********************************')
        print('** --     Menú Príncipal     -- **')
        print('**********************************')
        print('1. CPs')
        print('2. Contactos')
        print('3. Citas')
        print('4. Salir')

    def option(self, last):
        print('Selecciona una opción (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opción no válida!\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """View for Zips"""

    def zips_menu(self):
        print('*********************')
        print('* -- SubMenú CPs -- *')
        print('*********************')
        print('1. Agregar CP')
        print('2. Leer CP')
        print('3. Leer todos los CPs')
        print('4. Leer CPs de una ciudad')
        print('5. Actualizar CP')
        print('6. Borrar CP')
        print('7. Regresar')

    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')

    def show_zip_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)

    def show_zip_midder(self):
        print('-'*78)

    def show_zip_footer(self):
        print('*'*78)

    """View for contacts"""

    def contacts_menu(self):
        print('***************************')
        print('* -- SubMenú contactos -- *')
        print('***************************')
        print('1. Agregar contacto')
        print('2. Leer contacto')
        print('3. Leer todos los contactos')
        print('4. Leer contactos de un CP')
        print('5. Leer contactos de una ciudad')
        print('6. Actualizar contacto')
        print('7. Borrar contacto')
        print('8. Regresar')

    def show_a_contact(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido paterno: ', record[2])
        print('Apellido materno: ', record[3])
        print('Calle: ', record[4])
        print('No Exterior: ', record[5])
        print('No Interior: ', record[6])
        print('Colonia: ', record[7])
        print('Ciudad: ', record[11])
        print('Estado: ', record[12])
        print('CP: ', record[8])
        print('Email: ', record[9])
        print('Teléfono: ', record[10])

    def show_a_contact_brief(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3])
        print('Dirección: ', record[4] +' '+record[5]+' - '+record[6]+', '+record[7])
        print(record[11]+', '+record[12]+', '+record[8])
        print('Email: ', record[9])
        print('Teléfono: ', record[10])

    def show_contact_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_contact_midder(self):
        print('-'*53)

    def show_contact_footer(self):
        print('*'*53)

    """Views for Appointment"""

    def appointment_menu(self):
        print('*************************')
        print('* -- SubMenú Citas -- *')
        print('*************************')
        print('1. Agregar cita')
        print('2. Leer cita')
        print('3. Leer todas las citas')
        print('4. Leer citas en un lugar')
        print('5. Leer citas de una fecha')
        print('6. Actualizar datos de una cita')
        print('7. Borrar cita')
        print('8. Salir')

    def show_appointment(self, record):
        print('ID: ', record[0])
        print('Asunto de la cita: ', record[2])
        print('Lugar de la cita: ', record[3])
        print('Fecha de la cita: ', record[4])
        print('Hora de la cita: ', record[5])
        print('Datos del contacto: '.center(81,'*'))
        self.show_a_contact_brief(record[6:])

    def show_appointment_header(self, header):
        print(header.center(81,'+'))

    def show_appointment_midder(self):
        print('/'*81)

    def show_appointment_footer(self):
        print('+'*81)

    