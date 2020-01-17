import model_check
import telnetlib

# функция завершения сессии
def close_session():
    model_check.telnet.close()