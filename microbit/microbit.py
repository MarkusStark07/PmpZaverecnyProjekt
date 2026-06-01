from microbit import *
import radio

radio.on()
radio.config(group=10)
uart.init(baudrate=115200)

display.show(Image.ASLEEP)

while True:
    # 1. Prijem z PC -> Rádio
    if uart.any():
        data_from_pc = uart.readline()
        if data_from_pc:
            msg = str(data_from_pc, 'utf-8').strip()
            radio.send(msg)
            # Vizuálna odozva
            display.show(Image.ARROW_N)
            sleep(200)
            display.show(Image.ASLEEP)

    # 2. Príjem z Rádia -> PC
    rcv_radio = radio.receive()
    if rcv_radio:
        uart.write(rcv_radio + '\n')
        # Vizuálna odozva
        display.show(Image.ARROW_S)
        sleep(200)
        display.show(Image.ASLEEP),