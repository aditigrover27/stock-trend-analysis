# 📊 Stock Price Analysis

## Overview
An automated quantitative finance and data visualization pipeline built in **Python**. This project ingests 5 years of daily market data from the **National Stock Exchange (NSE)** for three major Indian equities—**Reliance Industries (`RELIANCE.NS`)**, **Tata Consultancy Services (`TCS.NS`)**, and **HDFC Bank (`HDFCBANK.NS`)**—to evaluate capital efficiency, structural price trends, and portfolio diversification benefits.

---

## 🔍 Key Financial & Quantitative Insights

* **Risk-Adjusted Performance Winner:** **Reliance Industries** delivered the superior capital efficiency over the analyzed timeframe, achieving the highest annualized return (**`13.52%`**) and the best Sharpe Ratio (**`0.3308`**, assuming $R_f = 6\%$).
* **Volatility & Drawdown Profiles:** Evaluated annualized risk ($\sigma$) across all equities. While **TCS** exhibited slightly lower annualized volatility (**`20.76%`**), its low excess return resulted in the weakest Sharpe Ratio (**`0.0271`**).
* **Structural Trend Analysis:** Modelled **50-Day vs. 200-Day Simple Moving Averages (SMA)** to identify momentum shifts, support/resistance baselines, and structural buy/sell crossover signals (*Golden Crosses* and *Death Crosses*).
* **Equal-Scale Comparison (Base = 100):** Rebased all share prices to an index value of **100** at the start date to compare cumulative wealth generation across assets trading at vastly different nominal share prices.
* **Portfolio Diversification Proof:** Constructed a daily return correlation matrix heatmap to measure inter-asset co-movement and downside protection across Energy/Conglomerate, IT, and Financial sectors.

---

## 📈 Performance Summary Table

| Ticker | Asset Name | Annualized Return | Annualized Volatility ($\sigma$) | Sharpe Ratio ($R_f = 0.06$) |
| :--- | :--- | :---: | :---: | :---: |
| **`RELIANCE.NS`** | Reliance Industries | **13.52%** | 22.73% | **0.3308** |
| **`HDFCBANK.NS`** | HDFC Bank | **10.10%** | 21.24% | **0.1929** |
| **`TCS.NS`** | Tata Consultancy Services | **6.56%** | 20.76% | **0.0271** |

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python 3
* **Market Data Ingestion:** `yfinance`
* **Data Manipulation & Math:** `pandas`, `numpy`
* **Financial Visualization:** `matplotlib`, `seaborn`

---

## 📁 Repository Structure & Artifacts

| File / Folder | Description |
| :--- | :--- |
| **`stock_analysis_project.py`** | Core Python script containing data downloading, financial math, metric calculation, and chart generation. |
| **`1_normalized_growth.png`** | Normalized price performance growth chart comparing ₹100 initial investment trajectories. |
| **`2_moving_averages.png`** | 50-day and 200-day Simple Moving Average crossover chart for Reliance Industries. |
| **`3_risk_return_scatter.png`** | Risk vs. Return evaluation scatter plot mapping annualized volatility against returns. |
| **`4_correlation_heatmap.png`** | Inter-asset daily return correlation matrix heatmap evaluating diversification efficiency. |

---

## 🚀 How to Run the Script

1. Ensure Python 3 is installed on your system.
2. Install required financial and plotting dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib seaborn
