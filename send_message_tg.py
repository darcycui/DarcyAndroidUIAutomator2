from message_tg.config.global_config_tg import CHAT_USER_NAME_IN_HUAWEI
from message_tg.entry.tg_pipeline import start_chat_pair_tg
from message_tg.tg_factory import get_user_in_tg, get_user_out_tg, get_user_out_huawei_tg

if __name__ == '__main__':
    user_in = get_user_in_tg()
    user_out = get_user_out_tg()
    user_out_huawei = get_user_out_huawei_tg()

    start_chat_pair_tg(user_in, user_out)

    user_in.chat_user_name = CHAT_USER_NAME_IN_HUAWEI
    start_chat_pair_tg(user_in, user_out_huawei)
