#%%
import pandas as pd

#%%

dataSetDF = pd.read_csv('./dataSet.csv')



# %%
dataSetDF = dataSetDF.drop(columns=["id"])

# %%
dataSetDF.head()

# %%
dataSetDF["Amount"].describe()

# %%
dataSetDF.dtypes

# %%
dataSetDF.dtypes.value_counts()

# %%
dataSetDF["Amount"].apply(type)

# %%
type('a')

# %%
dataSetDF.select_dtypes("object").apply(pd.Series.nunique, axis = 0)

# %%
#multiArray = [
#    [0,1,2], #Axis1
#    [3,4,5], #Axis2
#    [6,7,8]  #Axis3
#]

#%%
# def genderToInt(gender):
def genderToInt(gender: str) -> int:
    if gender == "M":
        return 0
    else:
        return 1

#%%
dataSetDF["Gender"].apply(genderToInt)

# %%
dataSetDF["Gender"] = dataSetDF["Gender"].apply(genderToInt)

# %%
dataSetDF.dtypes