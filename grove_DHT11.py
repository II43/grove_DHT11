#!/usr/bin/python3
import time
import seeed_dht
import RPi.GPIO as GPIO

LED = 12 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

def main():
    sensor = seeed_dht.DHT('11', 12)
    led_state = True 
    while True:
        hum, T = sensor.read()
        print(f'DHT{sensor.dht_type}, humidity {hum} %, temperature {T} degC')
        time.sleep(1)
        GPIO.output(LED, led_state)
        led_state = not led_state 

if __name__ == '__main__':
    main()