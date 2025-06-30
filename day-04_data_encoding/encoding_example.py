import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample data
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})

# Label Encoding
label_encoder = LabelEncoder()
df['Color_Label'] = label_encoder.fit_transform(df['Color'])

# One-Hot Encoding
one_hot = pd.get_dummies(df['Color'], prefix='Color')
df = pd.concat([df, one_hot], axis=1)

print(df)
