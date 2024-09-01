#finance #derivatives 
# Covered Calls for Beginners
## Chapter 2 - The Basics of Options Contracts
Options terminology revolves around the way a contract is structured. Once you understand how the structure works, you'll have no problems grasping what the various terms means.

### Call Options
A ***call*** option gives you the right to buy the underlying security at a certain price. An option's ***strike price*** is the level at which it will make you money. Choosing the right strike price is very important with a call or a put because it determines how far the underlying has to move in order for you to start making money.

Investors buy calls when they're bullish about a stock's prospects. How do you use a call to buy the underlying? The process is called *exercising the option.* Remember that each call options contract covers 100 shares of the underlying.

> ***Example:*** If you exercise a single options contract of Mercado Libre at $2,500 you we'll need to pay $250,000 in cash from your account. 

Over and above this, you'll also need to pay the ***premium*** when you buy the call. The premium is not recoverable under any circumstances. Whether your trade goes for a profit or a loss, you will lose this money. 
Therefore, when exercising or selling a call, you need to make sure you earn at least this much back in order to break even.

The option's premium fluctuates depending on how close the underlying market price is to the strike price. An option's premium has two portions to it: The ***intrinsic value*** and the ***time value*** (also known as extrinsic value). In order to understand how these work, you first need to understand ***expiry dates.***

### Expiry Dates
All options contracts have an expiry date attached to them. This means that whether you want to exercise or sell the option, you need to do that before the expiry date. Let's consider an example:

> Mercado Libre stock is selling for $2,000. You can buy two calls: one with a strike price of $1,900 and another with a strike price of $1,500. Both of these calls expire in the same month, which is 30 days away. Their premium will differ since clearly, they're not worth the same.
> The $1,500 call will make you more money. Its price will be a sum of it *intrinsic value* and its *time value*. The intrinsic value is a straightforward mathematical calculation.
> It's simply the difference between the underlying price and the strike price:
> `Call MELI $1,500 -> $2,000 - $1,500 = $500`
> `Call MELI $1,900 -> $2,000 - $1,900 = $100`

```python
# This program calculates the intrinsinc value of a call option

spot_price   = float(input("Enter the spot price of the stock:"))
strike_price = float(input("Enter the strike price of the option:"))

intrinsic_value = spot_price - strike_price

if (intrinsic_value > 0):
    print(f"The intrinsic value of the call option is {intrinsic_value:.2f}")
else:
    print(f"The call option is out of the money and has no intrinsic value")
```

This leaves us with the time value. Unlike the *intrinsic value*, the *time value* is not as straightforward mathematical calculation. ***The longer and option has until expiration, the more valuable it is.*** The reasoning is that there is more time for the underlying to move into a position where the option can make you money.***The closer it is to expiry, the less value it has, since there is less time for the option to make you money.***
Time value is a constantly changing thing and there is no straightforward method of calculating it. But, the concept of *time value* is far more important for you to understand than calculating the value itself. ***Specifically, you need to understand that time value decreases as the option approaches expiry.*** This phenomenon is called ***time decay.*** 
***Time decay*** usually accelerates once the option is less than 30 days aways from expiry.

💥Some options can be exercised or sold only on the expiry date: these are called ***European*** options. The other type of options, called ***American*** options, can be exercised on any day leading up to the expiry date.

### In and Out of the Money
In the case of a ***call option***, the investor makes money only when the underlying price is greater than the option's ***strike price.*** If an option can make its owner money, it's said to be ***in the money*** or ***ITM.***

When the strike price equals the market price, the option is said to be ***at the money*** or ***ATM.***

When the call option is ***outside the money*** or ***OTM***, the strike price is greater than the market price. In this scenario, the option buyer would lose money if they exercised it; therefore in the case of an ***OTM*** option the *intrinsic value* is zero, and the option has only *time value* attached to it.

With ***OTM*** options, if the underlying price increases past the strike price turning the option ***in the money*** or ***ITM,*** the option premium value will rise accordingly since it will gain *intrinsic value.* Its *time value* will also increase by some amount despite moving closer to expiry since the probability of making money is taken into account in this value.


> ***A Sample Option Trade***
> You spotted a reason for Mercado Libre to increase in value from it current price of $2,000. You think it's going to go past $2,500 over the next two months easily.
> Since you think a target price of $2,500 is probable, you'd want to pick a call with a strike that is less than $2,500 but still leaves you with enough room to earn profit.
> Take a look at the calls and decide that the $2,200 is the right strike price. 
> At this level, the option has no intrinsic value since it's ***OTM.***
> This call costs you $50, you'll pay $5,000 since every options contract controls 100 shares.
> As MELI increases in price, your calls become more valuable. Eventually, with a week remaining until expiry, the underlying sells for $2,400: this results in a $200 gain in intrinsic value per share.
> However, your time value is quickly decreasing since there isn't much time left till expiry.
> At this point, you have two choices:
> 1. Exercise the call and buy 100 shares of MELI at $2,200
> 2. Sell the call and earn profit
> Let's assume that time value declines to zero: that isn't a problem because the call still has an intrinsic value of $200 per share in it.
> Selling the option will result in a credit of $20.000 to your account. You paid $5,000 to buy the call. This leaves you with a profit of $35,000. ***This is the best case scenario.***
> The ***worst case scenario*** for you would be the underlying not moving past your strike price of $2,200. What happens then?
> Your contract will be worthless since it will be ***OTM*** upon expiry. You simple let it expire, and all you lose is your initial $5,000 investment, which is how much you paid to buy the call.


### Put Options
Call options give you the right to buy the stock at a particular price, whereas puts give you the right to sell the underlying at a particular price. Puts tend to confuse new investors a bit since you're effectively shorting the underlying stock, which is not something you'd usually do with regular investing. 
Put options solve the problem of margins.

> ***A Sample Option Trade***
> The terminology associated with puts is the same as it is with calls. It's just that ***ITM*** and ***OTM*** conditions are flipped. Puts make you money when the underlying value is less than the strike price: this is when they're **ITM**,
> For example: If MELI is selling for $2,000 the $1,900 put is **OTM**, and the $2,300 put is **ITM**. In the case of a call, the $1,900 call will be **ITM** and the $2,300 call will be ***OTM.***
> The calculation of *intrinsic value* is also flipped in the case of a put. A put gains *intrinsic value* when the underlying moves lower than the *strike price*. It has no *intrinsic value* as long as the underlying is greater than the strike price. 
> The time value works in the same way as it does with a call.
> So, you think MELI's price will decline to $1,800. Instead of shorting the stock, you buy puts with a strike price of $1,900. If MELI declines to $1,800 you will earn a profit of $100 per share, or $10,000 per contract. 
> If the put expires ***OTM*** you'll lose only the premium you paid for the put.

We'd like to point out once again that you'll be buying the put, not shorting it. You can short or write a put, but that's not what's going on here. If you wish to benefit from a decline in prices, you buy a put.

```python
# This program calculates the intrinsinc value of a put option

spot_price   = float(input("Enter the spot price of the stock:"))
strike_price = float(input("Enter the strike price of the option:"))

intrinsic_value = strike_price - spot_price

if (intrinsic_value > 0):
    print(f"The intrinsic value of the put option is {intrinsic_value:.2f}")
else:
    print(f"The put option is out of the money and has no intrinsic value")
```

### Buying and Writing Options


