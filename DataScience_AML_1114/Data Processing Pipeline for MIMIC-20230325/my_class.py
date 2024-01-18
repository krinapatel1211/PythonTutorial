import pandas as pd


class MIMIC:
    # to define the property of a class we need to use a predefined function called
    # "__init__(self)"
    # __init__(self) is a function that will be called each time you create an instance of your class
    def __init__(self, patient_data_path, admission_data_path, chart_data_path):
        # The instance MIMIC has a property called patient_data_path
        self.patient_data_path = patient_data_path

        # The instance MIMIC has a property called admission_data_path
        self.admission_data_path = admission_data_path

        # The instance MIMIC has a property called chart_data_path
        self.chart_data_path = chart_data_path

    @staticmethod
    def find_pivot(input_df, list_of_index, list_of_columns, value_column_name):
        # converts the input_df[value_column_name] to be str
        input_df[value_column_name] = input_df[value_column_name].astype(str)

        # extract the portion of the input_df that the column value_column_name is numeric
        input_df = input_df[input_df[value_column_name].apply(lambda x: x.isnumeric())]

        # converts the input_df[value_column_name] to be float
        input_df[value_column_name] = input_df[value_column_name].astype(float)

        # find the pivot tabple with the given the column, index, and value
        temp_df = pd.pivot_table(data=input_df, index=list_of_index, columns=list_of_columns,
                                 values=value_column_name).reset_index()
        return temp_df

    # the method are functions inside the class that either use the self as the input
    # or they are static
    def load_data(self):
        print('loading data...')
        patient_data = pd.read_csv(self.patient_data_path)
        admission_data = pd.read_csv(self.admission_data_path)

        # removing the duplicate 'subject_id'
        admission_data = admission_data.drop_duplicates(subset=['subject_id'], keep='last')
        print('merging patient information...')
        merged_patient_information = pd.merge(left=patient_data, right=admission_data, how='inner', on=['subject_id'])

        chart_data = pd.read_csv(self.chart_data_path)

        # pivot the chart data
        chart_data = self.find_pivot(input_df=chart_data, list_of_index=['subject_id', 'charttime'], list_of_columns=['itemid'], value_column_name='value')

        # merging the chart data with the merged patient data
        print('merging the chart data with the patient information...')
        final_table = pd.merge(left=chart_data, right=merged_patient_information, on=['subject_id'], how='inner')

        return final_table