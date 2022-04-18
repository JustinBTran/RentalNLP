# Generic
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings, gc
warnings.filterwarnings("ignore")

# Tensorflow
import tensorflow as tf

# ktrain
import ktrain
from ktrain import text

# sklearn
from sklearn.model_selection import train_test_split

# Load
url = 'room-rental-ads.csv'
df = pd.read_csv(url, header='infer')

# Dropping Null Values
df.dropna(inplace=True)

# Total Records
print("Total Records: ", df.shape[0])

# Inspect
df.head()


# Data Split
target = ['Vague/Not']
data = ['Description']

X = df[data]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.1, random_state=42)

# Common Parameters
max_len = 500
batch_size = 6
learning_rate = 5e-5
epochs = 1

# Transformer Model
model_ = 'distilbert-base-uncased'
t_mod = text.Transformer(model_, maxlen=500, classes = [0,1])


'''Converting split data to list [so it can processed]'''
#train
X_tr = X_train['Description'].tolist()
y_tr = y_train['Vague/Not'].tolist()

#test
X_ts = X_test['Description'].tolist()
y_ts = y_test['Vague/Not'].tolist()


# Pre-processing training & test data
train = t_mod.preprocess_train(X_tr,y_tr)
test = t_mod.preprocess_train(X_ts,y_ts)

# Model Classifier
model = t_mod.get_classifier()

learner = ktrain.get_learner(model, train_data=train, val_data=test, batch_size=2)

# Train Model
learner.fit_onecycle(learning_rate, epochs)

# Evaluate
x = learner.validate(class_names=t_mod.get_classes())



model.save_pretrained("/Models/bert.cpkt")

# Garbage Collect
gc.collect()