from sentence_transformers import SentenceTransformer
from pathlib import Path
import pickle

def embed_all_text(folder, save_path):
    # Load a pretrained Sentence Transformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")
    cvs_folder = Path(folder)
    txt_files = cvs_folder.glob("*.txt")
    embeddings_dict = {}
    save_folder = Path(save_path)

    for txt_file in txt_files:
        text = txt_file.read_text(encoding="utf-8")
        embeddings = model.encode(text)
        print(embeddings.shape)
        embeddings_dict[txt_file.name] = embeddings
    print(embeddings_dict)


    # Save the dictionary 
    with open(save_path, "wb") as f:
        pickle.dump(embeddings_dict, f)
    
    return embeddings_dict
