import model_check
import telnetlib

# функция для обновления по tftp
def swi_update_2520():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'copy tftp flash 10.157.197.253 S2520.swi primary\n')
    model_check.telnet.read_until(b'OS')
    model_check.telnet.write(b'y\n')
    model_check.telnet.read_until(b'#')
    model_check.telnet.close()