from message_signal.config.global_config_sig import SIGNAL_PACKAGE_NAME


class SignalBean(object):
    def __init__(self,
                 device_id: str,
                 country_number: str,
                 phone_number: str,
                 chat_user_name: str,
                 root_name: str):
        self.device_id: str = device_id
        self.country_number: str = country_number
        self.phone_number: str = phone_number
        self.chat_user_name: str = chat_user_name
        self.root_name: str = root_name
        self.package_name = SIGNAL_PACKAGE_NAME
