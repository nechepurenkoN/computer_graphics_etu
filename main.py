import threading

from PyQt5 import QtWidgets

from ui.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    with open("ui/style.qss") as f:
        try:
            app.setStyleSheet("\n".join(f.readlines()))
        except Exception as e:
            logging.error(e)
        else:
            logging.info("Stylesheets are included")
    window = MainWindow()
    window.show()
    logging.info("Show main window, starting main thread")
    main_thread = threading.Thread(target=app.exec_)
    main_thread.run()


if __name__ == "__main__":
    import sys
    import logging
    format_ = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Starting main...")
    main()
