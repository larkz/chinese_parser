import re
import codecs
import numpy as np
import sys
import pandas as pd

ipath= u"hsk/hsk1.txt"

df = pd.read_csv(ipath, sep='\t', header=None)

# Define columns
df = df.rename(columns={0: "c_sim", 1: "c_trad", 2: "py1", 3: "py2", 4: "eng"})
df

nrow = df.shape[0]
rand = np.random.randint(nrow, size=1)[0]

df.iloc[[rand]][["c_sim"]]
df.iloc[[rand]][["c_trad"]]

df.iloc[[rand]][["eng"]]
df.iloc[[rand]][["py2"]]

def get_random_char():
    nrow = df.shape[0]
    rand = np.random.randint(nrow, size=1)[0]
    print(df.iloc[[rand]][["c_sim"]])
    print(df.iloc[[rand]][["c_trad"]])
    return 1

def get_random_eng():
    nrow = df.shape[0]
    rand = np.random.randint(nrow, size=1)[0]
    print(df.iloc[[rand]][["eng"]])
    print(df.iloc[[rand]][["py2"]])
    return 1



