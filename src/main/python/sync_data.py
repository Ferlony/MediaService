import json
from typing import Union
from datetime import datetime

from src.main.python.db.worker_db import (get_sync_data, update_sync_data)


# TODO
class SyncData:
    # {
    #   sync_data:
    #   [
    #       {"key_data1": {"key1": "value1", "key2": "value2"}},
    #       {"key_data2": {"key1": "value1", "key2": "value2"}}...
    #   ]
    # }

    @staticmethod
    def __sync_items(current_item: dict, last_item: dict) -> dict:
        current_date: datetime = current_item["date"]
        last_date: datetime = last_item["date"]

        if current_date > last_date:
            return current_item
        else:
            return last_item

    def __sync_alg(self, current_data: dict, last_data: dict) -> dict:
        current_data_list = list(current_data.values())[0]  # B*
        last_data_list = list(last_data.values())[0]  # A*

        current_data_keys: set = set([list(each.keys())[0] for each in current_data_list])  # B
        last_data_keys: set = set([list(each.keys())[0] for each in last_data_list])  # A
        to_update_keys: set = last_data_keys.intersection(current_data_keys)  # D

        new_keys: set = current_data_keys - to_update_keys  # C ~ B*
        old_keys: set = last_data_keys - to_update_keys  # E ~ A*

        synced_data_list = []

        for to_update_key in list(to_update_keys):
            current_to_sync_values: Union[dict, None] = None
            last_to_sync_values: Union[dict, None] = None
            for each in current_data_list:
                current_key, current_values = list(each.items())[0]
                if current_key == to_update_key:
                    # current_to_sync_values = json.loads(current_values)
                    current_to_sync_values = current_values
                    break
            for each in last_data_list:
                last_key, last_values = list(each.items())[0]
                if last_key == to_update_key:
                    # last_to_sync_values = json.loads(last_values)
                    last_to_sync_values = last_values
                    break

            synced_values = self.__sync_items(current_to_sync_values, last_to_sync_values)
            synced_data_list.append({to_update_key: synced_values})
            # synced_data_list.append({to_update_key: json.dumps(synced_values)})

        for old_key in list(old_keys):
            for each in last_data_list:
                key, values = list(each.items())[0]
                if old_key == key:
                    synced_data_list.append({old_key: values})
                    break

        for new_key in list(new_keys):
            for each in current_data_list:
                key, values = list(each.items())[0]
                if new_key == key:
                    synced_data_list.append({new_key: values})
                    break

        return {"sync_data": synced_data_list}

    def sync_devices(self, current_data: Union[dict, None], username: str):
        last_data = get_sync_data(username)

        if not current_data and not last_data:
            return None

        if not last_data:
            sync_data = current_data
            update_sync_data(username, sync_data)
            return sync_data

        if not current_data:
            sync_data = last_data
            return sync_data

        sync_data = self.__sync_alg(current_data, last_data)
        update_sync_data(username, sync_data)
        return sync_data
