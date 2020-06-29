#%%
import pandas as pd

# %%
dataSetOneDF = pd.read_csv('./dataOne.csv')

# %%
# def genderToInt2(gender):
def genderToInt2(gender: str) -> int:
    if gender == "Male":
        return 0
    else:
        return 1


# %%
dataSetOneDF["gender"] = dataSetOneDF["gender"].apply(genderToInt2)


# %%
dataSetOneDF.insert(5,"UserName","")

# %%
dataSetOneDF.insert(6,"Domain","")

# %%
dataSetOneDF.dtypes

# %%
def emailUser(email: str)-> str:
    split = email.split("@")
    return split [0]

def emailDomain(email: str) -> str:
    split = email.split("@")
    return split[1]

dataSetOneDF["UserName"] = dataSetOneDF["email"].apply(emailUser)

dataSetOneDF["Domain"] = dataSetOneDF["email"].apply(emailDomain)

