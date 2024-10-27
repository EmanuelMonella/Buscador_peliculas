import sys
from PySide6.QtWidgets import QApplication
from controlador import BuscadorPeliculas

def main():
    app = QApplication(sys.argv)
    ventana = BuscadorPeliculas()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
