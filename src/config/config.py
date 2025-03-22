from typing import Any

search_model_path = "openai/clip-vit-base-patch32"
data_path = "huggan/wikiart"

data_setting: dict[Any, Any] = {
    "format" : "parquet",
    "classification_fields" : ["artist", "style", "genre"],
    "max_samples" : 1000,
    "name" : "wikiart"
}