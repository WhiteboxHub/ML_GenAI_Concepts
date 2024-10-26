# Mistral API Document Retrieval and Evaluation

This README.md provides a comprehensive overview, setup instructions, usage guidance, and example output to help users understand and effectively use the script.

This script performs document retrieval, response generation, and evaluation using the Mistral API, FAISS for similarity search, and evaluation metrics including Precision@K, ROUGE, and BLEU.

## Requirements

Before running the script, ensure the following dependencies are installed:

```bash
pip install requests numpy faiss-cpu scikit-learn rouge-score nltk
