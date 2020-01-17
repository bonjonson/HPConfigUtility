import model_check
import telnetlib

# функция проверки прошивки
def swi_check():
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'sh flash\n')
    get_swi_version = str(model_check.telnet.read_until(b'#'))
    if 'S.15.09.0029' in get_swi_version:
        swi_version = 'Updated'
    elif 'YB.16.08.0001' in get_swi_version:
        swi_version = 'Updated'    
    else:
        swi_version = 'Outdated'
    return(swi_version)