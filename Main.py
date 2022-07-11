import Adafruit_DHT #library untuk memanggil sensor

DHT_SENSOR = Adafruit_DHT.DHT11 #penamaan untuk memanggil data sensor
DHT_PIN = 4 #penamaan pin input sensor

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) #membaca data yg diambil oleh sensor

    if humidity is not None and temperature is not None: 
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(humidity, temperature)) #menampilkan data sensor dgn format celcius
    else:
        print("Failed Import Data Sensor") #logic jika gagal mendapatkan data sensor
