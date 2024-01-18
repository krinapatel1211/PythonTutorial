from my_class import MIMIC


if __name__ == '__main__':
    # 1) An instance of the class is generated -> MIMIC()
    # 2) the properties of the class are assigned MIMIC(<properties>)
    # 3) the load_data method is called and the output of this function is returned
    data_instance = MIMIC(patient_data_path='./MIMIC-Data/PATIENTS.csv',
                          admission_data_path='./MIMIC-Data/ADMISSIONS.csv',
                          chart_data_path='./MIMIC-Data/CHARTEVENTS.csv')

    result = data_instance.load_data()
    result.to_csv('final_result.csv', index=False)