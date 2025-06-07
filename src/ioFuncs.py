import kagglehub
import os
import pandas as pd
import json
from gensim.models import LdaModel


def read_raw_main(Data_path):

    dataset_name = "10Mar2025.json"
    dataset_path = os.path.join(Data_path, dataset_name)

    if os.path.isfile(dataset_path):
        with open(dataset_path, 'r') as f:
            data = json.load(f)
        print("Dataset loaded from drive.")
    else:
        print("Downloading from Kaggle ...")
        fort_list_path = kagglehub.dataset_download("jarredgaudineer/social-media-posts-fortune-1000-companies")
        print("Dataset downloaded from kaggle.")

        # Load the wanted file
        temp_path = os.path.join(fort_list_path, "10Mar2025.json")
        
        with open(Data_path, 'r') as f:
            data = json.load(f)

        # Save the data into drive
        with open(dataset_path, 'w') as f:
            json.dump(data, f)
        print("Dataset saved to drive.")

    return data

def read_raw_complement():
    # The complementary Dataset
    dataset_name = "fortune1000_2024.csv.csv"
    dataset_path = os.path.join(Data_path, dataset_name)

    if os.path.isfile(dataset_path):
        fortune_company_list = pd.read_csv(dataset_path)
        print("Dataset loaded from drive.")
    else:
        fort_list_path = kagglehub.dataset_download("jeannicolasduval/2024-fortune-1000-companies")
        print("Dataset downloaded from kaggle.")
        fortune_company_list = pd.read_csv(os.path.join(fort_list_path, "fortune1000_2024.csv"))
        fortune_company_list.to_csv(dataset_path)
        print("Dataset saved to drive.")


def kaggle_save(dataset_name, data_path):
    print("Downloading from Kaggle ...")
    temp_path = kagglehub.dataset_download("khalilvandian/enriched-social-media-posts-fortune-1000-companies")
    temp_dataset_path = os.path.join(temp_path, dataset_name)

    enriched_data = pd.read_csv(temp_dataset_path)

    # Save to local data dir
    dataset_path = os.path.join(data_path, dataset_name)
    enriched_data.to_csv(dataset_path)

    return enriched_data


def read_enriched(data_path):
    dataset_name = "enriched_social-media-posts-fortune-1000-companies_data.csv"
    dataset_path = os.path.join(data_path, dataset_name)

    if os.path.isfile(dataset_path):
        enriched_data = pd.read_csv(dataset_path)
        print('Loaded file from data dir.')

    else:
        enriched_data = kaggle_save(dataset_name, data_path)

    return enriched_data

def read_preprocessed(data_path, notebook_env):

    if notebook_env == "test":
        dataset_name = "complete_preprocessed_companyData.csv"
    else:
        dataset_name = "complete_preprocessed_companyData_allData.csv"

    dataset_path = os.path.join(data_path, dataset_name)

    if os.path.isfile(dataset_path):
        temp_df = pd.read_csv(dataset_path)
        print("Dataset loaded from drive.")
        return temp_df
    else:
        return None
    
def read_tokenized(data_path, notebook_env):
    if notebook_env == "test":
        dataset_name = "spacy_tokenized_sample.pkl"
    else:
        dataset_name = "spacy_tokenized_allData.pkl"

    dataset_path = os.path.join(data_path, dataset_name)

    if os.path.isfile(dataset_path):
        tokenized_texts = pd.read_pickle(dataset_path)
        print("Loaded from drive.")
        return tokenized_texts
    else:
        return None

def load_lda_model(models_path):
    model_name = "GensimLdaModel_SpacyTokens_TopicCount20"
    # retrain with 20 topics or load back
    model_path_temp = os.path.join(models_path, model_name)

    if os.path.isfile(model_path_temp):
        lda_model = LdaModel.load(model_path_temp)
        return lda_model
    else:
        return None

if __name__ == "__main__":

    Data_path = "B:/Projects/BehavioralPsychology/Fortune_company_opinion_mining/Data"
    Models_path = "B:/Projects/BehavioralPsychology/Fortune_company_opinion_mining/Models"

    enriched_data = read_enriched(Data_path)
    print(enriched_data.head())
    print("Well, Well, Well!")



