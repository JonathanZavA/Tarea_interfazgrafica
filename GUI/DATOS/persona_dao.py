from GUI.DATOS.conexion import Conexion


class PersonaDAO:
    _INSERT = ("INSERT INTO Personas (Nombres, apellidos, cedula, sexo, email)" "VALUES (?, ?, ?, ?, null)")

    @classmethod
    def insertar_persona(cls, persona):
        with Conexion.obtenerCursor() as cursor:
            datos = (persona.nombre, persona.apellido, persona.cedula,persona.email, persona.sexo)
            cursor.execute(cls._INSERT, datos)