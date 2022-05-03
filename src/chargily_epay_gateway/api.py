
import json

from .constants import BASE_CHARGILY_API, PAYMENT_ENDPOINT

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

    def __init__(self, api_key, *args, **kwargs):
        self.__api_key = api_key
        self.__invoice = None

    def make_payment(self, **kwargs):
        """ Return raw response from Chargily server """
        self.__invoice = make_payment(self.__api_key, **kwargs)
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
