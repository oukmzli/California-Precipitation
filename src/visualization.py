import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(trends):
    """plot monthly and annual precipitation trends."""
    fig, ax = plt.subplots(2,1, figsize=(12,10))
    trends[0].plot(ax=ax[0], title='monthly precipitation trends')
    trends[1].plot(ax=ax[1], title='annual precipitation trends')
    ax[0].set_ylabel('precipitation (mm)')
    ax[1].set_ylabel('precipitation (mm)')
    plt.tight_layout()
    plt.show()

def plot_seasonal_precipitation(seasonal):
    """plot precipitation by season."""
    plt.figure(figsize=(8,6))
    seasonal.plot(kind='bar', color='skyblue')
    plt.title('average precipitation by season')
    plt.xlabel('season')
    plt.ylabel('average precipitation (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(corr_matrix):
    """plot correlation matrix."""
    plt.figure(figsize=(15, 13))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', annot_kws={"size": 12})
    plt.title('correlation Matrix')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

def plot_regression_results(model, data):
    """plot regression analysis results."""
    plt.figure(figsize=(10,6))
    plt.scatter(data['TimeIndex'], data['Total Precip (mm)'], alpha=0.5, label='data')
    plt.plot(data['TimeIndex'], model.fittedvalues, color='red', alpha=0.5, label='fitted line')
    plt.title('trend analysis with linear regression')
    plt.xlabel('time index')
    plt.ylabel('total precip (mm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_extreme_precipitation_analysis(extremes):
    plt.figure(figsize=(12, 6))
    extremes['max'].plot(label='max Precipitation')
    extremes['min'].plot(label='min Precipitation')
    plt.title('extreme precipitation analysis by year')
    plt.xlabel('year')
    plt.ylabel('precipitation (mm)')
    plt.legend()
    plt.show()