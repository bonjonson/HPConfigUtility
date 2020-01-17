import telnetlib
import model_check

# функция для перезагрузки устройства
def reboot():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'boot\n')
    model_check.telnet.read_until(b'continue')
    model_check.telnet.write(b'y\n')