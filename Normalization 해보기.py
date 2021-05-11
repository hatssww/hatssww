# 필요한 도구 import
from sklearn import preprocessing
import pandas as pd


# 파일경로 지정, 소수점 5번째 자리까지 출력 옵션 지정
PATIENT_FILE_PATH = './datasets/liver_patient_data.csv'
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# 데이터 파일을 pandas dataframe으로 변환
liver_patients_df = pd.read_csv(PATIENT_FILE_PATH)

# Normalization할 열들 dataframe으로 추출
features_to_normalize = ['Total_Bilirubin','Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase']
features_df = liver_patients_df[features_to_normalize]

# Normalization
scaler = preprocessing.MinMaxScaler()
normalized_data = scaler.fit_transform(features_df)
normalized_df = pd.DataFrame(normalized_data, columns=features_to_normalize)


# 결과
print(normalized_df.describe())