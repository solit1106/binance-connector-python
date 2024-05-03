#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)

try:
    response = client.place_limit_order(
        baseAsset="BNB",
        quoteAsset="USDT",
        limitPrice=0.0001,
        side="BUY",
        expiredType="1_D",
        baseAmount=0.0001,
    )
    logger.info(response)
except ClientError as error:
    logger.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
