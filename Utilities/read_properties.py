import configparser

config = configparser.ConfigParser()
config.read('./Configurations/config.ini')

class Read_Config:

    @staticmethod
    def get_admin_page_url():
        admin_page_url = config.get('Admin login info', 'admin_page_url')
        return admin_page_url

    @staticmethod
    def get_username():
        username = config.get('Admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('Admin login info', 'invalid_username')
        return invalid_username


