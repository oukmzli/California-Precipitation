import pandas as pd


def load_data(filepath):
    return pd.read_csv(filepath)


def clean_data(data):
    data = data.drop(columns=[col for col in data.columns if 'qc' in col])
    data['Month Year'] = pd.to_datetime(data['Month Year'], format='%b %Y')
    for col in data.columns:
        if data[col].dtype == 'float64':
            data[col] = data[col].fillna(data[col].median())
    return data


def save_data(data, output_path):
    data.to_csv(output_path, index=False)
    return data


if __name__ == '__main__':
    raw_data_path = '../data/raw/monthly.csv'
    processed_data_path = '../data/processed/monthly_cleaned.csv'

    data = load_data(raw_data_path)
    clean_data = clean_data(data)
    save_data(clean_data, processed_data_path)
