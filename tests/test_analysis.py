import pandas as pd
from src.analysis import analyze_precipitation_trends, seasonal_analysis


def test_analyze_precipitation_trends():
    data = pd.DataFrame({
        'Month Year': pd.to_datetime(['2020-01', '2020-02', '2020-03', '2020-04']),
        'Total Precip (mm)': [5, 10, 15, 20]
    })

    monthly_trends, annual_trends = analyze_precipitation_trends(data)
    assert monthly_trends.loc['2020-01'] == 5
    assert annual_trends.loc['2020'] == 12.5


def test_seasonal_analysis():
    data = pd.DataFrame({
        'Month Year': pd.to_datetime(['2020-01', '2020-04', '2020-07', '2020-10']),
        'Total Precip (mm)': [10, 20, 30, 40]
    })

    results = seasonal_analysis(data)
    expected_seasons = {'Winter': 10, 'Spring': 20, 'Summer': 30, 'Fall': 40}

    for season, value in results.items():
        assert value == expected_seasons[season]
