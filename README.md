# A Cost-Efficient Solution for Crypto Mining Rig with Enhanced Cooling Mechanisms

## Authors
- Abbaraju Sree Tharun Raju (am.en.u4aie22001@am.students.amrita.edu)
- Nikhil Chandran (am.en.u4aie22035@am.students.amrita.edu)
- Jayant Sasikumar (am.en.u4aie22059@am.students.amrita.edu)
- Vighnesh S R (am.en.u4aie22056@am.students.amrita.edu)

## Institution
Department of Computer Science and Engineering, Amrita Vishwa Vidyapeetham, Amritapuri, India

## Abstract
This project proposes a cost-efficient IoT-enhanced solution for cryptocurrency mining using a Raspberry Pi 4 and a DHT11 sensor for thermal management. The objective is to optimize the thermal performance of the mining rig to ensure continuous and efficient mining operations. By incorporating real-time temperature and humidity monitoring, the system maintains optimal operating conditions, thereby enhancing the efficiency and reliability of the mining process.

## Introduction
Cryptocurrency mining is a computationally intensive process that generates significant heat. Efficient thermal management is crucial for continuous mining operations. This project utilizes IoT technology to improve the cost-effectiveness and productivity of cryptocurrency mining through a Raspberry Pi 4 and DHT11 sensor setup.

## System Architecture
The system architecture includes:
- **Raspberry Pi 4**: Acts as the main computing device for mining operations.
- **DHT11 Sensor**: Monitors temperature and humidity for thermal management.
- **LCD Display**: Continuously displays the temperature readings.
- **Computer Cooling Fan**: Provides necessary cooling based on sensor data.
- **Pushbullet**: Sends real-time alerts when temperature thresholds are exceeded.

## Methodology
The project involves setting up a Raspberry Pi 4 with a DHT11 sensor to monitor environmental conditions continuously. The data is processed to regulate cooling mechanisms effectively, ensuring the mining hardware operates efficiently. The mining is performed using XMRig software targeting Monero cryptocurrency, chosen for its resistance to ASIC mining.

### Temperature Monitoring Script
The `temperature_control_message.py` script performs the following functions:
- Initializes the DHT11 sensor and LCD display.
- Reads temperature and humidity data from the sensor.
- Displays temperature and humidity on the LCD.
- Sends a Pushbullet notification if the temperature exceeds 33°C, alerting users to potential overheating issues.

```python
# Sample code snippet from temperature_control_message.py
# Initialize DHT11 sensor and LCD
dht_device = adafruit_dht.DHT11(board.D4)
lcd = CharLCD('PCF8574', 0x3f, cols=16, rows=2)

# Main loop to read sensor data and display on LCD
while True:
    humidity = dht_device.humidity
    temperature = dht_device.temperature
    lcd.write_string(f'Temp: {temperature:.1f} C')
    if temperature > 33:
        pb.push_note("Temperature Alert", f"Temperature has exceeded 33°C! Current temperature: {temperature:.1f}°C")
    time.sleep(2)
