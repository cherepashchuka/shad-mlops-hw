import pandas as pd
import numpy as np

# Define column types
COLS_TO_SAVE = ['сумма', 'частота_пополнения', 'доход', 'сегмент_arpu', 'частота',
                'объем_данных', 'on_net', 'продукт_1', 'продукт_2', 'зона_1', 'зона_2',
                'секретный_скор', 'pack_freq', 'client_id']

def import_data(path_to_file):
    print('### Reading data ###')

    data = pd.read_csv(path_to_file)
    data = data[COLS_TO_SAVE]
    
    print('### Reading data -- Successful ###')

    return data
 
def run_preproc(input_data):
    print('### Preprocessing data ###')

    output_data = input_data.fillna(-999999)

    print('### Preprocessing -- Successful ###')

    return output_data