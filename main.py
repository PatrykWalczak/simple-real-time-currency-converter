from forex_python.converter import CurrencyRates

currency = CurrencyRates()
amount = float(input("How much: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
result = currency.convert(from_currency, to_currency, amount)
print(f'After exchanging {from_currency} you get', round(result, 2), to_currency)
print("1", from_currency, "is", currency.get_rate(from_currency, to_currency), to_currency)