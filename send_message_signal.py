from message_signal.entry.signal_pipeline import start_chat_pair_signal
from message_signal.factory.signal_factory import get_signal_in, get_signal_out, get_signal_out_huawei

if __name__ == '__main__':
    user_in = get_signal_in()
    user_out = get_signal_out()
    user_out_huawei = get_signal_out_huawei()

    start_chat_pair_signal(user_in, user_out)
