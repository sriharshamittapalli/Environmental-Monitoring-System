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
