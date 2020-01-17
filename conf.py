import telnetlib
import model_check

# функция входа в режим конфигурации
def conf_mode():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'conf t\n')