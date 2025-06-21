from typing import Any

search_model_path = "openai/clip-vit-base-patch32" # Tên mô hình clip
data_path = "huggan/wikiart" # Tên bộ dữ liệu

data_setting: dict[Any, Any] = {
    "format" : "parquet", # format của dữ liệu
    "classification_fields" : ["artist", "style", "genre"], # các trường dữ liệu quan trọng
    "max_samples" : 1000, # Số lượng ảnh được sử dụng
    "name" : "wikiart"
}