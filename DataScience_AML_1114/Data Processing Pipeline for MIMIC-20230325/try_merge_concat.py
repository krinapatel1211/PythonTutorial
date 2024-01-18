import pandas as pd
from my_functions import find_duplicates, find_pivot


if __name__ == '__main__':
    # reading a table using a relative path
    patients = pd.read_csv('./MIMIC-Data/PATIENTS.csv')
    admission = pd.read_csv('./MIMIC-Data/ADMISSION_NONOVERLAPPING.csv')
    admission = admission.drop_duplicates(subset=['subject_id'], keep='last')
    print('shape of patients: ', patients.shape)
    print('shape of admission: ', admission.shape)
    print('Is there any duplicate values for subject_id in patients? ', find_duplicates(input_df=patients, column_name='subject_id'))
    print('Is there any duplicate values for subject_id in admission? ', find_duplicates(input_df=admission, column_name='subject_id'))

    merged_table = pd.merge(left=patients, right=admission, how='inner', on=['subject_id'])
    print('shape of merged_table: ', merged_table.shape)
    merged_table.to_csv('merge_table.csv', index=False)

    chart_table = pd.read_csv('./MIMIC-Data/CHARTEVENTS.csv', usecols=['subject_id', 'itemid', 'charttime', 'value'])
    input_table = pd.read_csv('./MIMIC-Data/INPUTEVENTS_MV.csv', usecols=['subject_id', 'itemid', 'storetime', 'amount'])
    input_table = input_table.rename(columns={"amount": "value", "storetime": "charttime"})
    print(chart_table.columns)
    print(input_table.columns)
    contact_table = pd.concat([chart_table, input_table], sort=False)
    contact_table.to_csv('concat_data.csv', index=False)



