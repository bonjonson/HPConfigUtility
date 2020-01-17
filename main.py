import telnetlib
import ipaddress
import hosts_pool
import model_check
import intro
import sign
import conf
import clock_check
import sntp
import swi_check
import swi2520
import swi2530
import save
import reboot
import close

model_2520 = 'J9137A'
model_2530 = 'J9780A'

for ip in hosts_pool.ip_pool:
    try:
        m = model_check.check_model()
        if m == model_2520:
            intro.scip_intro()
            sign.log_in()
            c = clock_check.clock_check()
            # sntp.sntp_settings()
            swi = swi_check.swi_check()
            # swi2520.swi_update_2520()
        elif h == model_2530:
            sign.log_in()
            c = clock_check.clock_check()
            # sntp.sntp_settings()
            swi = swi_check.swi_check()
            # swi2530.swi_update_2530()
        else:
            print(ip, 'unsupported')
            close.close_session()
        print(ip, ' model is ', m, ' clock is ', c, ' firmware is ', swi)
        # save.save_conf()
        # reboot.reboot()
        close.close_session()
    except:
        print(ip, 'host is unreachable')
        close.close_session()
        continue