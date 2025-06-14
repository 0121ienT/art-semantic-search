import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from fiftyone.core.session.session import Session
from fiftyone.core.collections import SampleCollection
import fiftyone as fo
from src.data import Dataset
from src.model import SearchModel
from src.config import data_setting, search_model_path, data_path
from dotenv import load_dotenv

load_dotenv()

DATASET_NAME = "wikiart_cached"
EMBEDDINGS_PATH = "cached_embeddings.npy"

# if "wikiart_cached" in fo.list_datasets():
#     fo.delete_dataset("wikiart_cached")

if DATASET_NAME in fo.list_datasets():
    print(f"Loading cached dataset '{DATASET_NAME}'...")
    dataset = fo.load_dataset(DATASET_NAME)
else:
    if "wikiart" in fo.list_datasets():
        fo.delete_dataset("wikiart")
    print("Downloading and caching dataset...")
    dataset_ins = Dataset(model_id=data_path, **data_setting)
    dataset: SampleCollection = dataset_ins.download()
    # dataset_ins.similarity_computing()
    dataset.name = DATASET_NAME
    dataset.persistent = True
    dataset.save()
    print("Dataset cached.")

# search_model: SearchModel = SearchModel(model_path=search_model_path, dataset=dataset)

print("Launching FiftyOne app...")
session: Session = fo.launch_app(dataset=dataset)
session.wait()