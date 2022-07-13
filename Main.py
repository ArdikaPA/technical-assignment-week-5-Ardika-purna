import Adafruit_DHT

DHT_11 = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_11, DHT_PIN)

    if humidity is not None and temperature is not None: 
        print("Suhu Ruangan={0:0.1f}*C  Kelembapan={1:0.1f}%".format(humidity, temperature))
    else:
        print("Lost Data")
