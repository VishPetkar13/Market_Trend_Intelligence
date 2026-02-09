import yfinance as yf
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

def fetch_price_data(
        ticker: str,
        start_date: str,
        end_date: str
) -> pd.DataFrame:
    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False
    )
    df.reset_index(inplace=True)
    df["Ticker"] = ticker

    return df

def save_raw_data(df: pd.DataFrame, ticker: str) -> None:
    """
    Save raw market data to CSV.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_path = DATA_DIR / f"{ticker}_prices.csv"
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    tickers = ["SPY", "QQQ", "XLK", "XLF"]
    start = "2018-01-01"
    end = "2026-01-01"

    for ticker in tickers:
        data = fetch_price_data(ticker, start, end)
        save_raw_data(data, ticker)
        print(f"Saved raw data for {ticker}")    