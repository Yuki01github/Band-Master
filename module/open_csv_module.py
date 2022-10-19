from subprocess import Popen
import webbrowser


def main():
    src = r'.\figure\data.csv'
    executer = r'C:\Software\Cassava\Cassava.exe'
    open_help_func()


def open_csv_func(src):
    # subprocess.Popen(['start', executer], shell=True)
    Popen(['start', src], shell=True)


def open_help_func():
    # Popen([r'%Windir%\notepad.exe', r'.\README.html'], shell=True)
    webbrowser.open(".\\README.html")


def create_csv_func():
    executer = r'C:\Software\Cassava\Cassava.exe'
    Popen(['start', executer], shell=True)


if __name__ == "__main__":
    main()
