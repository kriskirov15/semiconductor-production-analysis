# semiconductor-production-analysis
This project is a course project for the subject "Python Basics" at Sofia University, Faculty of Physics.


## Description

This project analyzes and visualizes semiconductor production data for companies like GlobalFoundries using Python. 
The project demonstrates data reading, processing, visualization, and statistical analysis using various Python libraries such as pandas, numpy, and plotly.


## Features

- **Data Reading and Processing**:
  - Reads data from a CSV file.
  - Processes the data to calculate total and defective chips and their percentages.
  - Groups data by date and other factors such as wafer size, shift, and machine ID.
  
- **Data Visualization**:
  - Creates interactive line and bar graphs using Plotly to visualize production data.
  
- **Statistical Analysis**:
  - Calculates mean and standard deviation of produced chips.
  - Analyzes and prints dates with high defective chip percentages.
  - Performs additional analyses on wafer size, shifts, and machines.
  
- **Error Handling**:
  - Robust error handling for file operations.

## Requirements

- Python 3.12
- pandas
- numpy
- plotly

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/YOUR_USERNAME/semiconductor-production-analysis.git
    cd semiconductor-production-analysis
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install pandas numpy plotly
    ```

4. Place the `semiconductor_production.csv` file in the project directory.

## Usage

Run the analysis script:
```sh
python analysis.py
