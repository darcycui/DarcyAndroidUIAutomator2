from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_DEVICE_ID_IN, SIGNAL_COUNTRY_NUMBER_IN, \
    SIGNAL_PHONE_NUMBER_IN, SIGNAL_CHAT_USER_NAME_IN, SIGNAL_ROOT_NAME_IN, SIGNAL_DEVICE_ID_OUT, \
    SIGNAL_COUNTRY_NUMBER_OUT, SIGNAL_PHONE_NUMBER_OUT, SIGNAL_CHAT_USER_NAME_OUT, SIGNAL_ROOT_NAME_OUT, \
    SIGNAL_USER_NAME_IN, SIGNAL_USER_NAME_OUT
from message_signal.entry.signal_pipeline import start_chat_pair_signal

if __name__ == '__main__':
    user_in = SignalBean(
        device_id=SIGNAL_DEVICE_ID_IN,
        country_number=SIGNAL_COUNTRY_NUMBER_IN,
        phone_number=SIGNAL_PHONE_NUMBER_IN,
        chat_user_name=SIGNAL_CHAT_USER_NAME_IN,
        root_name=SIGNAL_ROOT_NAME_IN,
        user_name=SIGNAL_USER_NAME_IN)

    user_out = SignalBean(
        device_id=SIGNAL_DEVICE_ID_OUT,
        country_number=SIGNAL_COUNTRY_NUMBER_OUT,
        phone_number=SIGNAL_PHONE_NUMBER_OUT,
        chat_user_name=SIGNAL_CHAT_USER_NAME_OUT,
        root_name=SIGNAL_ROOT_NAME_OUT,
        user_name=SIGNAL_USER_NAME_OUT)

    start_chat_pair_signal(user_in, user_out)
