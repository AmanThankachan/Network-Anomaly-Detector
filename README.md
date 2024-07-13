# Anomaly Detection in Network Traffic

This project implements an anomaly detection system for network traffic using machine learning techniques. It incorporates data preprocessing, model training, CI/CD practices, and monitoring using Prometheus and Grafana.

## Table of Contents

- [Setup](#Setup)
    - [Prerequisites](#Prerequisites)
    - [Dataset](#Dataset)
    - [Steps](#Steps)
- [CI/CD](#CI/CD)
- [Monitoring](#Monitoring)


## Setup

1. **Prerequisites**
    - Python3.6 or higher
    - Docker
    - Jenkins
    - Prometheus
    - Grafana

2. **Dataset**
    - Link to the dataset: https://research.unsw.edu.au/projects/unsw-nb15-dataset
    - Extract the dataset into the data/UNSW-NB15 directory.
    - Merge th dataset by running:
      ```bash
      python data/merge_datasets.py
      ```
      This will create a single network_traffic.csv file in the data directory.

## Steps

1. **Data Preprocessing**
   ```bash
   python src/preprocess_data.py

   ```
   Run the preprocessing script to clean and standardize the data.

2. **Model Training**
   ```bash
   python src/train_model.py

   ```
   Train the anomaly detection model using the preprocessed data.

3. **Testing**
   ```bash
   python src/test_model.py

   ```
   Evaluate the trained model's performance.

4. **Build and Run Docker Container**
   
   Build the Docker image for the Flask application and run the container:
   ```bash
   docker build -t anomaly-detection src/.
   docker run -d -p 5000:5000 anomaly-detection
   ```

6. **Set Up CI/CD Pipeline with Jenkins**
   
   Configure Jenkins pipeline to use the Jenkinsfile located in the src/jenkins/ directory.   

## CI/CD
The project includes a Jenkins pipeline defined in the Jenkinsfile, which automates the following stages:
  -  Data preprocessing
  -  Model training
  -  Model testing
  -  Docker image build
  -  Deployment of the Docker container 


## Monitoring

1. **Download and Install Prometheus:**

   Download Prometheus from https://prometheus.io/download/
   
2. **Configure Prometheus:**
   
   Navigate to the Prometheus directory and copy prometheus.yaml from this repository.
   
4. **Start Prometheus:**
   ```bash
   ./prometheus --config.file=prometheus.yml
   ``` 
5. **Grafana**
   
    Set up Grafana to visualize these metrics using the provided dashboard configuration.
