import sys
from PySide6.QtWidgets import QApplication
from controlador import Controlador

def main():
    app = QApplication(sys.argv)
    controlador = Controlador()
    controlador.mostrar_pantalla()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
