""" Explicación del Código:
Clase OptionPricing: Define los atributos necesarios para calcular el precio de la opción y la volatilidad implícita.
Métodos d1 y d2: Calculan los valores intermedios necesarios para el modelo de Black-Scholes.
Método bs_price: Calcula el precio de la opción utilizando el modelo de Black-Scholes.
Método implied_volatility: Utiliza el método de Newton-Raphson para iterar y encontrar la volatilidad implícita que 
hace que el precio calculado de la opción coincida con el precio de mercado.
Este código te permitirá calcular la volatilidad implícita de una opción dada su prima, precio de ejercicio, 
tiempo hasta el vencimiento y tasa de interés libre de riesgo. """
import scipy.stats as si
import numpy as np
import math

class OptionPricing:
    def __init__(self, S, K, T, r, market_price, option_type='call'):
        self.S = S  # Precio del activo subyacente
        self.K = K  # Precio de ejercicio
        self.T = T  # Tiempo hasta el vencimiento en años
        self.r = r  # Tasa de interés libre de riesgo
        self.market_price = market_price  # Precio de mercado de la opción
        self.option_type = option_type  # Tipo de opción ('call' o 'put')

    def d1(self, sigma):
        return (np.log(self.S / self.K) + (self.r + 0.5 * sigma ** 2) * self.T) / (sigma * np.sqrt(self.T))

    def d2(self, sigma):
        return self.d1(sigma) - sigma * np.sqrt(self.T)

    def bs_price(self, sigma):
        d1 = self.d1(sigma)
        d2 = self.d2(sigma)
        if self.option_type == 'call':
            price = (self.S * si.norm.cdf(d1, 0.0, 1.0) - self.K * np.exp(-self.r * self.T) * si.norm.cdf(d2, 0.0, 1.0))
        elif self.option_type == 'put':
            price = (self.K * np.exp(-self.r * self.T) * si.norm.cdf(-d2, 0.0, 1.0) - self.S * si.norm.cdf(-d1, 0.0, 1.0))
        return price

    def implied_volatility(self, tol=1e-5, max_iterations=100):
        sigma = 0.5  # Valor inicial de la volatilidad
        for i in range(max_iterations):
            price = self.bs_price(sigma)
            vega = self.S * si.norm.pdf(self.d1(sigma)) * np.sqrt(self.T)
            price_diff = self.market_price - price
            if abs(price_diff) < tol:
                return sigma
            sigma += price_diff / vega  # Método de Newton-Raphson
        return sigma

# Ejemplo de uso
S = 4470  # Precio del activo subyacente
K = 4458  # Precio de ejercicio
T = 0.15  # Tiempo hasta el vencimiento en años
r = 0.35  # Tasa de interés libre de riesgo
market_price = 367.6  # Precio de mercado de la opción

option = OptionPricing(S, K, T, r, market_price, option_type='call')
implied_vol = option.implied_volatility()
print(f'La volatilidad implícita es: {implied_vol:.2%}')
price_opt = option.bs_price(sigma=0.3392)
print(f'El precio de la prima es: {price_opt:.2f}')

