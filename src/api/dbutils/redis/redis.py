import pickle
from typing import List

import httpx
import redis
import sys
from datetime import timedelta
import json
from redis.commands.json.path import Path

from api.dbutils.models.contract import Contract


def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            password="ubuntu",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


client = redis_connect()


def get_data_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(key)
    return val


def set_data_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.setex(key, timedelta(seconds=3600), value=value, )
    return state


def add_contract_to_cache_database(contract: Contract):
    key = contract.firstname + contract.lastname + str(contract.zip)
    set_data_to_cache(f"contract:{key}", pickle.dumps(contract))


def get_all_contracts() -> List[Contract]:
    contracts = []
    for key in client.scan_iter("contract:*"):
        contract = pickle.loads(get_data_from_cache(key))
        contracts.append(contract)
    return contracts
