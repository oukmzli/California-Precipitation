# AirQuality-NYC
 NYC Air quality analyzer 

AirQuality-NYC is a pet-project designed to analyze the air quality in New York City (or any other city, depending on data you want to use!). 

## Structure of project:

AirQualNYC/
│
├── data/                   # Data directory
│   ├── raw/                    # raw data
│   └── processed/              # processed data
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── exploration.ipynb       # preanalizing data
│   └── visualization.ipynb     # visualising data
│
├── src/                    # Source of a project
│   ├── __init__.py             # pyrhon module
│   ├── data_processing.py      # data processing module
│   ├── analysis.py             # data analysis module
│   └── visualization.py        # data visualization module
│
├── tests/                  # Tests
│   ├── __init__.py
│   └── test_data_processing.py
│
├── requirements.txt
├── .gitignore
└── README.md


## Getting Started

1. Clone the repository:
    ```bash
   git clone https://github.com/yourusername/AirQuality-NYC.git
   ```
2. Navigate to the project directory:
    ```bash
   cd AirQuality-NYC
   ```
3. Install the dependencies:
    ```bash
   pip install -r requirements.txt
   ```
   -- **OR**
    ```bash
   pip3 install -r requirements.txt  #for several systems
4. Launch Jupyter Notebook to explore the data:
    ```
    ```bash
   jupyter notebook
   ```
