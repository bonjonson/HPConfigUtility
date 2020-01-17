import telnetlib
import model_check

# функция пропуска приветственного экрана для моделей 2520
def scip_intro():
    model_check.telnet.read_until(b'continue', timeout = 10)
    model_check.telnet.write(b'\n')