from datetime import datetime

from src.main.python.config.config_dataclass import ConfigData


class AuthLog:
    __current_client_host = []

    @property
    def current_client_host(self):
        return self.__current_client_host

    @current_client_host.setter
    def current_client_host(self, value):
        self.__current_client_host = value

    @staticmethod
    def do_log_auth(auth_status):
        with open(ConfigData.log_auth, "a") as f:
            now_human_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            f.write(f"AUTH:    {auth_status} IN {now_human_time}\n")

    def set_default_current_client_host(self):
        self.current_client_host = []

    def log_attempt_new_connection_host(self, host):
        if host not in self.current_client_host:
            self.current_client_host.append(host)
            self.do_log_auth(f"SUCCESS FROM {host}")
