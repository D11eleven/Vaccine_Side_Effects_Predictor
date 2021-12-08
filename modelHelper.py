import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
from wordcloud import WordCloud


def makePredictions(age_group, sex, other_meds, cur_ill, history, prior_vax, allergies, vax_name, vax_site, vax_dose):

    # File to Load (Remember to Change These)
    data = "../Resources/FINAL_CLEAN_FILE.csv"

    # read to dataframe
    data_df = pd.read_csv(data)

    X = data_df.drop(['VAERS_ID', 'SYMPTOM', 'ASSIGNED_GROUP', 'SEVERITY_LEVEL',
                    'HOSPITAL', 'DIED', 'L_THREAT', 'AGE_YRS', 'AGE_GROUP'], axis=1)

    with open(f'../knn_model.pickle', "rb") as f:
        model = pickle.load(f)

        features_np = ['OTHER_MEDS', 'CUR_ILL', 'HISTORY', 'PRIOR_VAX', 'ALLERGIES', 'F', 'M', 'JANSSEN', 'MODERNA', 'PFIZER',
                    'VAX_DOSE_SERIES_1', 'VAX_DOSE_SERIES_2', 'VAX_SITE_LA', 'VAX_SITE_RA', '18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76-85', '86-95',
                    '96 +']

        user_input = np.zeros(len(features_np))

        age_idx = features_np.index(f'{age_group}')
        sex_idx = features_np.index(f'{sex}')
        vax_idx = features_np.index(f'{vax_name}')
        dose_idx = features_np.index(f'VAX_DOSE_SERIES_{vax_dose}')
        site_idx = features_np.index(f'VAX_SITE_{vax_site}')

        user_input[0] = other_meds
        user_input[1] = cur_ill
        user_input[2] = history
        user_input[3] = prior_vax
        user_input[4] = allergies
        user_input[sex_idx] = 1
        user_input[vax_idx] = 1
        user_input[dose_idx] = 1
        user_input[age_idx] = 1
        user_input[site_idx] = 1

        pred_severity = model.predict([user_input])

        # # 5 people closest to user 1
        # tree = KDTree(X)
        # dist, ind = tree.query(user_input, k=200)

        # #convery ndarry to list
        # like_users = ind[0].tolist()
        # print(like_users)  # indices of 5 closest neighbors

        # # save nearest 50 neighbors symptoms as list for wordcloud
        # predicted_symptoms = data_df['ASSIGNED_GROUP'].iloc[like_users].tolist()
        # predicted_symptoms[:5]

        # #convert list to string and generate
        # unique_string=(" ").join(predicted_symptoms)

        # #create circle mask
        # x, y = np.ogrid[:300, :300]
        # mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
        # mask = 255 * mask.astype(int)

        # wordcloud = WordCloud(width = 1000, height = 500, mask=mask).generate(unique_string)
        # plt.figure(figsize=(15,8))
        # plt.imshow(wordcloud)
        # plt.axis("off")
        # #plt.savefig("your_file_name"+".png", bbox_inches='tight')
        # plt.show()
        # plt.close()

        return pred_severity


if __name__ == "__main__":
    results = makePredictions([[0, 0, 0, 1, 1, 1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0]])
    print(results)
