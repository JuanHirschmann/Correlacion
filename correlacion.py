import numpy as np
import yfinance as yf
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

ADRs = [
    "SPY",
    "QQQ",
    "^DJI",
    "EEM",
    "EWZ",
    "BMA",
    "GGAL",
    "SUPV",
    "TS",
    "TX",
    "MELI",
    "CRESY",
    "IRS",
    "LOMA",
    "TEO",
    "CEPU",
    "EDN",
    "PAM",
    "TGS",
    "YPF",
]
datos = yf.download(ADRs, period="3y")
print(datos["Adj Close"])
datos = datos["Adj Close"]
plt.title("Correlación 3 años")
matriz_correlacion = datos.pct_change().fillna(method="bfill")[ADRs].corr()
sns.heatmap(matriz_correlacion, linewidths=0.5, cmap="RdYlGn")

plt.show()
