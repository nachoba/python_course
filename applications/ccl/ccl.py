# Cálculo del US$ CCL x ADRs
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

datos = yf.download(
        ["GGAL", "GGAL.BA", "YPF", "YPFD.BA", "PAM", "PAMP.BA", "TGS", "TGSU2.BA", "BMA", "BMA.BA"],
        auto_adjust=True,
        start="2023-01-01")

cierres = datos.Close

ccl_GGAL = cierres["GGAL.BA"] * 10 / cierres["GGAL"]
ccl_BMA  = cierres["BMA.BA"] *  10 / cierres["BMA"]
ccl_YPF  = cierres["YPFD.BA"] / cierres["YPF"]
ccl_PAM  = cierres["PAMP.BA"] * 25 / cierres["PAM"]
ccl_TGS  = cierres["TGSU2.BA"] * 5 / cierres["TGS"]

df = pd.concat([ccl_GGAL, ccl_BMA, ccl_YPF, ccl_PAM, ccl_TGS], axis=1)
df.columns = ["GGAL", "BMA", "YPF", "PAMP", "TGSU2"]

# print(df.tail(1))
average = df.tail(1).sum(axis=1) / 5 
valor_actual = round(average.iloc[-1],2)
print("El valor promedio del US$ CCL es ${:,.2f}".format(valor_actual))



# fig, ax = plt.subplots(figsize=(15,6), dpi=300)
# ax.plot(df, lw=0.75)
# plt.show()

