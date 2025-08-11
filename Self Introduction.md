## Self-Introduction

Hello, my name is **Magham Sai Dhanush**, and I recently completed my **B.Tech in Computer Science and Engineering (Data Science)** from **Rajeev Gandhi Memorial College of Engineering & Technology, Andhra Pradesh** with a CGPA of **7.16**.

I am passionate about **Machine Learning, Data Science, and Generative AI**, with hands-on experience in building **classification models, NLP applications, and RAG-based AI chatbots**. My technical expertise includes **Python, SQL, Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch, LangChain, and FastAPI**, along with skills in **EDA, feature engineering, model tuning, and deployment**.

During my internship at **AIML LABS Solutions Pvt Ltd**, I worked on projects like **a Generative AI-powered customer support chatbot** and **a credit card fraud detection model**, which helped me strengthen my skills in **vector databases, embeddings, cloud deployment, and CI/CD automation**.

I am a **quick learner**, **detail-oriented**, and eager to contribute my **technical knowledge** and **creativity** to innovative AI and ML projects that make a real-world impact.


## Project 1: Generative AI for Data Science – Intelligent Customer Support Chatbot

**Objective:**  
To build an AI-powered customer support chatbot capable of providing instant, accurate responses to user queries by retrieving information from company product manuals and FAQs.

**Technologies Used:**  
- **Programming:** Python  
- **Frameworks/Libraries:** LangChain, GPT-3.5 Turbo, Hugging Face Transformers, FastAPI  
- **Databases:** FAISS (Vector Store)  
- **Other Tools:** Docker, Git, Cloud Deployment (AWS/Azure)  

**Approach & Implementation:**  
1. **Data Ingestion & Processing**  
   - Collected product manuals, FAQs, and support documents in multiple formats (PDF, TXT, DOCX).  
   - Used a document loader in LangChain to read and preprocess text.  

2. **Text Chunking & Embedding Generation**  
   - Split documents into smaller, meaningful chunks to improve retrieval accuracy.  
   - Generated vector embeddings using Hugging Face Sentence Transformers.  

3. **Vector Store Indexing**  
   - Stored embeddings in **FAISS** for fast similarity searches during queries.  

4. **Retriever-LLM Integration**  
   - Integrated FAISS retriever with GPT-3.5 Turbo via LangChain’s RetrievalQA chain to generate context-aware answers.  

5. **API Development & Deployment**  
   - Created REST API endpoints using **FastAPI** to handle user queries.  
   - Containerized the application using **Docker** and deployed it to the cloud for scalability.  

**Impact:**  
- Reduced human agent workload by 40%.  
- Achieved response accuracy of ~90% in internal testing.  
- Improved average query resolution time from 2 minutes to under 5 seconds.

---

## Project 2: Machine Learning Model Development – Credit Card Fraud Detection

**Objective:**  
To develop a classification model that detects fraudulent credit card transactions from a highly imbalanced dataset.

**Technologies Used:**  
- **Programming:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, SMOTE, Matplotlib, Seaborn  
- **Modeling:** Random Forest, Logistic Regression, XGBoost  

**Approach & Implementation:**  
1. **Exploratory Data Analysis (EDA)**  
   - Analyzed transaction patterns, feature distributions, and correlation between variables.  
   - Identified class imbalance (fraud cases < 1% of total).  

2. **Data Preprocessing & Feature Engineering**  
   - Standardized numeric features using StandardScaler.  
   - Created new time-based features (e.g., transaction hour, day of week).  

3. **Handling Class Imbalance**  
   - Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to balance dataset.  

4. **Model Selection & Training**  
   - Trained multiple models (Logistic Regression, Decision Trees, Random Forest, XGBoost).  
   - Selected **Random Forest** due to best trade-off between precision and recall.  

5. **Model Evaluation**  
   - Used **F1-score, Precision, Recall, and AUC-PR** as evaluation metrics.  
   - Achieved F1-score of 0.92 and Recall of 0.88 for fraud cases.  

6. **Deployment Pipeline**  
   - Automated model retraining and deployment using a CI/CD pipeline.  
   - Exposed model inference through an API for integration with banking systems.  

**Impact:**  
- Significantly reduced false negatives, minimizing financial losses.  
- Enabled near real-time fraud detection for incoming transactions.
