import random
import time

def get_sensor_data():
    data = {
        "temperature": random.randint(20, 45),
        "humidity": random.randint(30, 90),
        "soil_moisture": random.randint(10, 80)
    }
    return data

for i in range(5):
    sensor_data = get_sensor_data()
    print("Sensor Data:", sensor_data)
    time.sleep(2)
