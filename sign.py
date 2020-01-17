import telnetlib
import model_check

# функция входа в систему
def log_in():
    model_check.telnet.read_until(b'Username')
    model_check.telnet.write(b'login\n')
    model_check.telnet.read_until(b'Password')
    model_check.telnet.write(b'password\n')