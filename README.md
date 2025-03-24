# S4Project
# Car Listings Dashboard

An interactive Streamlit web app to explore and visualize car listings data from the US.

## Features

- Histogram of car prices
- Scatter plots of price vs. year and odometer
- Toggle to exclude listings with price = 0

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly Express

## How to Run Locally

1. Clone the repository:
git clone https://github.com/joshuaferreira327/S4Project.git cd S4Project
2. Create and activate a virtual environment:
python -m venv venv source venv/bin/activate # On Windows use: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the app:
streamlit run app.py
## Data Source
Dataset: `vehicles_us.csv` — a dataset of car listings in the US.