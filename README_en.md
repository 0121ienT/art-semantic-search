# Artistic Style Analysis with Multimodal Embeddings

This repository explores the analysis of artistic styles in images using multimodal embeddings and computed attributes. Leveraging the **WikiArt dataset** from the 🤗 Hugging Face Hub, we utilize **FiftyOne** for data analysis and visualization, alongside a pre-trained **CLIP model** from 🤗 Transformers for generating embeddings. The project dives into unstructured data analysis in several exciting ways.

## Features

- **Image Similarity Search and Semantic Search**: Generate multimodal embeddings for images using CLIP and index the dataset for fast, unstructured searches.
- **Clustering and Visualization**: Cluster images by artistic style using embeddings and visualize the results with UMAP dimensionality reduction.
- **Uniqueness Analysis**: Assign uniqueness scores to images based on their similarity to others in the dataset.
- **Image Quality Analysis**: Compute metrics like brightness, contrast, and saturation, and explore their correlation with artistic styles.

## Dataset

The project uses the **WikiArt dataset**, a rich collection of artwork images, available via the 🤗 Hugging Face Hub.

## Tools and Libraries

- **FiftyOne**: For data loading, analysis, and visualization.
- **🤗 Transformers**: Provides the pre-trained CLIP model for embedding generation.
- **UMAP**: For dimensionality reduction and visualization of clustered embeddings.
- **Python**: Core programming language for the project.

## Getting Started

### Prerequisites

- Python 3.8+
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/artistic-style-analysis.git
   cd artistic-style-analysis
   ```

2. Install dependencies:
   ```bash
   pip install fiftyone transformers torch umap-learn
   ```

3. Download the WikiArt dataset using FiftyOne or Hugging Face Hub (instructions in the notebook).

### Usage

Run the Jupyter notebook `artistic_style_analysis.ipynb` to explore the full workflow:
```bash
jupyter notebook artistic_style_analysis.ipynb
```

The notebook includes detailed steps for:
- Loading and preprocessing the WikiArt dataset.
- Generating CLIP embeddings.
- Performing similarity searches, clustering, and uniqueness analysis.
- Visualizing results with UMAP and quality metrics.

## Example Results

- **Similarity Search**: Find images visually or semantically similar to a query image.
- **Clusters**: Group artworks by style (e.g., Impressionism, Abstract).
- **Uniqueness Scores**: Identify standout pieces in the dataset.
- **Quality Metrics**: Analyze how brightness and contrast vary across styles.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your ideas or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the FiftyOne team for their powerful data analysis tools.
- Gratitude to 🤗 Hugging Face for the WikiArt dataset and Transformers library.