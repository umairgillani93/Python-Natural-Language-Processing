from pyresparser import ResumeParser
import nltk
import spacy

nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')

# Cv information
data = ResumeParser("new_updated_CV.pdf").get_extracted_data()

# Extracting skills from Cv
print(data['skills'])
