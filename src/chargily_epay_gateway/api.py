
import json

from .constants import BASE_CHARGILY_API, PAYMENT_ENDPOINT
from .exceptions import ChargilyErrorKeyMissing

import requests


def make_payment(api_key, **kwargs):
    payment_url = BASE_CHARGILY_API + PAYMENT_ENDPOINT
    headers = {
        "X-Authorization" : api_key,
        "Accept" : 'application/json'
    }
    payloads = {
        'client':kwargs.get('client', None),
        'client_email':kwargs.get('client_email', None),
        'invoice_number':kwargs.get('invoice_number', None),
        'amount':kwargs.get('amount', None),
        'discount':kwargs.get('discount', None),
        'back_url':kwargs.get('back_url', None),
        'webhook_url':kwargs.get('webhook_url', None),
        'mode':kwargs.get('mode', None),
        'comment':kwargs.get('comment', None),
    }
    return requests.post(payment_url, headers=headers, data=payloads)


class Invoice:
    API_KEY = None

    def __init__(self, api_key=None, *args, **kwargs):
        if api_key:
            self.API_KEY = api_key
        if self.API_KEY is None:
            raise ChargilyErrorKeyMissing('API KEY')
        self.__invoice = None

    def make_payment(self, **kwargs):
        """ Return raw response from Chargily server """
        self.__invoice = make_payment(self.API_KEY, **kwargs)
        return self.get_invoice()

    def get_invoice(self):
        """ Return current raw invoice """
        return self.__invoice

    def get_invoice_content(self):
        """ Load current raw invoice (JSON -> Python) """
        return Invoice.load_invoice(self.__invoice.content)

    @classmethod
    def load_invoice(cls, invoice):
        """ JSON -> Python """
        return json.loads(invoice)
