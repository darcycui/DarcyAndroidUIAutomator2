from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_DEVICE_ID_IN, SIGNAL_COUNTRY_NUMBER_IN, \
    SIGNAL_PHONE_NUMBER_IN, SIGNAL_CHAT_USER_NAME_IN, SIGNAL_ROOT_NAME_IN, SIGNAL_DEVICE_ID_OUT, \
    SIGNAL_COUNTRY_NUMBER_OUT, SIGNAL_PHONE_NUMBER_OUT, SIGNAL_CHAT_USER_NAME_OUT, SIGNAL_ROOT_NAME_OUT, \
    SIGNAL_USER_NAME_IN, SIGNAL_USER_NAME_OUT, SIGNAL_FILE_EXPLORER_TEXT_IN, SIGNAL_FILE_EXPLORER_PACKAGE_NAME_IN, \
    SIGNAL_FILE_EXPLORER_TEXT_OUT, SIGNAL_FILE_EXPLORER_PACKAGE_NAME_OUT_HUAWEI, SIGNAL_FILE_EXPLORER_PACKAGE_NAME_OUT, \
    SIGNAL_DEVICE_ID_OUT_HUAWEI, SIGNAL_COUNTRY_NUMBER_OUT_HUAWEI, SIGNAL_PHONE_NUMBER_OUT_HUAWEI, \
    SIGNAL_CHAT_USER_NAME_OUT_HUAWEI, SIGNAL_ROOT_NAME_OUT_HUAWEI, SIGNAL_USER_NAME_OUT_HUAWEI, \
    SIGNAL_FILE_EXPLORER_TEXT_OUT_HUAWEI


def get_signal_in() -> SignalBean:
    user_in = SignalBean(
        device_id=SIGNAL_DEVICE_ID_IN,
        country_number=SIGNAL_COUNTRY_NUMBER_IN,
        phone_number=SIGNAL_PHONE_NUMBER_IN,
        chat_user_name=SIGNAL_CHAT_USER_NAME_IN,
        root_name=SIGNAL_ROOT_NAME_IN,
        user_name=SIGNAL_USER_NAME_IN,
        file_explorer_text=SIGNAL_FILE_EXPLORER_TEXT_IN,
        file_explorer_package_name=SIGNAL_FILE_EXPLORER_PACKAGE_NAME_IN
    )
    return user_in


def get_signal_out() -> SignalBean:
    user_out = SignalBean(
        device_id=SIGNAL_DEVICE_ID_OUT,
        country_number=SIGNAL_COUNTRY_NUMBER_OUT,
        phone_number=SIGNAL_PHONE_NUMBER_OUT,
        chat_user_name=SIGNAL_CHAT_USER_NAME_OUT,
        root_name=SIGNAL_ROOT_NAME_OUT,
        user_name=SIGNAL_USER_NAME_OUT,
        file_explorer_text=SIGNAL_FILE_EXPLORER_TEXT_OUT,
        file_explorer_package_name=SIGNAL_FILE_EXPLORER_PACKAGE_NAME_OUT
    )
    return user_out


def get_signal_out_huawei() -> SignalBean:
    user_out_huawei = SignalBean(
        device_id=SIGNAL_DEVICE_ID_OUT_HUAWEI,
        country_number=SIGNAL_COUNTRY_NUMBER_OUT_HUAWEI,
        phone_number=SIGNAL_PHONE_NUMBER_OUT_HUAWEI,
        chat_user_name=SIGNAL_CHAT_USER_NAME_OUT_HUAWEI,
        root_name=SIGNAL_ROOT_NAME_OUT_HUAWEI,
        user_name=SIGNAL_USER_NAME_OUT_HUAWEI,
        file_explorer_text=SIGNAL_FILE_EXPLORER_TEXT_OUT_HUAWEI,
        file_explorer_package_name=SIGNAL_FILE_EXPLORER_PACKAGE_NAME_OUT_HUAWEI
    )
    return user_out_huawei
