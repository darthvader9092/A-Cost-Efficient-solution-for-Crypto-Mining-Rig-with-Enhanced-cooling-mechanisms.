import adafruit_dht
from RPLCD.i2c import CharLCD
import board
import time
from pushbullet import Pushbullet

# Initialize LCD using I2C address 0x3F (adjust as needed)
lcd = CharLCD('PCF8574', 0x3f, cols=16, rows=2)

# Define DHT11 sensor type and GPIO pin
dht_device = adafruit_dht.DHT11(board.D4)

# Replace with your Pushbullet Access Token
API_KEY = 'o.3m149zzLHRihRXLXnPnpgIvxWOTQ17du'
pb = Pushbullet(API_KEY)

try:
    while True:
        # Attempt to read sensor data
        humidity = None
        temperature = None
        while humidity is None or temperature is None:
            try:
                humidity = dht_device.humidity
                temperature = dht_device.temperature
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue

        # Print data to console
        print(f'Temperature: {temperature:.1f} °C | Humidity: {humidity:.1f} %')

        # Display data on LCD
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f'Temp: {temperature:.1f} C')
        lcd.cursor_pos = (1, 0)
        lcd.write_string(f'Humidity: {humidity:.1f} %')

        # Check if temperature exceeds 30°C
        if temperature > 33:
            pb.push_note("Temperature Alert", f"Temperature has exceeded 30°C! Current temperature: {temperature:.1f}°C Please do consider mining at High Temperatures")

        # Wait 2 seconds before reading again
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    lcd.clear()
