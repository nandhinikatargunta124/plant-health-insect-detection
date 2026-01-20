def etl_process(sensor_data):
    cleaned_data = {}

    for key, value in sensor_data.items():
        if value >= 0:
            cleaned_data[key] = value

    return cleaned_data


def analyze_plant_health(data):
    alerts = []

    if data["soil_moisture"] < 30:
        alerts.append("⚠️ Plant stress detected: Low soil moisture")

    if data["humidity"] > 70 and data["temperature"] > 35:
        alerts.append("🐛 Possible insect activity detected")

    return alerts


# Sample sensor data
sample_data = {
    "temperature": 38,
    "humidity": 75,
    "soil_moisture": 25
}

clean_data = etl_process(sample_data)
alerts = analyze_plant_health(clean_data)

print("Cleaned Data:", clean_data)
for alert in alerts:
    print(alert)
