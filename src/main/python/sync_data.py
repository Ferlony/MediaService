from src.main.python.db.worker_db import (get_sync_data, update_sync_data)


# TODO
class SyncData:
    # {
    #   sync_data:
    #   [
    #       {"key_data1": {"key1": "value1", "key2": "value2"}},
    #       {"key_data2": {"key1": "value1", "key2": "value2"}}
    #   ]
    # }

    @staticmethod
    def __sync_alg(current_data: dict, last_data: dict):
        current_data_list = list(current_data.values())[0]
        last_data_list = list(last_data.values())[0]

        synced_data_list = []

        for item in current_data_list:

            key, values = list(item.items())[0]


            break

        return

    @staticmethod
    def __get_items_from_data_list(data: list) -> list:
        out = []
        for each in data:
            key, values = list(each.items())[0]

    def sync_devices(self, current_data: dict, username: str) -> str:
        last_data = get_sync_data(username)
        if not last_data:
            update_sync_data(username, current_data)
            return "Sync data created"

        self.__sync_alg(current_data, last_data)
