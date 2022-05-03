# epay-chargily-python
Chargily ePay Gateway (Python Package)

![Chargily ePay Gateway](https://raw.githubusercontent.com/Chargily/epay-gateway-php/main/assets/banner-1544x500.png "Chargily ePay Gateway")

This Plugin is to integrate ePayment gateway with Chargily easily.
- Currently support payment by **CIB / EDAHABIA** cards and soon by **Visa / Mastercard** 
- This repo is recently created for **Python package**, If you are a developer and want to collaborate to the development of this package, you are welcomed!

# Requirements
1. Python 2.7 or higher.
2. API Key/Secret from [ePay by Chargily](https://epay.chargily.com.dz) dashboard for free.
3. Requests.

# Installation
1- Install the package:

```bash
pip install chargily-epay-gateway
```

or pipenv
```bash
pipenv install chargily-epay-gateway
```

2- Setup the Environment Variables:

* Mac/Linux:
```bash
export CHARGILY_API_KEY='YOUR_API_KEY'
export CHARGILY_SECRET_KEY='YOUR_SECRET_KEY'
```

# Usage

1- Make Payment:

* Class based way:

```python
import os
from chargily_epay_gateway.api import Invoice

CHARGILY_API_KEY = os.environ["CHARGILY_API_KEY"]

invoice = Invoice(CHARGILY_API_KEY)


invoice_payment = invoice.make_payment(
    client='Client name goes here',
    client_email='Client email goes here',
    invoice_number='Invoice number as integer',
    amount='Amount as float',
    discount='Discount as float',
    back_url='https://your-website-url/',
    webhook_url='https://your-website-url/<webhook_path>/',
    mode="CIB or EDAHABIA",
    comment='Comment goes here',
)

invoice.get_invoice_content()  # Return invoice data as python data structure

Invoice.load_invoice(invoice_payment)  # Also return invoice data as python data structure

invoice.get_invoice()  # Return the invoice as response
```

* Function based way:

```python
import os
from chargily_epay_gateway.api import make_payment

CHARGILY_API_KEY = os.environ["CHARGILY_API_KEY"]


invoice = make_payment(
    api_key=CHARGILY_API_KEY,
    client='Client name goes here',
    client_email='Client email goes here',
    invoice_number='Invoice number as integer',
    amount='Amount as float',
    discount='Discount as float',
    back_url='https://your-website-url/',
    webhook_url='https://your-website-url/<webhook_path>/',
    mode="CIB or EDAHABIA",
    comment='Comment goes here',
)
```

2- Validate Chargily Signature:

```python
from chargily_epay_gateway.utils import signature_is_valid

# Return True if signature is valid, otherwise False
valid_signature = webhook_is_valid(request)
```

# Configurations

- Available Configurations

| key                   |  description                                                                                          | redirect url |  process url |
|-----------------------|-------------------------------------------------------------------------------------------------------|--------------|--------------|
| CHARGILY_APP_KEY               | must be string given by organization                                                                  |   required   |   required   |
| CHARGILY_APP_SECRET            | must be string given by organization                                                                  |   required   |   required   |
| back_url        | must be string and valid url                                                                          |   required   | not required |
| webhook_url        | must be string and valid url                                                                          _|   required   | required |
| mode                  | must be in **CIB**,**EDAHABIA**                                                                       |   required   | not required |
| invoice_number       |  string or int                                                                                 |   required   | not required |
| client_name  | string                                                                                        |   required   | not required |
| clientEmail | must be valid email This is where client receive payment receipt after confirmation        |   required   | not required |
| amount      | must be numeric and greather or equal than  75                                                        |   required   | not required |
| discount    | must be numeric and between 0 and 99  (discount in %)                                     |   required   | not required |
| description  | must be string_                                                                                        |   required   | not required |


# Notice

- If you faced Issues [Click here to open one](https://github.com/Chargily/epay-gateway-python)
