import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot']  10
lst += ['human']  10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

encoder = OneHotEncoder(sparse=False)
onehot_column = encoder.fit_transform(data[['whoAmI']].values.reshape(-1,1))
encoded_columns_name = encoder.get_feature_names_out(['whoAmI'])
encoded_data = pd.DataFrame(onehot_column, columns = encoded_columns_name)

data = encoded_data
data.head()