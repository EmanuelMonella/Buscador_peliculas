import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from buscador_ui import Ui_buscador  # Asegúrate de que esto está correctamente importado

class VentanaBuscador(QMainWindow):
    def __init__(self):
        super().__init__()  # Llama al constructor de QMainWindow
        self.ui = Ui_buscador()  # Crea la instancia de la interfaz
        self.ui.setupUi(self)  # Configura la interfaz en el QMainWindow

    def run(self):
        self.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaBuscador()
    ventana.run()
