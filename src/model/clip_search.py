from transformers.models.clip.modeling_clip import CLIPModel
from transformers import CLIPModel
import fiftyone.brain as fob

class SearchModel:
    def __init__(self, dataset, model_path) -> None:
        self.model: CLIPModel = CLIPModel.from_pretrained(model_path)

        fob.compute_similarity(
            dataset, 
            model=self.model,
            embeddings="clip_embeddings",
            brain_key="clip_sim" 
        )

        fob.compute_visualization(dataset,
            embeddings="clip_embeddings", 
            method="umap", 
            brain_key="clip_vis"
        )