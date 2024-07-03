import pandas as pd
import numpy as np
import statsmodels.api as sm


def analyze_precipitation_trends(data):
    """generates monthly and annual trends, by calculating mean"""
    monthly_trends = data.groupby(data['Month Year'].dt.to_period('M'))['Total Precip (mm)'].mean()
    annual_trends = data.groupby(data['Month Year'].dt.to_period('Y'))['Total Precip (mm)'].mean()
    return monthly_trends, annual_trends


def seasonal_analysis(data):
    """generates seasonal map, by calculating mean of months"""
    if data['Month Year'].dtype != 'datetime64[ns]':
        data['Month Year'] = pd.to_datetime(data['Month Year'])

    data['Month'] = data['Month Year'].dt.month
    seasonal_mapping = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
                        8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'}
    data['Season'] = data['Month'].map(seasonal_mapping)
    seasonal_precip = data.groupby('Season')['Total Precip (mm)'].mean()
    return seasonal_precip


def correlation_analysis(data):
    """generates correlation matrix between precipitation trends."""
    numeric_data = data.select_dtypes(include=[np.number])

    correlation_matrix = numeric_data.corr()
    return correlation_matrix


def trend_analysis(data, column_name):
    """analysis of precipitation trends using linear regression."""
    if data['Month Year'].dtype != 'datetime64[ns]':
        data['Month Year'] = pd.to_datetime(data['Month Year'])

    data['Month'] = data['Month Year'].dt.month
    data['Season'] = data['Month'] % 12 // 3 + 1
    data['TimeIndex'] = np.arange(len(data))

    data['LogTimeIndex'] = np.log1p(data['TimeIndex'])

    x = sm.add_constant(data[['LogTimeIndex', 'Season']])
    y = data[column_name]

    model = sm.OLS(y, x, missing='drop').fit()
    # print(model.summary())
    return model


def extreme_precipitation_analysis(data):
    data['Year'] = data['Month Year'].dt.year
    extremes = data.groupby('Year')['Total Precip (mm)'].agg(['max', 'min'])
    return extremes


if __name__ == '__main__':
    data = pd.read_csv('../data/processed/monthly_cleaned.csv')
    data['Month Year'] = pd.to_datetime(data['Month Year'])

    trends = analyze_precipitation_trends(data)
    seasonal = seasonal_analysis(data)
    corr_matrix = correlation_analysis(data)
    trend_model = trend_analysis(data, 'Total Precip (mm)')
    extreme_precip = extreme_precipitation_analysis(data)
    # print(extreme_precip)
