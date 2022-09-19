from datetime import datetime
import json
from infra.logger import get_logger

from infra.util import cal_std_day, execute_rest_api
from infra.hdfs_client import get_client


class CoronaApiExtractor:
    # 클래스 = 데이터 + 함수
    # class method, static method
    # instance method

    # 접근제한자
    # public, protected,    private
    #       , __메서드, 변수  __메서드, __변수

    URL = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api'
    SERVICE_KEY = 'm6fI67lUoycfS42U8TRjC2cthLpZZSzm1/C26exYUqj1G/T9sbdjEnmTEb8UlhcyaBWYsLnB1gbuBCbHpg5xNg=='
    FILE_DIR = '/corona_data/patient/'


    @classmethod
    def extract_data(cls, befor_cnt=1):
        
        for i in range(1, befor_cnt+1):
            params = cls.__create_param(i)
            
            try:
                res = execute_rest_api('get', cls.URL, {}, params)
                file_name = 'corona_patient_' + params['std_day'] + '.json'
                cls.__upload_to_hdfs(file_name, res)

            except Exception as e:
                log_dict = cls.__create_log_dict(params)
                cls.__dump_log(log_dict, e)

    @classmethod
    def __upload_to_hdfs(cls, file_name, res):
        get_client().write(cls.FILE_DIR + file_name, res, encoding = 'utf-8', overwrite=True)
    

    @classmethod
    def __create_param(cls, before_day):
        return {
            'serviceKey':cls.SERVICE_KEY,
            'pageNo':'1',
            'numOfRows':'500',
            'apiType':'JSON',
            'std_day':cal_std_day(before_day)
        }


    @classmethod
    def __dump_log(cls, log_dict, e):
        log_dict['err_msg'] = e.__str__()
        log_json = json.dumps(log_dict, ensure_ascii = False)
        get_logger('coronaEXtractor').error(log_json)

    @classmethod
    def __create_log_dict(cls, params):
        log_dict = {
                    'is_success':'Fail',
                    'type':'corona_patient',
                    'std_day':params['std_day'],
                    'params':params
            }
        
        return log_dict