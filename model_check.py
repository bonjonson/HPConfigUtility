import hosts_pool
import telnetlib
import ipaddress
import main

# функция проверки модели устройства
def check_model():
    global telnet
    telnet = telnetlib.Telnet(main.ip)
    get_version_string = str(telnet.read_until(b'Copyright'))
    if main.model_2520 in get_version_string:
        version = main.model_2520
    elif main.model_2530 in get_version_string:
        version = main.model_2530
    else:
        version = 'another'
    return(version)