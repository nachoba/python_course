# This program calculates the intrinsic value of a put option

spot_price = float(input("Enter the spot price of the stock:"))
strike_price = float(input("Enter the strike price of the option:"))

intrinsic_value = strike_price - spot_price

if (intrinsic_value > 0):

    print(f"The intrinsic value of the put option is {intrinsic_value:.2f}")
else:
    print(f"The put option is out of the money and has no intrinsic value.")




