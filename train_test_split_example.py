import pandas as pd
from sklearn.model_selection import train_test_split

data = {'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
        'Marks': [35, 40, 45, 55, 60, 65, 70, 80]}
df = pd.DataFrame(data)

X = df[['Hours']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
print("Train data size:", X_train.shape)
print("Test data size:", X_test.shape)
