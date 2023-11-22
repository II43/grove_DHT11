import time
import seeed_dht

def main():
    sensor = seeed_dht.DHT('11', 12)
    while True:
        hum, T = sensor.read()
        print(f'DHT{sensor.dht_type}, humidity {hum} %, temperature {T} degC')
        time.sleep(1)

if __name__ == '__main__':
    main()