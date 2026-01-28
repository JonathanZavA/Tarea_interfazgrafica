from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from GUI.DATOS.persona_dao import PersonaDAO
from GUI.DOMINIO.Persona import Persona
from GUI.UI.vtnPrincipal import Ui_btn_guardar


class PersonaServicio(QMainWindow):
    '''
    Clase que genera la logica de los objetos de la persona
    '''

    def __init__(self):
        # Inicialización de la ventana principal y la interfaz
        super(PersonaServicio, self).__init__()
        self.ui = Ui_btn_guardar()
        self.ui.setupUi(self)

        # Conexión de eventos de botones con sus funciones correspondientes
        self.ui.btn_guardar_.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

        # Restricción para que el campo cédula solo acepte números
        self.ui.txt_cedula.setValidator(QIntValidator())

    def guardar(self):
        # Extracción de valores ingresados en los campos de la interfaz
        nombre = self.ui.txt_nombre.text()
        apellido = self.ui.txt_apellido.text()
        cedula = self.ui.txt_cedula.text()
        email = self.ui.txt_email.text()
        sexo = self.ui.txt_sexo.text()

        # Validacion de datos (Interfaz)
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Nombre")
        elif not nombre.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "ERROR NOMBRE. Debe ingresar texto")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Apellido")
        elif not apellido.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar texto")
        elif email == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Email")
        # BORRÉ LA VALIDACIÓN DE 'ISALPHA' EN EL EMAIL PORQUE ERA INCORRECTA
        elif len(cedula) > 10:  # Ojo: Aquí quizás quieras validar que sea == 10, no solo > 10
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cedula válida")
        elif sexo == "Selecione..." or sexo == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Sexo")

        else:

            try:
                # Intento de creación del objeto de dominio con sus validaciones internas
                persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, email=email, sexo=sexo)

                # Envío del objeto validado a la capa de datos para su inserción
                PersonaDAO.insertar_persona(persona)
                print(nombre)
                print(apellido)
                print(email)
                print(cedula)
                print(sexo)

                # Notificación visual de éxito y limpieza del formulario
                self.ui.statusbar.showMessage("Se guardo la persona", 1500)
                self.limpiar()

            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", str(e))

            except Exception as e:
                # Notificación visual de éxito y limpieza del formulario
                QMessageBox.critical(self, "Error Crítico", f"Ocurrió un error: {e}")
    def limpiar(self):
        # Restablecimiento de todos los componentes de la interfaz a su estado inicial
        self.ui.txtNombre.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText("Seleccione...")