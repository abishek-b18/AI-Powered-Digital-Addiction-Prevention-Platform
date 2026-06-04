import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.DataFrame({
    'screen_time':[2,4,6,8,10,12],
    'social_media':[1,2,4,5,7,9],
    'gaming':[0,1,2,3,5,6],
    'sleep':[8,7,6,5,4,3],
    'risk':[0,0,1,1,2,2]
})

X = data[['screen_time',
          'social_media',
          'gaming',
          'sleep']]

y = data['risk']

model = DecisionTreeClassifier()
model.fit(X,y)

pickle.dump(
    model,
    open("addiction_model.pkl","wb")
)

print("Model Trained")