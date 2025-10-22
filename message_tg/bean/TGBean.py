from message_tg.config.global_config_tg import PACKAGE_NAME, PACKAGE_NAME_BETA, PACKAGE_NAME_WEB


class UserBean:
    def __init__(self,
                 device_id: str,
                 country_number: str,
                 phone_number: str,
                 chat_user_name: str,
                 root_name: str
                 ):
        self.device_id: str = device_id
        self.country_number: str = country_number
        self.phone_number: str = phone_number
        self.chat_user_name: str = chat_user_name
        self.root_name: str = root_name
        self.package_name: str = PACKAGE_NAME
        self.package_name_beta: str = PACKAGE_NAME_BETA
        self.package_name_web: str = PACKAGE_NAME_WEB
