import pandas as pd

#load_data 
def load_data():
    job_posting_df = pd.read_csv("C:\\Users\\lenovo\\Documents\\ironhack\\IT trending jobs\\archive\\postings.csv")
    job_skills_df = pd.read_csv("C:\\Users\\lenovo\\Downloads\\archive\\jobs\\job_skills.csv")

    result = pd.merge(job_posting_df, job_skills_df)
    return result

#data_cleaning functions
