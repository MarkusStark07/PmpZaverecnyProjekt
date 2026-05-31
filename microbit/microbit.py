from microbit import *
import radio

# 1. Nastavenie rádia
radio.on()
radio.config(group=10)
# ZAPIS: Zapína rádiový modul a nastavuje "skupinu" 10.
# Všetky micro:bity v projekte musia mať rovnaké číslo skupiny,
# aby sa "počuli" navzájom.

# 2. Inicializácia UART (Sériovej linky)
uart.init(baudrate=115200)
# ZAPIS: Pripravuje sériovú komunikáciu cez USB kábel.
# Baudrate 115200 je štandardná rýchlosť, ktorou si PC a micro:bit
# vymieňajú dáta.

while True:
    # 3. Čítanie z PC (UART)
    if uart.any():
        data = uart.read()
        radio.send_bytes(data)
        display.show(Image.ARROW_N)
        # ZAPIS: Ak PC pošle niečo cez USB, micro:bit to prečíta,
        # pošle to vzduchom (rádiom) a rozsvieti šípku hore.

    # 4. Čítanie z rádia
    incoming = radio.receive_bytes()
    if incoming:
        uart.write(incoming)
        display.show(Image.ARROW_S)
        # ZAPIS: Ak micro:bit zachytí rádio signál, pošle tieto dáta
        # do PC cez USB a rozsvieti šípku dole.