from pyresparser import ResumeParser
import pandas as pd
import nltk
import spacy
import os

nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')

# Cv information
data = ResumeParser("CVAsadjaved.pdf").get_extracted_data()

# Extracting skills from Cv
print(data['skills'])

# Creating Pandas DataFrame from parsed information
df = pd.DataFrame({key: pd.Series(value) for key, value in data.items()})
print(df.head())

# Creating csv file from pandas DataFrame
df.to_csv(os.getcwd() + "/resume1.csv")
