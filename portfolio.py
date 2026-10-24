"""Sample-data portfolio tracker. Run: python portfolio.py"""
import csv
from datetime import datetime
from pathlib import Path

PRICE_FILE = Path(__file__).with_name("sample_prices.csv")
OUTPUT_FILE = Path(__file__).with_name("portfolio_summary.csv")

def load_prices(path=PRICE_FILE):
    """Load ticker/current-price pairs from CSV."""
    prices = {}
    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not {"ticker", "current_price"}.issubset(reader.fieldnames):
                raise ValueError("Price CSV must have ticker,current_price columns.")
            for row in reader:
                ticker = row["ticker"].strip().upper()
                try:
                    price = float(row["current_price"])
                except (TypeError, ValueError):
                    continue
                if ticker and price >= 0:
                    prices[ticker] = price
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find {path.name}. Keep it beside portfolio.py.")
    return prices

def get_positive_number(prompt, allow_zero=False):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < 0 or (value == 0 and not allow_zero):
                print("Enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a number, such as 125.50.")

def get_portfolio(prices):
    holdings = []
    print("\nEnter holdings. Available sample tickers:", ", ".join(sorted(prices)))
    print("Type DONE as ticker when finished.")
    while True:
        ticker = input("\nTicker: ").strip().upper()
        if ticker == "DONE":
            break
        if not ticker:
            print("Ticker cannot be empty.")
            continue
        if ticker not in prices:
            print("Ticker not found in sample_prices.csv. Choose one of the listed tickers.")
            continue
        buy_price = get_positive_number("Buy price per share: ")
        quantity = get_positive_number("Number of shares: ")
        if not quantity.is_integer():
            print("For this beginner version, share quantity must be a whole number.")
            continue
        holdings.append({
            "ticker": ticker,
            "buy_price": buy_price,
            "quantity": int(quantity),
            "current_price": prices[ticker],
        })
    return holdings

def summarize(holdings):
    rows = []
    for item in holdings:
        invested = item["buy_price"] * item["quantity"]
        market_value = item["current_price"] * item["quantity"]
        gain_loss = market_value - invested
        percent = (gain_loss / invested * 100) if invested else 0.0
        rows.append({
            **item,
            "invested": invested,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": percent,
        })
    return rows

def save_summary(rows, path=OUTPUT_FILE):
    fields = [
        "timestamp", "ticker", "buy_price", "current_price", "quantity",
        "invested", "market_value", "gain_loss", "gain_loss_percent"
    ]
    timestamp = datetime.now().isoformat(timespec="seconds")
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for row in rows:
                writer.writerow({"timestamp": timestamp, **row})
    except OSError as exc:
        print(f"Could not write CSV report: {exc}")
        return False
    return True

def main():
    try:
        prices = load_prices()
    except (OSError, ValueError) as exc:
        print("Could not load sample prices:", exc)
        return
    holdings = get_portfolio(prices)
    if not holdings:
        print("No holdings entered. Nothing to report.")
        return
    rows = summarize(holdings)
    print("\n=== PORTFOLIO SUMMARY ===")
    print(f"{'Ticker':<10}{'Qty':>6}{'Invested':>14}{'Market Value':>16}{'Gain/Loss':>14}{'Gain/Loss %':>14}")
    for row in rows:
        print(f"{row['ticker']:<10}{row['quantity']:>6}{row['invested']:>14.2f}{row['market_value']:>16.2f}{row['gain_loss']:>14.2f}{row['gain_loss_percent']:>13.2f}%")
    total_invested = sum(r["invested"] for r in rows)
    total_value = sum(r["market_value"] for r in rows)
    total_gain = total_value - total_invested
    total_pct = total_gain / total_invested * 100 if total_invested else 0
    print("-" * 74)
    print(f"Total invested: {total_invested:.2f}")
    print(f"Current value:  {total_value:.2f}")
    print(f"Total gain/loss:{total_gain: .2f} ({total_pct:.2f}%)")
    if save_summary(rows):
        print(f"\nCSV report saved to: {OUTPUT_FILE.name}")

if __name__ == "__main__":
    main()
