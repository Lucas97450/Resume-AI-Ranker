from sentence_transformers import SentenceTransformer
from pathlib import Path
import pickle
import utils

def similarity(cvs_path, jobs_path):
    cvs_folder = Path(cvs_path)
    cvs_files = cvs_folder.glob("*.pkl")
    jobs_folder = Path(jobs_path)
    jobs_files = jobs_folder.glob("*.pkl")

    cv_names = []
    cv_vectors = []

    for cvs_file in cvs_files:
        for name, vec in utils.load_embeddings_items(cvs_file):
            cv_names.append(name)
            cv_vectors.append(vec)

    job_names = []
    job_vectors = []

    for jobs_file in jobs_files:
        for name, vec in utils.load_embeddings_items(jobs_file):
            job_names.append(name)
            job_vectors.append(vec)


    vectors_similarity = []

    for job in job_vectors:
        for cv in cv_vectors:
            cos_sim = utils.cos_sim(job, cv)
            vectors_similarity.append(cos_sim)

    results = list(zip(cv_names, vectors_similarity))
    results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

    for name, score in results_sorted:
        print(f"{name} : {score:.4f}")

similarity("embedded_files/cvs", "embedded_files/jobs")
