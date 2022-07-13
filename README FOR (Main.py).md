import Adafruit_DHT               #library untuk memanggil sensor

DHT_11 = Adafruit_DHT.DHT11       #penamaan untuk memanggil data sensor
DHT_PIN = 4                       #penamaan pin input sensor

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_11, DHT_PIN) #membaca data yg diambil oleh sensor

    if humidity is not None and temperature is not None: 
        print("Suhu Ruangan={0:0.1f}*C  Kelembapan={1:0.1f}%".format(humidity, temperature))  #menampilkan data sensor (suhu) dgn format celcius dan (kelembaban) dalam %
    else:
        print("Lost Data")                                                                     #logic jika gagal mendapatkan data sensor
