import pandas as pd
from src.data_processing import load_data, clean_data, save_data
from src.analysis import analyze_precipitation_trends, seasonal_analysis, correlation_analysis, trend_analysis, \
    extreme_precipitation_analysis
from src.visualization import plot_trends, plot_seasonal_precipitation, plot_correlation_matrix, \
    plot_regression_results, plot_extreme_precipitation_analysis


def main():
    raw_data_path = './data/raw/monthly.csv'
    processed_data_path = './data/processed/monthly_cleaned.csv'

    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, processed_data_path)

    data = pd.read_csv(processed_data_path)
    data['Month Year'] = pd.to_datetime(data['Month Year'])

    trends = analyze_precipitation_trends(data)
    seasonal = seasonal_analysis(data)
    corr_matrix = correlation_analysis(data)
    trend_model = trend_analysis(data, 'Total Precip (mm)')
    extremes = extreme_precipitation_analysis(data)

    print("monthly and annual precipitation trends:")
    print(trends)
    print("\nseasonal precipitation analysis:")
    print(seasonal)
    print("\ncorrelation matrix:")
    print(corr_matrix)
    print("\ntrend analysis:")

    print("\ntrend analysis with linear regression:")
    print(trend_model.summary())

    plot_trends(trends)
    plot_seasonal_precipitation(seasonal)
    plot_correlation_matrix(corr_matrix)
    plot_regression_results(trend_model, data)
    plot_extreme_precipitation_analysis(extremes)



if __name__ == '__main__':
    main()
