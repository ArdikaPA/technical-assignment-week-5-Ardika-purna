#install in terminall
$ sudo apt-get install git-core
$ sudo pip3 install Adafruit_DHT
$ cd Adafruit_Python_DHT
$ sudo python3 setup.py install
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
  
#for call sensor in logic
import Adafruit_DHT

DHT_11 = Adafruit_DHT.DHT_11
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_11,DHT_PIN)
