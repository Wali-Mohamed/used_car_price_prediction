

#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
# extra libraries
from scipy import stats
from scipy.stats import f_oneway, skew
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, OrdinalEncoder, MinMaxScaler
from sklearn.neural_network import MLPRegressor



import sklearn
sklearn.__version__


# In[24]:


def wrangle(path, scaling=False):
    df=pd.read_csv(path)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.drop(columns=['unnamed'], inplace=True)
    # Impute missing values
    
    # Derive column 'Brand' from column: 'title'
    df.insert(1, "brand", df.apply(lambda row : row["title"].split(" ")[0].upper(), axis=1))
    # drop title column
    df = df.drop(columns=['title'])
    # Fill in Service History
    df['service_history']=df['service_history'].fillna('unknown')
    # fill in with median
    df['previous_owners'].fillna(df['previous_owners'].median(), inplace=True)
    df['doors'].fillna(df['doors'].median(), inplace=True)
    df['seats'].fillna(df['seats'].median(), inplace=True)
    # Fill missing 'emission_class' values with the most frequent category (mode)
    df['engine']=df['engine'].fillna(df['engine'].mode()[0])
    df['emission_class']=df['emission_class'].fillna(df['emission_class'].mode()[0]) 
    # put all the contents in to lower case
    categorical = list(df.dtypes[df.dtypes == 'object'].index)
    numerical = list(df.dtypes[df.dtypes != 'object'].index)
    for col in categorical:
        df[col] = df[col].str.lower().str.replace(' ', '_')
    
    
        
    
    
    
    

    return df


# In[25]:


df = pd.read_csv('./data/used_cars_UK.csv')

# In[28]:


df.columns.to_list()


# In[29]:


df.columns = df.columns.str.lower().str.replace(' ', '_')


# In[30]:


# Fill in Service History
df['service_history']=df['service_history'].fillna('unknown')


# In[38]:


# Service History has 85% missing and unamed is just an extra column, so both dropped
df.drop(['unnamed:_0'], axis=1, inplace=True)

# columns with missing values
# Columns with Null Values
missing_cols=df.isnull().sum()[df.isnull().sum()!=0].index.to_list()
print(missing_cols)
# drop categorical missing columns
# drop engine
del missing_cols[1]
# drop emission_class
del missing_cols[3]


# In[41]:
# Check skewness and fill missing values with median if skewed
skewness=df[missing_cols].skew()
for column in missing_cols:
    if skewness[column] > 0.5:  # Right skewed
        print(f"{column} is positively skewed. Filling missing values with the median.")
        df[column].fillna(df[column].median(), inplace=True)
    elif skewness[column] < -0.5:  # Left skewed
        print(f"{column} is negatively skewed. Filling missing values with the median.")
        df[column].fillna(df[column].median(), inplace=True)
    else:
        print(f"{column} is not significantly skewed. Filling missing values with the median.")
        df[column].fillna(df[column].median(), inplace=True)


# Fill missing 'emission_class' values with the most frequent category (mode)
df['engine']=df['engine'].fillna(df['engine'].mode()[0])
df['emission_class']=df['emission_class'].fillna(df['emission_class'].mode()[0])


# In[49]:


print(df.isnull().sum())


# In[50]:


df.duplicated().sum()


# In[51]:


df.drop_duplicates(inplace=True)

# Derive column 'Brand' from column: 'title'
df.insert(1, "brand", df.apply(lambda row : row["title"].split(" ")[0].upper(), axis=1))
# drop title column
df = df.drop(columns=['title'])


categorical = list(df.dtypes[df.dtypes == 'object'].index)
numerical = [x for x in list(df.dtypes[df.dtypes != 'object'].index) if x !='price']
numerical, categorical


# In[66]:


for col in categorical:
    df[col] = df[col].str.lower().str.replace(' ', '_')


# In[67]:


df.duplicated().sum()


# In[78]:


duplicates = df[df.duplicated(keep=False)]
len(duplicates)


# In[79]:


df.isnull().sum()


# ### Building Model 

# #### Pipeline to combine dealing with categorical features, scaling and training.

# In[80]:


# Define Feature Types
ordinal_features = ['service_history', 'emission_class', 'engine']
nominal_features = ['brand', 'fuel_type', 'body_type', 'gearbox']
numeric_features = ['mileage(miles)', 'registration_year', 'previous_owners', 'doors', 'seats'] 

# Define the full list of engine sizes
engine_sizes = ['0.8l', '0.9l', '1.0l', '1.1l', '1.2l', '1.3l', '1.4l', '1.5l', '1.6l', '1.7l', 
                '1.8l', '1.9l', '2.0l', '2.1l', '2.2l', '2.3l', '2.4l', '2.5l', '2.6l', '2.7l', 
                '2.8l', '2.9l', '3.0l', '3.1l', '3.2l', '3.3l', '3.5l', '3.7l', '4.0l', '4.2l', 
                '4.3l', '4.4l', '4.8l', '5.0l', '5.5l', '6.3l']


# Define Preprocessing Steps
preprocessor = ColumnTransformer(
    transformers=[
        ('ordinal', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1, categories=[
            ['unknown', 'full'],  # Service history categories
            ['euro_1', 'euro_2', 'euro_3', 'euro_4', 'euro_5', 'euro_6'],  # Emission class categories
            engine_sizes  # Full list of engine sizes
        ]), ordinal_features),
        
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'), nominal_features),
        
        ('scale', StandardScaler(), numeric_features)  # Scaling for numerical features
    ],
    remainder='drop'  # Drop any columns not specified
)







# In[ ]:





# 
# <div style="background-color:#00008b;font-size:40px; color:white;">  Split</div>
# 

# In[81]:


df.reset_index(inplace=True, drop=True)
X = df.drop('price', axis=1)
y=df.price
#y=np.log1p(df.price)
X.shape


# In[82]:


X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.25, random_state=42)


# Create the pipeline with scaling and MLPRegressor
model_pipeline = make_pipeline(
    preprocessor,  # Scaling the data
    MLPRegressor(hidden_layer_sizes=(128, 64), random_state=1, max_iter=10000, solver='adam',  learning_rate_init=0.001)  # MLPRegressor
)

# Fit the model
print('Fitting the model the first neural network model')
model_pipeline.fit(X_train, y_train)

# Predict using the trained model
y_pred = model_pipeline.predict(X_val)

# Evaluate the model
RMSE = np.sqrt(mean_squared_error(y_val, y_pred))
r2 = r2_score(y_val, y_pred)  # R^2 Score
print(f'Root Mean Squared Error: {RMSE}')
print(f'R2 Score: {r2}')


# Create the pipeline with scaling and MLPRegressor
model_pipeline = make_pipeline(
    preprocessor,  # Scaling the data
    MLPRegressor(hidden_layer_sizes=(128, 64), random_state=1, max_iter=10000, solver='adam',  learning_rate_init=0.001)  # MLPRegressor
)
print('Fitting the model the final neural network model')
# Fit the model
model_pipeline.fit(X_train_full, y_train_full)

# Predict using the trained model
y_pred = model_pipeline.predict(X_test)

# Evaluate the model
RMSE = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)  # R^2 Score
print(f'Root Mean Squared Error: {RMSE}')
print(f'R2 Score: {r2}')


# In[109]:



import pickle  # Import the pickle module

# ... (previous code remains the same)


best_model = model_pipeline

# Save the best model to a file using pickle
with open('car_price_predictor/best_neural_network.pkl', 'wb') as file:
    pickle.dump(best_model, file)

print("Best model saved to 'best_neural_network.pkl'")
