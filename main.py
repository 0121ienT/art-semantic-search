# from src.model import SearchModel
from fiftyone.core.session.session import Session
from fiftyone.core.collections import SampleCollection
# from src.data.data import Dataset

import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F
from src.data import Dataset
from src.model import SearchModel
from src.config import data_setting, search_model_path, data_path

dataset_ins: Dataset = Dataset(model_id = data_path, **data_setting)

dataset: SampleCollection = dataset_ins.download()

search_model: SearchModel = SearchModel(model_path=search_model_path, dataset=dataset)

session: Session = fo.launch_app(dataset = dataset)

session.wait()