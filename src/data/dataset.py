import fiftyone.brain as fob
import fiftyone.utils.huggingface as fouh
from typing import Any
from fiftyone.core.collections import SampleCollection

class Dataset:
    def __init__(self, model_id : str, **kwarg) -> None:
        self.model_id = model_id
        self.metadata = kwarg

        self.dataset = None

    def download(self) -> SampleCollection:
        if self.dataset == None:
            self.dataset = fouh.load_from_hub(
                repo_id=self.model_id,
                format= self.metadata["format"],
                classification_fields=self.metadata["classification_fields"],
                max_samples=self.metadata["max_samples"],
                name=self.metadata["name"]
            )
        return self.dataset

    def similarity_computing(self) -> None:
        fob.compute_similarity(
            self.dataset,
            model="zero-shot-classification-transformer-torch",
            name_or_path="openai/clip-vit-base-patch32",
            embeddings="clip_embeddings",
            brain_key="clip_sim",
            batch_size=32,
        )

    def label(self, collumn) -> tuple[None, ...] | list[Any] | list[None] | None:
        try:
            return self.dataset.distinct(f"{collumn}.label")
        except Exception as e:
            print(f"You have face this error : {e}")