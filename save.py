import telnetlib
import model_check

# функция для сохранения конфигурации
def save_conf():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'wr mem\n')