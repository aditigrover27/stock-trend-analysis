import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA CONFIGURATION & DOWNLOADING
# ==========================================
# NSE Tickers for Reliance, TCS, and HDFC Bank
tickers = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
start_date = "2021-01-01"
end_date = "2025-12-31"

print("Downloading stock data from Yahoo Finance...")
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Fill any missing trading days
data = data.ffill().dropna()

# ==========================================
# 2. FINANCIAL CALCULATIONS & METRICS
# ==========================================
# Daily percentage returns
daily_returns = data.pct_change().dropna()

# Cumulative returns rebased to 100 (for equal-scale comparison)
normalized_data = (data / data.iloc[0]) * 100

# 50-Day and 200-Day Simple Moving Averages (SMA) for Reliance
reliance_close = data["RELIANCE.NS"]
sma_50 = reliance_close.rolling(window=50).mean()
sma_200 = reliance_close.rolling(window=200).mean()

# Annualized Performance Metrics (Assuming 252 trading days per year)
annual_returns = daily_returns.mean() * 252
annual_volatility = daily_returns.std() * np.sqrt(252)

# Create a Summary DataFrame
performance_summary = pd.DataFrame({
    "Annualized Return": annual_returns,
    "Annualized Volatility (Risk)": annual_volatility,
    "Sharpe Ratio (Rf=0.06)": (annual_returns - 0.06) / annual_volatility
})

print("\n--- PERFORMANCE SUMMARY ---")
print(performance_summary.round(4))

# ==========================================
# 3. VISUALIZATION DASHBOARD
# ==========================================
# Set custom styling
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "Arial"

# Chart 1: Normalized Cumulative Growth (Rebased to 100)
plt.figure(figsize=(12, 6))
for column in normalized_data.columns:
    plt.plot(normalized_data.index, normalized_data[column], label=column.replace(".NS", ""), linewidth=2)
plt.title("Normalized Price Performance (Base = 100)", fontsize=14, fontweight="bold")
plt.xlabel("Date", fontsize=11)
plt.ylabel("Index Value (₹100 Initial Investment)", fontsize=11)
plt.legend(frameon=True, facecolor="white")
plt.tight_layout()
plt.savefig("1_normalized_growth.png", dpi=300, bbox_inches="tight")
plt.show()

# Chart 2: Trend Analysis - Reliance 50-Day vs 200-Day SMA
plt.figure(figsize=(12, 6))
plt.plot(reliance_close.index, reliance_close, label="Reliance Close Price", color="black", alpha=0.6, linewidth=1.5)
plt.plot(sma_50.index, sma_50, label="50-Day SMA (Short-Term)", color="blue", linewidth=2)
plt.plot(sma_200.index, sma_200, label="200-Day SMA (Long-Term)", color="red", linewidth=2)
plt.title("Reliance Industries - 50-Day & 200-Day Moving Average Crossover", fontsize=14, fontweight="bold")
plt.xlabel("Date", fontsize=11)
plt.ylabel("Price (INR)", fontsize=11)
plt.legend(frameon=True, facecolor="white")
plt.tight_layout()
# Replace plt.show() with:
plt.savefig("2_moving_averages.png", dpi=300, bbox_inches="tight")
plt.show()

# Chart 3: Risk vs. Return Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(annual_volatility, annual_returns, color="#1f77b4", s=120, edgecolors="black", zorder=5)

for ticker in tickers:
    name = ticker.replace(".NS", "")
    plt.annotate(
        name,
        (annual_volatility[ticker], annual_returns[ticker]),
        xytext=(10, 5),
        textcoords="offset points",
        fontsize=11,
        fontweight="bold"
    )

plt.title("Risk vs. Return Evaluation", fontsize=14, fontweight="bold")
plt.xlabel("Annualized Volatility (Risk)", fontsize=11)
plt.ylabel("Annualized Return", fontsize=11)
plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
plt.tight_layout()
# Replace plt.show() with:
plt.savefig("3_risk_return_scatter.png", dpi=300, bbox_inches="tight")
plt.show()

# Chart 4: Correlation Matrix Heatmap
plt.figure(figsize=(8, 6))
corr_matrix = daily_returns.corr()
corr_matrix.columns = [col.replace(".NS", "") for col in corr_matrix.columns]
corr_matrix.index = [idx.replace(".NS", "") for idx in corr_matrix.index]

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=0,
    vmax=1,
    linewidths=1.0,
    cbar_kws={"label": "Correlation Coefficient"}
)
plt.title("Daily Return Correlation Matrix", fontsize=14, fontweight="bold")
plt.tight_layout()
# Replace plt.show() with:
plt.savefig("4_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()