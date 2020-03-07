# This file is executed on every boot (including wake-boot from deepsleep)
# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import webrepl
webrepl.start()
webrepl.start(password='12345678')

import network
sta_if = network.WLAN(network.STA_IF)

def do_connect():
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        #sta_if.ifconfig(('192.168.1.251','255.255.255.0','192.168.1.1','8.8.8.8'))
        sta_if.connect('CLARO_280FB9', 'B18D64AB99')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
