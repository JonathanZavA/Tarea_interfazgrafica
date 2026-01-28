import sys
from PySide6.QtWidgets import QApplication
from SERVICIOS.personaservicio import PersonaServicio

app = QApplication()
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())