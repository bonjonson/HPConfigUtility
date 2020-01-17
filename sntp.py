import telnetlib
import model_check

# функция изменения sntp настроек
def sntp_settings():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'sntp 30\n')
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'sntp unicast\n')
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'sntp server priority 1 10.157.199.1\n')
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'time timezone 180\n')
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'timesync sntp\n')