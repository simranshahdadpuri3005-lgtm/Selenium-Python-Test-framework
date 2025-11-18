import logging

class Log_Maker:

    @staticmethod
    def log_gene():
        logging.basicConfig(filename="./Logs/SwagLabPytest.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt= '%Y/%m/%d %H:%M:%S %p', force= True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger



