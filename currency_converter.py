## import libraries
import requests

def get_currency_rates():
    response = requests.get('https://api.frankfurter.app/latest')
    if response.status_code == 200:
        data = response.json()
        if 'rates' in data:
            return data['rates']
        else:
            print('Error: response does not contain "rates" key')
    else:
        print('Error: API request failed with status code', response.status_code)
    return None

def convert_to_inr(amount, currency_code):
    currency_rates = get_currency_rates()
    if currency_rates is not None and currency_code in currency_rates:
        inr_rate = currency_rates['INR']
        return amount * (inr_rate / currency_rates[currency_code])
    else:
        print('Error: unable to convert', currency_code, 'to INR')
    return None

def convert_from_inr(amount, currency_code):
    currency_rates = get_currency_rates()
    if currency_rates is not None and currency_code in currency_rates:
        inr_rate = currency_rates['INR']
        return amount / (inr_rate / currency_rates[currency_code])
    else:
        print('Error: unable to convert INR to', currency_code)
    return None

# Convert USD to INR
usd_to_inr = convert_to_inr(100, 'USD')
print('100 USD =', usd_to_inr, 'INR')

# Convert INR to USD
inr_to_usd = convert_from_inr(100, 'USD')
print('100 INR =', inr_to_usd, 'USD')

# Convert EUR to INR
eur_to_inr = convert_to_inr(100, 'EUR')
print('100 EUR =', eur_to_inr, 'INR')

# Convert INR to EUR
inr_to_eur = convert_from_inr(100, 'EUR')
print('100 INR =', inr_to_eur, 'EUR')

# Convert GBP to INR
gbp_to_inr = convert_to_inr(100, 'GBP')
print('100 GBP =', gbp_to_inr, 'INR')

# Convert INR to GBP
inr_to_gbp = convert_from_inr(100, 'GBP')
print('100 INR =', inr_to_gbp, 'GBP')

# Convert JPY to INR
jpy_to_inr = convert_to_inr(100, 'JPY')
print('100 JPY =', jpy_to_inr, 'INR')

# Convert INR to JPY
inr_to_jpy = convert_from_inr(100, 'JPY')
print('100 INR =', inr_to_jpy, 'JPY')

# Convert AUD to INR
aud_to_inr = convert_to_inr(100, 'AUD')
print('100 AUD =', aud_to_inr, 'INR')

# Convert INR to AUD
inr_to_aud = convert_from_inr(100, 'AUD')
print('100 INR =', inr_to_aud, 'AUD')

# Convert CAD to INR
cad_to_inr = convert_to_inr(100, 'CAD')
print('100 CAD =', cad_to_inr, 'INR')

# Convert INR to CAD
inr_to_cad = convert_from_inr(100, 'CAD')
print('100 INR =', inr_to_cad, 'CAD')

