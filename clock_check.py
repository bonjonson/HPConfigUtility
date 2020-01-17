import model_check
import telnetlib

# функция проверки часов
def clock_check():
    global clock
    clock = ''
    model_check.telnet.read_until(b'#')
    model_check.telnet.write(b'sh time\n')
    s = str(model_check.telnet.read_until(b'#'))
    if '2020' in s:
        clock = 'correct'
    else:
        clock = 'incorrect'
    return(clock)