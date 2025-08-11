## Self-Introduction

Hello, my name is **Magham Sai Dhanush**, and I recently completed my **B.Tech in Computer Science and Engineering (Data Science)** from **Rajeev Gandhi Memorial College of Engineering & Technology, Andhra Pradesh** with a CGPA of **7.16**.

I am passionate about **Machine Learning, Data Science, and Generative AI**, with hands-on experience in building **classification models, NLP applications, and RAG-based AI chatbots**. My technical expertise includes **Python, SQL, Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch, LangChain, and FastAPI**, along with skills in **EDA, feature engineering, model tuning, and deployment**.

During my internship at **AIML LABS Solutions Pvt Ltd**, I worked on projects like **a Generative AI-powered customer support chatbot** and **a credit card fraud detection model**, which helped me strengthen my skills in **vector databases, embeddings, cloud deployment, and CI/CD automation**.

I am a **quick learner**, **detail-oriented**, and eager to contribute my **technical knowledge** and **creativity** to innovative AI and ML projects that make a real-world impact.

# Detailed Project Explanations

---

## **Project 1: Generative AI for Data Science – Intelligent Customer Support Chatbot**

### **Problem Statement**
In many companies, customer support teams spend significant time answering repetitive queries from product manuals and FAQs. This leads to delays, inconsistent responses, and high operational costs.  
The goal was to develop an AI chatbot capable of instantly providing accurate, context-aware answers to customer queries, thereby reducing human workload and improving customer satisfaction.

---

### **Motivation**
- Customers often abandon queries if response times are slow.
- Human agents get overwhelmed with repetitive questions, leaving less time for complex issues.
- Generative AI with Retrieval-Augmented Generation (RAG) can bridge the gap between structured manuals and conversational support.

---

### **Technologies Used**
- **Programming:** Python
- **Libraries & Frameworks:** LangChain, GPT-3.5 Turbo, Hugging Face Transformers, FAISS, FastAPI
- **Tools:** Docker, Git, Jupyter Notebook
- **Deployment:** Cloud environment (AWS / Azure)

---

### **Detailed Approach**
1. **Data Collection & Preprocessing**
   - Gathered company product manuals, FAQs, and policy documents (PDF, TXT, DOCX formats).
   - Used LangChain’s document loaders to extract raw text.
   - Cleaned and normalized text by removing special characters, redundant spaces, and HTML tags.

2. **Chunking & Embedding Generation**
   - Split documents into small, semantically meaningful chunks (around 500–1000 characters).
   - Generated embeddings using **Hugging Face Sentence Transformers** for vector representation.

3. **Vector Database Creation**
   - Stored the embeddings in **FAISS**, an efficient vector store for similarity search.
   - Indexed chunks for fast retrieval during query execution.

4. **Retriever-LLM Integration**
   - Used LangChain’s RetrievalQA chain to connect the FAISS retriever with **OpenAI GPT-3.5 Turbo**.
   - When a user asks a question:
     1. Retriever searches FAISS for relevant chunks.
     2. GPT-3.5 Turbo uses retrieved chunks as context to generate a coherent, factual answer.

5. **API Development**
   - Built a REST API using **FastAPI** to expose chatbot functionality.
   - Created endpoints for querying and receiving responses in JSON format.

6. **Deployment**
   - Containerized the application using **Docker**.
   - Deployed to a cloud environment for scalability and accessibility.

---

### **Challenges Faced**
- **Chunk Size Optimization:** Balancing between small chunks (better precision) and larger chunks (better context).
- **Latency Issues:** Optimized FAISS index and API calls to keep response time under 5 seconds.
- **Hallucinations:** Tuned prompt templates and retrieval scoring to ensure responses were factually correct.

---

### **Impact**
- Reduced average query resolution time from 2 minutes to **under 5 seconds**.
- Achieved an **accuracy rate of ~90%** in internal QA testing.
- Lowered workload on support agents by **40%**, freeing them to focus on complex queries.

---

## **Project 2: Machine Learning Model Development – Credit Card Fraud Detection**

### **Problem Statement**
Credit card fraud is a major financial risk for banks and customers. The challenge lies in detecting fraudulent transactions in **real-time** from highly imbalanced datasets where fraud cases are less than 1% of all transactions.

---

### **Motivation**
- Prevent monetary losses and improve customer trust.
- Build a system that minimizes **false negatives** (missed fraud cases) while controlling **false positives** (blocking legitimate transactions).

---

### **Technologies Used**
- **Programming:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, SMOTE
- **Algorithms:** Random Forest, Logistic Regression, XGBoost
- **Deployment Tools:** FastAPI, Git, CI/CD pipeline

---

### **Detailed Approach**
1. **Data Exploration & Understanding**
   - Analyzed transaction dataset containing features such as transaction amount, time, and anonymized numerical features (V1–V28).
   - Identified severe **class imbalance** (~0.17% fraud cases).

2. **Data Preprocessing**
   - Handled missing values and standardized numerical features using **StandardScaler**.
   - Created new features like:
     - **Transaction hour of the day** (to detect unusual time patterns).
     - **Transaction frequency per card** (to detect sudden bursts of activity).

3. **Handling Class Imbalance**
   - Applied **SMOTE (Synthetic Minority Oversampling Technique)** to oversample fraudulent cases and balance the dataset.

4. **Model Training**
   - Tried multiple models:
     - Logistic Regression (baseline)
     - Random Forest
     - XGBoost
   - Selected **Random Forest** for its high precision and recall balance.

5. **Model Evaluation**
   - Used evaluation metrics suited for imbalanced data:
     - **Precision, Recall, F1-score**
     - **AUC-PR** (Area Under Precision-Recall Curve)
   - Final Model Performance:
     - **F1-score:** 0.92
     - **Recall:** 0.88
     - **Precision:** 0.90

6. **Deployment**
   - Developed an inference API using **FastAPI** for integration into banking applications.
   - Built a CI/CD pipeline to automatically retrain the model periodically with new data.

---

### **Challenges Faced**
- **Severe Class Imbalance:** Required careful sampling to avoid overfitting on minority class.
- **Feature Selection:** Needed to ensure engineered features added predictive value.
- **Model Drift:** Added scheduled retraining to maintain accuracy over time.

---

### **Impact**
- Enabled near **real-time fraud detection** for incoming transactions.
- Reduced false negatives, preventing significant financial losses.
- Provided an explainable ML model, improving trust with stakeholders.
