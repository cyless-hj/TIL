"""
JDBC Connect Info
"""

from enum import Enum

class DataWarehouse(Enum):
    """
    JDBC Connect Enum
    """
    URL = 'jdbc:oracle:thin:@decorona_high?TNS_ADMIN=/home/big/study/db/Wallet_DECORONA',
    PROPS = {
        'user':'dw_de',
        'password':'123qwe!@#QWE'
    }


class DataMart(Enum):
    """
    JDBC Connect Enum
    """
    URL = 'jdbc:oracle:thin:@decorona_high?TNS_ADMIN=/home/big/study/db/Wallet_DECORONA',
    PROPS = {
        'user':'dm_de',
        'password':'123qwe!@#QWE'
    }

def save_data(config, dataframe, table_name):
    dataframe.write.jdbc(url=config.URL.value,
                         table=table_name, 
                         mode='append', 
                         properties=config.PROPS.value)

def update_data(config, dataframe, table_name):
    dataframe.write.jdbc(url=config.URL.value, 
                         table=table_name, 
                         mode='overwrite', 
                         properties=config.PROPS.value)