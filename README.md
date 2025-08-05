# Chat_Based_Sentiment_Analysis
This is a project that I completed during my internship period at DIIGOO.

The methodology for developing the Chat-Based Sentiment Analysis System involves a series of well-defined steps, from data preparation to model evaluation. The focus is on using machine learning techniques—particularly the XGBoost algorithm—to accurately classify chat messages into positive, negative, or neutral sentiments.
1. Data Collection:
• Here a labelled dataset is typically used in which there are two columns known as text, Sentiment or similar typos.
• Dataset: “DATASET.csv” or similar names.
o Dataset size: 6000+ rows.
• Balanced distribution across all classes (positive, negative, neutral).
• Save the dataset to a .csv extension for easy processing.
2. Data Preprocessing:
• Text cleaning: remove the links, remove unnecessary symbols, remove numbers, remove special characters.
• Lower Case : Convert the string to the lower case,
• Stop words removal: remove the stop words.
• Handel NULL values: use some techniques to fill the NULL values or if the NULL values are to high then the model may not be able to correctly identify the sentiment.
3. Label Encoding:
• Converting the Textual sentiment into numerical value:
o Positive: 1
o Negative: 2
o Neutral: 3
• Typically this is done by LableEncoder.
4. Feature Extraction:
• Use TF-IDF Vectorization to convert the cleaned text into numerical feature vectors suitable for model training.
5. Data splitting:
• Split the dataset into traing_set and Testing_set typically the amount of data in training and testing set would be 80% and 20% respectively.
• The splitting is done using train_test_split().
6. Model building:
• Train the XGBoost Classifier on the training data.
• XGBoost is selected for its ability to handle structured data efficiently and its performance on classification tasks.
• Parameters such as “use_label_encoder=False and eval_metric='mlogloss'” are commonly used.
7. Model evaluation:
• Evaluate the trained model using metrics such as:
o Accuracy Score
o Classification Report (Precision, Recall, F1-score)
8. User Input and Prediction
• The final system allows real-time sentiment prediction from user-input chat messages.
• The user’s message is pre-processed and vectorized, then passed to the trained XGBoost model to output the predicted sentiment.
