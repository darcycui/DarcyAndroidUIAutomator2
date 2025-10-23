from bean.IUserBean import IUserBean
from message_tg.config.global_config_tg import PACKAGE_NAME, PACKAGE_NAME_BETA, PACKAGE_NAME_WEB


class TGBean(IUserBean):
    def __init__(self, device_id: str, country_number: str, phone_number: str, chat_user_name: str, root_name: str,
                 package_name: str):
        super().__init__(device_id, country_number, phone_number, chat_user_name, root_name, PACKAGE_NAME)
        self.package_name_beta: str = PACKAGE_NAME_BETA
        self.package_name_web: str = PACKAGE_NAME_WEB
