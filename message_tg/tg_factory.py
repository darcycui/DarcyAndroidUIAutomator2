from message_tg.bean.TGBean import TGBean
from message_tg.config.global_config_tg import DEVICE_ID_IN, COUNTRY_NUMBER_IN, PHONE_NUMBER_IN, CHAT_USER_NAME_IN, \
    ROOT_NAME_IN, DEVICE_ID_OUT, COUNTRY_NUMBER_OUT, PHONE_NUMBER_OUT, CHAT_USER_NAME_OUT, ROOT_NAME_OUT, \
    DEVICE_ID_OUT_HUAWEI, COUNTRY_NUMBER_OUT_HUAWEI, PHONE_NUMBER_OUT_HUAWEI, CHAT_USER_NAME_OUT_HUAWEI, \
    ROOT_NAME_OUT_HUAWEI, CHAT_USER_NAME_IN_HUAWEI, PACKAGE_NAME, FILE_EXPLORER_TEXT_IN, FILE_EXPLORER_TEXT_OUT_HUAWEI, \
    FILE_EXPLORER_TEXT_OUT, FILE_EXPLORER_PACKAGE_NAME_IN, FILE_EXPLORER_PACKAGE_NAME_OUT, \
    FILE_EXPLORER_PACKAGE_NAME_OUT_HUAWEI


def get_user_in_tg() -> TGBean:
    user_in = TGBean(
        device_id=DEVICE_ID_IN,
        country_number=COUNTRY_NUMBER_IN,
        phone_number=PHONE_NUMBER_IN,
        chat_user_name=CHAT_USER_NAME_IN,
        root_name=ROOT_NAME_IN,
        package_name=PACKAGE_NAME,
        file_explorer_text=FILE_EXPLORER_TEXT_IN,
        file_explorer_package_name=FILE_EXPLORER_PACKAGE_NAME_IN
    )
    return user_in


def get_user_out_tg() -> TGBean:
    user_out = TGBean(
        device_id=DEVICE_ID_OUT,
        country_number=COUNTRY_NUMBER_OUT,
        phone_number=PHONE_NUMBER_OUT,
        chat_user_name=CHAT_USER_NAME_OUT,
        root_name=ROOT_NAME_OUT,
        package_name=PACKAGE_NAME,
        file_explorer_text=FILE_EXPLORER_TEXT_OUT,
        file_explorer_package_name=FILE_EXPLORER_PACKAGE_NAME_OUT
    )
    return user_out


def get_user_out_huawei_tg() -> TGBean:
    user_out_huawei = TGBean(
        device_id=DEVICE_ID_OUT_HUAWEI,
        country_number=COUNTRY_NUMBER_OUT_HUAWEI,
        phone_number=PHONE_NUMBER_OUT_HUAWEI,
        chat_user_name=CHAT_USER_NAME_OUT_HUAWEI,
        root_name=ROOT_NAME_OUT_HUAWEI,
        package_name=PACKAGE_NAME,
        file_explorer_text=FILE_EXPLORER_TEXT_OUT_HUAWEI,
        file_explorer_package_name=FILE_EXPLORER_PACKAGE_NAME_OUT_HUAWEI
    )
    return user_out_huawei
