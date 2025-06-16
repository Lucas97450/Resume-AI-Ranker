from sentence_transformers import SentenceTransformer
from pathlib import Path
import pickle
import utils

def similarity(cvs_path, jobs_path):
    cvs_folder = Path(cvs_path)
    cvs_files = cvs_folder.glob("*.pkl")
    jobs_folder = Path(jobs_path)
    jobs_files = jobs_folder.glob("*.pkl")
        
    for cvs_file in cvs_files:
        for name, vec in utils.load_embeddings_items(cvs_file):
            print(name ,  vec.shape)


    for jobs_file in jobs_files:
        for name, vec in utils.load_embeddings_items(jobs_file):
            print(name ,  vec.shape)
