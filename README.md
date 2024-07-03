# California-Precipitation
 California-Precipitation analyzer 

Based on CIMIS Station Reports.
California-Precipitation is a pet-project designed to analyze the Precipitation in state of California. 

## Structure of project:

```
California-Precipitation/ 
│
├── data/                   # Data directory
│   ├── raw/                    # raw data
│   │   └── monthly.csv          # monthly precipitation
│   │
│   └── processed/              # processed data
│       └── monthly_cleaned.csv  # cleaned data 
│               
│
├── notebooks/              # Jupyter notebook for exploration
│   ├── test.ipynb              # test of jupyter notebook
│   └── visualization.ipynb     # visualising data
│
├── src/                    # Source of a project
│   ├── __init__.py             # python module
│   ├── data_processing.py      # data processing module
│   ├── analysis.py             # data analysis module
│   └── visualization.py        # data visualization module
│
├── tests/                  # Tests
│   ├── __init__.py
│   ├── import_tests.py
│   ├── test_analysis.py
│   └── test_data_processing.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

1. Clone the repository:
    ```bash
   git clone https://github.com/oukmzli/California-Precipitation.git
   ```
2. Navigate to the project directory:
    ```bash
   cd California-Precipitation
   ```
3. Install the dependencies:
    ```bash
   pip install -r requirements.txt
   ```
   -- **OR** --
    ```bash
   pip3 install -r requirements.txt  #for several systems
   ```
4. Launch Jupyter Notebook to explore the data:
    ```bash
   jupyter notebook
   ```
