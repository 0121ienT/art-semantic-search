import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
os.environ["FIFTYONE_APP_USE_ELECTRON"] = "0"
import threading
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

# Khởi tạo dataset
if DATASET_NAME in fo.list_datasets():
    print(f"Loading cached dataset '{DATASET_NAME}'...")
    dataset = fo.load_dataset(DATASET_NAME)
else:
    if "wikiart" in fo.list_datasets():
        fo.delete_dataset("wikiart")
    print("Downloading and caching dataset...")
    dataset_ins = Dataset(model_id=data_path, **data_setting)
    dataset: SampleCollection = dataset_ins.download()
    dataset.name = DATASET_NAME
    dataset.persistent = True
    dataset.save()
    print("Dataset cached.")

# Biến toàn cục để lưu session và thread
current_session = None
current_thread = None
session_lock = threading.Lock()

def run_app(dataset):
    """Chạy FiftyOne app trong một thread riêng."""
    global current_session
    with session_lock:
        current_session = fo.launch_app(dataset=dataset, auto=False)
    current_session.wait()

def start_app(dataset):
    """Khởi động thread chạy FiftyOne app."""
    global current_thread
    if current_thread is None or not current_thread.is_alive():
        current_thread = threading.Thread(target=run_app, args=(dataset,))
        current_thread.start()
        print("FiftyOne app launched.")
    else:
        print("FiftyOne app is already running.")

def close_app():
    """Đóng FiftyOne app hiện tại."""
    global current_session
    with session_lock:
        if current_session is not None:
            current_session.close()
            current_session = None
            print("FiftyOne app closed.")
        else:
            print("No FiftyOne app is running.")

def reload_app(dataset):
    """Reload FiftyOne app."""
    close_app()
    start_app(dataset)
    print("FiftyOne app reloaded.")

if __name__ == "__main__":
    print("Starting FiftyOne app...")
    start_app(dataset)

    # Ví dụ: reload app sau một khoảng thời gian hoặc theo yêu cầu
    while True:
        user_input = input("Enter 'reload' to reload FiftyOne app or 'exit' to quit: ")
        if user_input.lower() == "reload":
            reload_app(dataset)
        elif user_input.lower() == "exit":
            close_app()
            break