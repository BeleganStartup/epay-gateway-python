
from . import exceptions as ex
from .constants import SIGNATURE_KEY
from .security import text2hash


def signature_is_valid(secret_key, invoice):
    """ Validate the sinature sent by Chargily server """
    # Get Signature
    try:
        signature = invoice.headers[SIGNATURE_KEY]
    except KeyError:
        raise ex.ChargilyErrorSignatureMissing(SIGNATURE_KEY)
    # Hash the body
    try:
        msg = invoice.body
    except AttributeError:
        msg = invoice.content
    confirm_signature = text2hash(msg, secret_key)
    return signature == confirm_signature
