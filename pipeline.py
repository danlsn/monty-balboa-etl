import csv
import json
import pandas as pd
import requests
from pathlib import Path
from tqdm import tqdm


def download(url):
    print(f'### Downloading {url}')
    response = requests.get(url)
    data = response.json()
    return data


def save_json(data, filename='./data/chumps.json'):
    print(f'### Saving {filename} to JSON')
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    with open(filename, 'w') as f:
        # Save the data to disk
        json.dump(data, f, indent=4)


def json_to_dataframe(data):
    # Convert the JSON data to rows and columns (dataframe)
    print('### Converting JSON to dataframe')
    df = pd.json_normalize(
        data,
        record_path='chumps',
        meta=['date', 'streak', 'date_year', 'date_week', 'thumb']
    )
    return df


def convert_data_types(df):
    # Convert date to datetime
    print('### Converting df[\'date\'] to datetime')
    df['date'] = pd.to_datetime(df['date'])

    # Convert columns to integers
    print('### Converting columns to integers')
    int_columns = ['streak', 'date_year', 'date_week']
    df[int_columns] = df[int_columns].astype(int)

    # Return the transformed dataframe
    return df


def reorder_columns(df, columns):
    # Return the dataframe with the columns in the specified order
    print('### Reordering columns')
    return df[columns]


def download_thumbnails(data, base_url, output='./data'):
    # Create a pretty progress bar to track progress
    print('### Downloading thumbnails')
    data = tqdm(data)

    # For each row in the data, download the thumbnail
    for row in data:
        # Update the progress bar with the current filename
        data.set_description(f'Downloading {row["thumb"]}')

        # Construct url from base_url and thumb value
        url = base_url + row['thumb']

        # Download the image
        response = requests.get(url)

        # Save the image to disk
        filename = Path(f'./{row["thumb"]}')
        filename.parent.mkdir(parents=True, exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(response.content)


def save_to_csv(df, filename='./data/chumps.csv'):
    print(f'### Saving {filename} to CSV')
    # Convert string to Path
    filename = Path(filename)

    # Create the directory if it doesn't exist
    filename.parent.mkdir(parents=True, exist_ok=True)

    # Save the dataframe to CSV
    df.to_csv(filename, index=False, quoting=csv.QUOTE_ALL)


def main():
    # Base URL where the data is located
    base_url = 'https://howmanydayssincemontaguestreetbridgehasbeenhit.com'
    # Download the data at /chumps.json
    data = download(base_url + '/chumps.json')
    # Save the json data to disk
    save_json(data)
    # Convert the JSON to rows and columns in a dataframe
    df = json_to_dataframe(data)
    # Convert the data types
    df = convert_data_types(df)
    # Reorder the columns
    columns = ['date', 'streak', 'date_year', 'date_week', 'name', 'url', 'thumb']
    df = reorder_columns(df, columns)
    # Download the thumbnails
    download_thumbnails(data, base_url)
    # Save the dataframe to CSV
    save_to_csv(df, './data/chumps.csv')


if __name__ == '__main__':
    main()
