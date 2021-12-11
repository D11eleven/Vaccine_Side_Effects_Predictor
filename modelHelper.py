import numpy as np
import pickle
import pandas as pd

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(age_group, sex, other_meds, history, prior_vax, allergies, vax_name, vax_dose):

        features_np = ['OTHER_MEDS', 'HISTORY', 'PRIOR_VAX', 'ALLERGIES', 'F', 'M', 'JANSSEN', 'MODERNA', 'PFIZER',
                    'VAX_DOSE_SERIES_1', 'VAX_DOSE_SERIES_2', '18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76-85', '86-95',
                    '96 +']

        user_input = np.zeros(len(features_np))

        age_idx = features_np.index(f'{age_group}')
        sex_idx = features_np.index(f'{sex}')
        vax_idx = features_np.index(f'{vax_name}')
        dose_idx = features_np.index(f'VAX_DOSE_SERIES_{vax_dose}')


        user_input[0] = other_meds
        user_input[1] = history
        user_input[2] = prior_vax
        user_input[3] = allergies
        user_input[sex_idx] = 1
        user_input[vax_idx] = 1
        user_input[dose_idx] = 1
        user_input[age_idx] = 1


        input_pred = [user_input]

        print("input_pred", input_pred)

        with open("final_regression_model.sav", "rb") as f:
            model = pickle.load(f)
        #     # print('hello')

        pred = model.predict(input_pred)
        print(pred)

        return pred

if __name__ == "__main__":
    results = ModelHelper.makePredictions('36-45','F',1, 1, 1, 1, 'PFIZER', '2')
    print(results)
    print('test')
    
