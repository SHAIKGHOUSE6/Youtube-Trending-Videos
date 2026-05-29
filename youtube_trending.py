from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
import os
import csv

api_key = 'AIzaSyD9mhONUr4t8CuJl0uA1pXv-rLCvz0Fa4g'


youtube = build('youtube', 'v3', developerKey=api_key)

countries = {
    'India': 'IN',
    'US': 'US',
    'UK': 'GB',
    'Canada': 'CA',
    'Australia': 'AU',
    'Germany': 'DE',
    'France': 'FR',
    'Brazil': 'BR',
    'Japan': 'JP',
    'South Korea': 'KR',
    'Mexico': 'MX',
    'Pakistan': 'PK'
}


all_data = []

today = datetime.now()

date = today.strftime('%Y-%m-%d')
week_number = today.strftime('%U')
year = today.strftime('%Y')


for country_name, country_code in countries.items():

    try:

        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            chart='mostPopular',
            regionCode=country_code,
            maxResults=50
        )

        response = request.execute()

        for item in response['items']:

          
            views = int(item['statistics'].get('viewCount', 0))
            likes = int(item['statistics'].get('likeCount', 0))
            comments = int(item['statistics'].get('commentCount', 0))

            title = item['snippet']['title']
            title = title.replace('\n', ' ').replace('\r', ' ')

            channel = item['snippet']['channelTitle']
            channel = channel.replace('\n', ' ').replace('\r', ' ')

    
            all_data.append({

                'Date': date,
                'Year': year,
                'Week': week_number,

                'Country': country_name,

                'Video_ID': item['id'],

                'Title': title,

                'Channel': channel,

                'PublishedAt': item['snippet']['publishedAt'],

                'Views': views,
                'Likes': likes,
                'Comments': comments,

                'Duration': item['contentDetails'].get('duration'),

                'Definition': item['contentDetails'].get('definition'),

                'Caption_Available': item['contentDetails'].get('caption')

            })

        print(f"Fetched Successfully: {country_name}")

    except Exception as e:

        print(f"Error in {country_name}: {e}")


df = pd.DataFrame(all_data)


df = df.drop_duplicates()


file_name = 'youtube_trending_data.csv'


if os.path.exists(file_name):

    df.to_csv(
        file_name,
        mode='a',
        header=False,
        index=False,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )

else:

    df.to_csv(
        file_name,
        index=False,
        encoding='utf-8',
        quoting=csv.QUOTE_ALL
    )


print("ETL Pipeline Completed Successfully!")

print(df.shape)

print(df.head())


# Load the cleaned data into PostgreSQL database

from sqlalchemy import create_engine

df = pd.read_csv('youtube_trending_cleaned_data.csv')

engine = create_engine(
    'postgresql://postgres:123456789990@localhost:5432/shaik_db'
)

df.to_sql(
    'youtube_data',
    engine,
    if_exists='replace',
    index=False
)

print("Loaded Successfully!")