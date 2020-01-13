# coding=utf-8
"""
Autodiscover is a Microsoft method for automatically getting the endpoint of the Exchange server and other
connection-related settings holding the email address using only the email address, and username and password of the
user.

The protocol for autodiscovering an email address is described in detail in
https://docs.microsoft.com/en-us/previous-versions/office/developer/exchange-server-interoperability-guidance. Handling
error messages is described here:
https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/handling-autodiscover-error-messages.

WARNING: The autodiscover protocol is very complicated. If you have problems autodiscovering using this implementation,
start by doing an official test at https://testconnectivity.microsoft.com
"""
from .cache import AutodiscoverCache, _autodiscover_cache, _autodiscover_cache_lock
from .legacy import discover
from .protocol import AutodiscoverProtocol


def close_connections():
    with _autodiscover_cache_lock:
        _autodiscover_cache.close()


def clear_cache():
    with _autodiscover_cache_lock:
        _autodiscover_cache.clear()


__all__ = [
    'AutodiscoverCache', 'discover', 'AutodiscoverProtocol', 'close_connections', 'clear_cache'
]