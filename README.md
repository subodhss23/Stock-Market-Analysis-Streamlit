# Stock-Market-Analysis-Streamlit



**Stock-Market-Analysis-Streamlit** is a Python application that leverages Streamlit to provide interactive visualizations and insights into stock market data. Utilizing the Alpaca API, this app fetches and displays data on top active stocks by volume and top market movers, including gainers and losers.

## Features

- **Top Active Stocks by Volume:** Displays the top 10 stocks with the highest trading volume. Visualizes this data using bar charts to show both trade count and volume.
- **Top Market Movers:** Provides insights into the top 10 market movers, separating them into gainers and losers. Displays this information in tabular format.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Stock-Market-Analysis-Streamlit.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Stock-Market-Analysis-Streamlit
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `config.py` file:** 
   Ensure you have a `config.py` file in the project directory with your Alpaca API credentials:
   ```python
   API_KEY = 'your_alpaca_api_key'
   SECRET_KEY = 'your_alpaca_secret_key'
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Navigate to the local server URL:** The app will be available at `http://localhost:8501` or the URL provided in the terminal.

## Code Overview

- **`app.py`:** The main script that contains the `TradingClass` which interacts with the Alpaca API to fetch stock data and visualize it using Streamlit.
  - `scan_for_most_active_stocks()`: Retrieves and displays the top 10 stocks by volume.
  - `scan_for_top_market_mover_stocks()`: Retrieves and displays top market movers categorized into gainers and losers.

## Requirements

- **Python 3.x**
- **requests**
- **streamlit**
- **pandas**
- **matplotlib**

## Notes

- Ensure your Alpaca API credentials are correctly set in `config.py`.
- This app is intended for educational and demonstration purposes.

## License

This project is licensed under the MIT License.


