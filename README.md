#Embedding Models – From Text to Meaningful Vector Representations
1. Introduction
Computers process information numerically, while human language contains meaning and context. Embeddings convert text into numerical vectors so machines can compare and process meaning.
Basic Workflow:
Text → Embedding Model → Vector
2. What is an Embedding?
An embedding is a numerical representation of text that captures useful semantic information.
Example:
"I enjoy coding."
       ↓
Embedding Model
       ↓
[0.21, -0.45, 0.78, 0.12, ...]
A vector is simply an ordered list of numbers.
3. Embedding Dimension
The embedding dimension is the number of values in an embedding vector.
Model: all-MiniLM-L6-v2
Embedding Dimension: 384
Therefore, each sentence is converted into a vector containing 384 numerical values.
4. Sentence Transformers
A Sentence Transformer converts complete sentences into fixed-size numerical embeddings.
Input Sentence
      ↓
Tokenization
      ↓
Transformer Encoder
      ↓
Pooling
      ↓
Embedding Vector
The Transformer processes words in context, while pooling combines token representations into one vector representing the complete sentence.
5. Semantic Similarity
Semantic similarity compares sentences based on their meaning rather than only their exact words.
Example:
"I enjoy coding."
"I like programming."
These sentences have similar meanings, so their embeddings are expected to be relatively close.
Cosine similarity is used to compare the embedding vectors.
6. Cosine Similarity
Cosine similarity measures how closely two vectors are aligned.
The program calculates similarity between sentence embeddings and displays pairs whose similarity is above the selected threshold.
Example:
Sentence 1: I enjoy coding.
Sentence 2: I like programming.
Similarity: 0.xxxx
A higher value generally indicates that the embeddings are more closely aligned.
7. Model Used
all-MiniLM-L6-v2
It is a Sentence Transformer model used to generate sentence embeddings.
Embedding size: 384 dimensions
8. Applications of Embeddings
Embeddings are commonly used for:
Semantic Search
Retrieval-Augmented Generation (RAG)
Document Similarity
Question Matching
Recommendation Systems
Clustering
RAG Workflow
Documents
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vectors
    ↓
Vector Store

User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
LLM
9. Project Implementation
The Python program:
Loads the Sentence Transformer model.
Defines multiple sentences.
Converts sentences into embeddings.
Displays the embedding dimension.
Calculates cosine similarity.
Finds semantically similar sentence pairs.
Displays the similarity score.
10. Technologies Used
Python
Sentence Transformers
Scikit-learn
PyTorch
Python Libraries
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
11. Project Files
embedding model/
│
├── app.py
├── README.md
└── output.pdf
app.py: Contains the Python implementation for generating sentence embeddings and calculating cosine similarity.
output.pdf: Contains the screenshot of the program output.
12. Key Takeaways
Embeddings convert text into numerical vector representations.
Vector dimension is the number of values in the vector.
Sentence Transformers convert complete sentences into fixed-size embeddings.
Pooling combines token representations into a sentence-level vector.
Semantically similar sentences generally have closer embeddings.
Cosine similarity compares embedding vectors.
Embeddings are important for semantic search and RAG systems.