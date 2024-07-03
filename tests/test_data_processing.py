import pandas as pd
import numpy as np
from src.data_processing import load_data, clean_data, save_data


def test_load_data():
    data = load_data('../data/raw/monthly.csv')
    assert not data.empty, "data shouldn't be empty"


def test_clean_data():
    data = pd.DataFrame({
        'Month Year': ['Jan 2020', 'Feb 2020'],
        'Total Precip (mm)': [10, 20],
        'qc': ['K', 'K']
    })

    cleaned_data = clean_data(data)
    assert 'qc' not in cleaned_data.columns, "column qc should be removed"
    assert not cleaned_data.isnull().values.any(), "data shouldn't have NaN values"


def test_save_data(tmpdir):
    data = pd.DataFrame({
        'Month Year': ['Jan 2020', 'Feb 2020'],
        'Total Precip (mm)': [10, 20],
    })

    sava_path = tmpdir.join("output.csv")
    saved_data = save_data(data, str(sava_path))
    assert sava_path.isfile(), "file should be saved"

    loaded_data = pd.read_csv(str(sava_path))
    pd.testing.assert_frame_equal(data, loaded_data)
