from pyspark.sql.functions import col, ceil
from infra.jdbc import DataWarehouse, find_data, save_data

class CoPopuDensity:

    popu = find_data(DataWarehouse, 'loc')
    patients = find_data(DataWarehouse, 'corona_patients')

    @classmethod
    def save(cls):
        pop_patients = cls.__generate_data()
        save_data(DataWarehouse, pop_patients, 'CO_POPU_DENSITY')

    @classmethod
    def __generate_data(cls):
        pop_patients = cls.popu.join(cls.patients, on='loc') \
                    .select('loc'
                           ,ceil(col('population')/col('area')).alias('POPU_DENSITY')
                            ,'qur_rate'
                            ,'std_day') \
                    .orderBy(col('std_day'))
                    
        return pop_patients
