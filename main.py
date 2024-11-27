import sys
from PySide6.QtWidgets import QApplication
from controlador import Controlador

def main():
    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.buscador.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
