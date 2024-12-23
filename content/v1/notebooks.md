---
title: RAG in LLMs
weight: 5
---

**Retrieval-Augmented Generation (RAG)** is a technique that enhances the capabilities of Large Language Models (LLMs) by integrating external knowledge sources during the generation process. Instead of relying solely on the information contained within the model's parameters, RAG allows the model to access and retrieve relevant data from external databases or documents to produce more accurate and contextually relevant responses.

#### Key Components of RAG:

- **Retriever:** Searches and retrieves relevant documents or data based on a given query.
- **Generator:** Uses the retrieved information to generate a response, combining it with the model's internal knowledge.

#### Benefits of RAG:

- **Enhanced Accuracy:** Incorporates up-to-date information not present in the model's training data.
- **Reduced Model Size:** Allows for smaller models since external data supplements the model's knowledge.
- **Improved Contextual Understanding:** Provides precise answers by leveraging specific, relevant data.

---

### Basic Concepts of Vector Embeddings

**Vector embeddings** are numerical representations of data—in this context, words or documents—that capture semantic meaning in a continuous vector space. Each word or piece of text is transformed into a high-dimensional vector, where similar meanings are placed closer together.

#### Important Points:

- **Dimensionality:** The number of dimensions in the vector space, typically ranging from 100 to 1,000.
- **Semantic Proximity:** Words or texts with similar meanings have vectors that are close in the vector space.
- **Embedding Models:** Algorithms like Word2Vec, GloVe, and transformer-based models generate these embeddings.

---

### Vector Databases

A **vector database** is a specialized data storage system designed to handle high-dimensional vector embeddings efficiently. It enables fast similarity searches and is essential for applications like semantic search and recommendation systems.

#### Features of Vector Databases:

- **Efficient Storage:** Optimized for storing large numbers of high-dimensional vectors.
- **Similarity Search Algorithms:** Implements algorithms for rapid nearest-neighbor searches.
- **Scalability:** Capable of handling growing datasets without significant performance loss.

---

### Semantic Search

**Semantic search** refers to searching for information based on the meaning and context rather than exact keyword matches. It leverages vector embeddings to understand the intent behind queries and retrieve results that are contextually relevant.

#### Characteristics:

- **Contextual Understanding:** Interprets the user's intent to provide meaningful results.
- **Enhanced Relevance:** Retrieves information that semantically matches the query, even if exact terms aren't present.
- **Use Cases:** Applied in search engines, chatbots, and information retrieval systems.

---

### Difference Between Semantic Search and Normal Similarity Search

- **Semantic Search:**

  - **Focus:** Understands the meaning and context behind queries and documents.
  - **Methodology:** Uses vector embeddings to capture semantic relationships.
  - **Results:** Provides contextually relevant results, improving accuracy.

- **Normal Similarity Search:**

  - **Focus:** Relies on surface-level similarities like keyword frequency or exact matches.
  - **Methodology:** Uses traditional text matching algorithms (e.g., TF-IDF).
  - **Results:** May miss contextually relevant information due to lack of semantic understanding.

---

### Using ChromaDB as Our Vector Storage

For this workshop, we will use **ChromaDB** as our vector storage.

#### Why ChromaDB?

- **Ease of Use:** Runs directly from Python without complex setups.
- **Quick Deployment:** The fastest option to get started with vector storage.
- **Flexibility:** Suitable for experimentation and integrates well with Python-based projects.

#### Alternative Options:

- While there are many other vector databases available, ChromaDB is ideal for our purposes due to its simplicity and speed. It allows us to focus on learning concepts without the overhead of configuring more complex systems.

---

### Generating Embeddings

We will explore two methods for generating embeddings:

#### 1. Using the Default Embedding Available with ChromaDB

- **Built-in Embeddings:** ChromaDB provides default embedding functions that are easy to use.
- **Immediate Start:** Enables quick testing and understanding of vector storage and retrieval.
- **Usage:** Ideal for initial experiments and learning basic operations.

#### 2. Using a Model Loaded Through Ollama for Generating Embeddings

- **Custom Embeddings:** By loading a model through **Ollama**, we can generate embeddings tailored to our specific data.
- **Advantages:**

  - **Customization:** Better control over the embedding process.
  - **Enhanced Performance:** Potentially improved accuracy and relevance in search results.

- **Implementation:**

  - **Integration with Ollama:** Utilize Ollama to load the desired embedding model.
  - **Embedding Generation:** Use the loaded model to generate embeddings, which are then stored in ChromaDB.

---
