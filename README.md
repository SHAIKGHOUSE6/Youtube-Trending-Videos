# YouTube Trending Data Engineering Project

## Project Overview

This project is an end-to-end Data Engineering and Analytics pipeline built using YouTube Trending Video data collected from the YouTube Data API.

The project extracts trending video data from multiple countries, performs data cleaning and feature engineering, stores the data in PostgreSQL, analyzes it using SQL, builds machine learning models for view prediction, and visualizes insights using Power BI.

---

# Tech Stack

* Python
* Pandas
* YouTube Data API
* PostgreSQL
* SQLAlchemy
* Docker
* Power BI
* Scikit-learn
* Random Forest Regressor

---

# Project Architecture

YouTube API
→ ETL Pipeline
→ CSV Storage
→ PostgreSQL Database
→ SQL Analytics
→ Machine Learning
→ Power BI Dashboard

---

# Features

## Data Extraction

* Extracted trending YouTube videos from multiple countries
* Used YouTube Data API v3
* Automated API requests using Python

## Data Cleaning

* Removed duplicate records
* Fixed CSV corruption issues
* Handled missing values
* Converted ISO duration format into numerical seconds

## Feature Engineering

Created additional features such as:

* Engagement Rate
* Like Rate
* Comment Rate
* Duration Category
* Upload Day
* Upload Time
* Short vs Long Video classification

## SQL Analytics

Performed analytics queries including:

* Top trending channels
* Country-wise trending analysis
* Weekly growth analysis
* Upload timing analysis
* HD vs SD performance
* Global viral video analysis

## Machine Learning

Built ML models to predict video views.

### Models Used

* Linear Regression
* Random Forest Regressor

### Model Performance

* Random Forest R² Score: 0.86
* RMSE: 65602

## Dashboard

Built interactive Power BI dashboards for:

* Country analytics
* Channel performance
* Engagement analysis
* Trend analysis
* ML insights

---

# Dataset Columns

| Column            | Description               |
| ----------------- | ------------------------- |
| Date              | Data collection date      |
| Year              | Collection year           |
| Week              | Collection week           |
| Country           | Trending country          |
| Video_ID          | Unique YouTube video ID   |
| Title             | Video title               |
| Channel           | Channel name              |
| PublishedAt       | Video publish timestamp   |
| Views             | Total views               |
| Likes             | Total likes               |
| Comments          | Total comments            |
| Duration          | Video duration in seconds |
| Definition        | HD/SD                     |
| Caption_Available | Caption availability      |
| Engagement_rate   | Engagement percentage     |
| Uploaded_day      | Upload weekday            |
| Uploaded_time     | Upload hour               |

---

# Project Structure

youtube-trending-project/

├── data/
├── sql/
├── notebooks/
├── dashboard/
├── docker/
├── screenshots/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

---

# Docker Setup

## Pull PostgreSQL Image

```bash
docker pull postgres
```

## Run PostgreSQL Container

```bash
docker run --name postgres-db ^
-e POSTGRES_PASSWORD=1234 ^
-e POSTGRES_USER=postgres ^
-e POSTGRES_DB=youtube_db ^
-p 5432:5432 ^
-d postgres
```

---

# PostgreSQL Connection

```python
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:1234@localhost:5432/youtube_db'
)
```

---

# Load Data into PostgreSQL

```python
df.to_sql(
    'youtube_data',
    engine,
    if_exists='replace',
    index=False
)
```

---

# Sample SQL Questions Solved

* Which country has the most trending videos?
* Which channels dominate multiple countries?
* Which upload day has most trending uploads?
* HD vs SD performance comparison
* Weekly growth analysis
* Top viral videos by engagement

---

# Power BI Dashboard Pages

1. Executive Overview
2. Country Analytics
3. Channel Performance
4. Video Performance
5. Engagement Analysis
6. Weekly Trend Analysis
7. ML Insights

---

# Key Insights

* Certain channels trend globally across multiple countries.
* HD videos generally receive higher engagement.
* Upload timing affects trending probability.
* Short and medium-length videos perform better in engagement.
* Random Forest significantly outperformed Linear Regression.

---

# Future Improvements

* Airflow pipeline automation
* Real-time streaming with Kafka
* Spark-based big data processing
* Cloud deployment using AWS/GCP/Azure
* Streamlit web application

---

# Author

Shaik Mohammed Ghouse

---

# License

This project is for educational and portfolio purposes.
