A Cloud-Based Weather Temperature Analysis System

Student Name :Dina Khadka
Github  Repo:- https://github.com/dina937/A-Cloud-Based-Weather-Temperature-Analysis-System

Project Description

This project demonstrates a cloud-native architecture for analyzing historical temperature data stored in CSV format and generating basic temperature predictions. The system uses Python, FastAPI, containerization, and Kubernetes deployment. It is designed to implement core cloud-computing and software architecture concepts including data ingestion, feature engineering, prediction logic, API exposure, and CI/CD readiness.
•	Architecture:- Data Ingest → Cloud Storage → Data Processing → Simple Prediction Logic → REST API.

•	 ADRs:- Use of a simple cloud architecture and lightweight prediction models (station mean and station-hour mean) for clarity and low computational cost.

•	CI/CD:- Basic data validation, simple testing of prediction logic, and container build using version control workflows.

•	Sustainability:
Low-energy computation using simple models, on-demand execution, and CPU-only processing.

•	Carbon-aware behavior (conceptual):High load: use simpler prediction logic.Normal load: use station-hour mean for better accuracy.

•	
•	Simulation & Monitoring:-Simulated system load changes with tracking of prediction error and basic system metrics.

Summary
This project implements a simple, cloud-based weather temperature analysis system using historical data from weather stations. The system is designed to demonstrate cloud-native architecture principles. A basic Data Ingest component loads weather data from a CSV file and stores it in cloud object storage. A Data Processing module prepares station-wise and time-based features, and a Prediction component applies simple statistical models such as station-mean and station-hour-mean temperature estimation.
A single REST API (implemented using FastAPI) exposes temperature analysis results and basic system status to users. The architecture avoids complex machine learning models and instead focuses on clarity, modularity, and low computational cost. Different prediction modes can be conceptually selected to balance accuracy and resource usage, demonstrating efficient system behavior.
The system uses lightweight cloud components such as object storage, on-demand compute, and basic monitoring. A simple CI/CD workflow validates data format, checks code correctness, and prepares the system for deployment. Overall, the project demonstrates how a well-structured cloud architecture can support data analysis tasks efficiently, sustainably, and in an easy-to-explain manner.

1.	Component Diagram:



1. External Weather Data (CSV Dataset)
•	Inputs: Historical weather temperature data in CSV format
•	Processes: Serves as the raw temperature data source
•	Outputs: Data is provided to the Data Ingest Service

2. Data Ingest Service
•	Inputs: External weather temperature dataset (CSV)
•	Processes: Loads and validates weather data
•	Outputs: Stores cleaned data in Cloud Object Storage

3. Feature Engineering Service
•	Inputs: Data from Cloud Object Storage
•	Processes: Station-based and hour-based feature extraction
•	Outputs: Prepared feature data for prediction

4. Prediction Engine
•	Inputs: Feature data
•	Sub-components:
o	Station Mean Model
o	Station-Hour Mean Model
•	Outputs: Predicted temperature values

5. REST API (FastAPI)
•	Interfaces:
o	analyze → returns temperature analysis
o	status → returns system status
•	Consumers: Browser-based client or dashboard

6. User / Client
•	Inputs: REST API responses
•	Displays: Temperature analysis results

7. CI/CD Pipeline
•	Stages:
o	Code checks
o	Data format validation
o	Build and deployment
•	Tools: GitHub Actions (conceptual)

8. Cloud Infrastructure
•	Components:
o	Cloud Object Storage (e.g., S3-compatible)
o	Containerized application (conceptual)
o	Basic monitoring

Core Development Tools
•	Language: Python 3
•	Libraries: Pandas, NumPy

API & Application Layer
•	Framework: FastAPI
•	Server: Uvicorn

Documentation & Diagrams
•	Markdown
•	Draw.io

Simulation
●	Python script for carbon-intensity simulation
●	Simple scheduler/loop (cron or Python)

2.	UseCase Diagram
 

●	•  Shows how the user interacts with the system.
●	•  Identifies the main actor: User.
●	•  Displays three primary system functions:
1️⃣ Load weather data
2️⃣ Analyze temperature
3️⃣ Check system status
●	•  Helps define system behaviour based on user goals.
●	•  Focuses on what the system does, not how it is built.
●	•  Used during requirement analysis to confirm user expectations.
●	•  Makes functionality easy to understand for both developers and reviewers
3.	Class Diagram




1. APIController Class
•	Acts as the entry point for user interactions.
•	Contains public methods:
✔ analyze_request()
✔ load_data_request()
✔ status_request()
•	Dispatches incoming API calls to other system components.
•	Connects directly to:
→ DataIngest
→ Feature Engineering

 2. DataIngest Class
•	Responsible for loading and validating the CSV dataset.
•	Attributes:
✔ csv_path — input dataset location
✔ raw_data — stored data object
•	Feeds cleaned data into Feature Engineering and Predictor.
•	Ensures the entire system starts with correct data.

 3. Feature Engineering Class
•	Generates processed data features for prediction.
•	Attributes:
✔ engineered_data — transformed dataset
•	Methods:
✔ apply_station_features()
✔ apply_hour_features()
✔ return_features()
•	Converts raw dataset into structured input for predictive models.

 4. Predictor Class
•	Executes temperature prediction using two model types:
✔ Full model
✔ Low-power model
•	Methods include:
✔ run_full_model()
✔ run_low_power_model()
✔ return_prediction()
•	Receives input from Feature Engineering and returns final temperature output.
 5. CarbonMonitor Class
•	Monitors carbon intensity for sustainability decisions.
•	Attributes:
✔ carbon_intensity
✔ threshold
•	Methods:
✔ check_intensity()
✔ choose_model()
•	Sends feedback signals to Predictor for model selection.

 6. Relationships Between Classes
•	APIController communicates with DataIngest and Feature Engineering.
•	DataIngest and Feature Engineering feed into Predictor.
•	Predictor receives carbon intensity data from CarbonMonitor.
•	Predictor returns predictions back to APIController.
•	The diagram shows a clear top-down system workflow.

4.	Sequence Diagrams
 

1.User Interaction
•	The workflow starts when the User sends an /analyze request.
•	The request is received and handled by the APIController
2 Data Loading
•	The APIController asks DataIngest to load the dataset.
DataIngest does three tasks:
1.	Reads the CSV file
2.	Checks if the data format and values are correct
3.	Sends cleaned data back
3. Feature Engineering (Make data ready for prediction)
•	The APIController passes the cleaned data to FeatureEngineer.
FeatureEngineer performs two types of processing:
1.	Station-based features
→ Information grouped by weather station
2.	Hour-based features
→ Information grouped by hour of the day
•	After processing, FeatureEngineer returns a set of engineered features to the APIController.
4. Carbon Intensity Check
•	The APIController asks the CarbonMonitor to check current carbon intensity.
CarbonMonitor actions:
1.	Calculates the carbon level
2.	Compares the value to a threshold
3.	Decides which prediction model to use
5 Prediction Execution
•	The APIController now requests prediction from the Predictor.
Predictor chooses between two models:
1.	Runs full model → if carbon intensity is LOW
2.	Runs low-power model → if carbon intensity is HIGH
•	Finally, Predictor sends back predicted temperature values.


6 Response to User
•	APIController formats the prediction into a JSON output.
•	The result is sent back to the User

5.	Deployment Diagram

✨ 












The deployment diagram shows how the system is installed and executed on the local machine. The FastAPI application, prediction engine, and feature engineering components run inside a Docker container, ensuring consistency and portability across environments. The system reads weather dataset files stored locally in CSV format and processes them inside the container. This setup demonstrates how the application can function independently on a single device without cloud dependency, while still following a cloud-native structure.


 Application Scaffolding:-
A Cloud-Based Weather Temperature Analysis System
├── data/
│   ├── input/
│   │   └── WeatherData.csv
│   └── output/
│       └── results.json
│
├── src/
│   ├── ingest.py
│   ├── process.py
│   ├── predict.py
│   └── main.py
│
├── docs/
│   ├── component_diagram.drawio
│   ├── class_diagram.drawio
│   ├── sequence_diagram.drawio
│   └── deployment_diagram.drawio
│
├── kubernetes/
│   ├── Deployment.yaml
│   └── Service.yaml
│
├── requirements.txt
├── README.md
└── .gitignore
