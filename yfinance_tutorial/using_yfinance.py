# Yfinance Cookbook
# =================

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt



# Bajamos los datos y los almacenamos en un DataFrame
df = yf.download("YPF", start="1995-01-01", end="2024-12-31", progress=True)

# Vemos los últimos datos del DataFrame
print(df.tail())

# Vemos datos básicos del DataFrame
print(df.info())


# Tomamos solamente el precio ajustado
adj_close = df["Adj Close"]


# Graficamos la serie de precio ajustado
#plt.plot(adj_close)
#plt.ylabel("Precio")
#plt.xlabel("Fecha")
#plt.title("Evolución del precio de YPF - NYSE (USD)")
#plt.grid(True)
#plt.show()

# Bajamos los datos usando el método Ticker para obtener más datos
ypf = yf.Ticker("YPF")

# ¿Pagó dividendos YPF alguna vez?
print(ypf.dividends)

fig, ax = plt.subplots()
ax.plot(ypf.dividends,"ro")
plt.title("Pago de dividendos de YPF USD")
plt.grid(True)
plt.show()

