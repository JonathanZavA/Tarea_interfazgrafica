class Persona:
    '''
    Clase que crea objetos persona
    '''

    def __init__(self, cedula: str, nombre: str, apellido: str, sexo: str, email: str = None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.email = email

    # Cédula
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.isdigit():
            raise ValueError("La cédula debe contener solo números")
        self._cedula = valor

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    # Apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor.strip():
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = valor

    # Sexo
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        if valor.lower() not in ("masculino", "femenino", "prefiero no decirlo"):
            raise ValueError("El sexo debe ser 'masculino' o 'femenino'")
        self._sexo = valor

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor and "@" not in valor:
            raise ValueError("El email debe contener '@'")
        self._email = valor

    # STR
    def __str__(self):
        return (f"Persona[ Cédula: {self._cedula}, "
                f"Nombre: {self._nombre} {self._apellido}, "
                f"Sexo: {self._sexo}, "
                f"Email: {self._email if self._email else 'No registrado'} ]")