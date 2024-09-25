# Environmental Monitoring System

## Overview

The **Environmental Monitoring System** is an IoT-based project designed to measure and analyze key environmental parameters such as temperature, humidity, air quality, and soil moisture. The system integrates Arduino technology, multiple sensors, and cloud services to deliver real-time monitoring, data visualization through a Streamlit web application, and alert functionality.

## Features

- **Real-time Monitoring**: Continuously measures environmental parameters using integrated sensors.
- **Data Visualization**: Displays real-time data via a Streamlit web application for interactive graphical analysis.
- **Cloud Integration**: Utilizes ThingSpeak for remote data access and long-term storage.
- **Alert System**: Triggers alerts when parameters exceed predefined thresholds for proactive monitoring.

## Components

### Hardware

- **Arduino Uno**: Microcontroller for processing sensor data.
- **DHT11 Sensor**: Measures temperature and humidity.
- **MQ135 Sensor**: Detects air quality levels.
- **Soil Moisture Sensor**: Monitors soil moisture content.

### Software

- **Arduino IDE**: Used to write and upload code to the Arduino board.
- **Streamlit**: Web application framework for interactive data visualization.
- **ThingSpeak API**: Facilitates cloud storage and retrieval of environmental data.

## Installation

### Hardware Setup

1. Connect the DHT11, MQ135, and soil moisture sensors to the Arduino Uno.

### Software Setup

1. Install the **Arduino IDE** on your computer.
2. Upload the provided Arduino code to the Arduino Uno board.
3. Set up a **ThingSpeak** account and configure channels for data storage and retrieval.

### Python & Streamlit Environment

1. Install the required Python libraries:

   ```bash
   pip install streamlit matplotlib requests

## Usage

1. Power on the system to begin monitoring environmental parameters.
2. Access real-time data and visualizations through the Streamlit web application.
3. View historical data from ThingSpeak.
4. Receive alerts if any environmental parameter exceeds predefined thresholds.

## Applications

- **Agriculture**: Optimize crop growth conditions by monitoring soil moisture and climate factors.
- **Indoor Air Quality**: Assess air quality in homes or offices to maintain a healthy environment.
- **Industrial Safety**: Ensure safe working conditions by continuously tracking environmental parameters.

## Contributing

Contributions are welcome! If you would like to improve this project, you can:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Open a pull request and describe the changes you’ve made.

If you encounter any issues or have suggestions, feel free to open an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
