from adbutils import device

from message_tg.bean.TGBean import UserBean
from message_tg.config.global_config_tg import DEVICE_ID_IN, COUNTRY_NUMBER_IN, PHONE_NUMBER_IN, CHAT_USER_NAME_IN, \
    ROOT_NAME_IN, DEVICE_ID_OUT, COUNTRY_NUMBER_OUT, PHONE_NUMBER_OUT, CHAT_USER_NAME_OUT, ROOT_NAME_OUT, \
    DEVICE_ID_OUT_HUAWEI, COUNTRY_NUMBER_OUT_HUAWEI, PHONE_NUMBER_OUT_HUAWEI, CHAT_USER_NAME_OUT_HUAWEI, \
    ROOT_NAME_OUT_HUAWEI, CHAT_USER_NAME_IN_HUAWEI
from message_tg.entry.tg_pipeline import start_chat_pair

if __name__ == '__main__':
    user_in = UserBean(
        device_id=DEVICE_ID_IN,
        country_number=COUNTRY_NUMBER_IN,
        phone_number=PHONE_NUMBER_IN,
        chat_user_name=CHAT_USER_NAME_IN,
        root_name=ROOT_NAME_IN)

    user_out = UserBean(
        device_id=DEVICE_ID_OUT,
        country_number=COUNTRY_NUMBER_OUT,
        phone_number=PHONE_NUMBER_OUT,
        chat_user_name=CHAT_USER_NAME_OUT,
        root_name=ROOT_NAME_OUT)

    user_out_huawei = UserBean(
        device_id=DEVICE_ID_OUT_HUAWEI,
        country_number=COUNTRY_NUMBER_OUT_HUAWEI,
        phone_number=PHONE_NUMBER_OUT_HUAWEI,
        chat_user_name=CHAT_USER_NAME_OUT_HUAWEI,
        root_name=ROOT_NAME_OUT_HUAWEI)

    # start_chat_pair(user_in, user_out)

    user_in.chat_user_name = CHAT_USER_NAME_IN_HUAWEI
    start_chat_pair(user_in, user_out_huawei)
