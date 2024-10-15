import sys

from PySide6.QtWidgets import QApplication

from ventana_principal import BuscadorPeliculas

def main():
    app = QApplication(sys.argv)
    ventana = BuscadorPeliculas()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
