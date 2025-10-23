class IUserBean(object):
    def __init__(self,
                 device_id: str,
                 country_number: str,
                 phone_number: str,
                 chat_user_name: str,
                 root_name: str,
                 package_name: str
                 ):
        self.device_id: str = device_id
        self.country_number: str = country_number
        self.phone_number: str = phone_number
        self.chat_user_name: str = chat_user_name
        self.root_name: str = root_name
        self.package_name = package_name