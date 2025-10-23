from bean.IUserBean import IUserBean
from message_signal.config.global_config_sig import SIGNAL_PACKAGE_NAME
from vip import package_name


class SignalBean(IUserBean):
    def __init__(self, device_id: str, country_number: str, phone_number: str, chat_user_name: str, root_name: str,
                 user_name: str):
        super().__init__(device_id, country_number, phone_number, chat_user_name, root_name,
                         package_name=SIGNAL_PACKAGE_NAME)
        self.user_name = user_name
