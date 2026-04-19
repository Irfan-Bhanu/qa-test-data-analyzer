**Week 6 – Machine Learning for Testing**
**Goal**

Apply Machine Learning techniques to improve test efficiency, detect failures, and prioritize test execution.

**Concepts Covered**
Supervised Learning (Classification)
Unsupervised Learning (Anomaly Detection)
Feature Engineering (Date, Module, Execution Time)
Model Evaluation Metrics:
Accuracy
Precision
Recall
F1 Score
Confusion Matrix Interpretation

**Tech Stack**
Python
Pandas
Scikit-learn
Matplotlib

**Tasks & Implementation**
1. Predict Pass/Fail (Beginner ML)
Used Logistic Regression
Converted categorical data using encoding
Evaluated using classification metrics

2. Decision Tree (Model Understanding)
Built rule-based model
Visualized decision paths
Understood feature impact

3. Random Forest (Advanced Model)
Used multiple trees for better accuracy
Reduced overfitting
Extracted feature importance

4. Bug-Prone Module Analysis
Grouped data by module
Calculated failure rate
Ranked modules by risk

5. Anomaly Detection
Used Isolation Forest
Detected unusual test executions


**Key Learnings**
ML can improve testing efficiency
Data quality directly impacts model performance
Recall is critical in testing (catching failures)
Feature engineering is essential for better predictions
ML helps move from reactive → proactive testing

**Workflow**
Test Data → Preprocessing → Model Training → Evaluation → Prediction → Insights
**Files Included**
Week6-ML in testing.ipynb
testdata.xlsx

**Future Improvements**
Increase dataset size
Handle class imbalance
Hyperparameter tuning
Integrate with Selenium automation
Real-time test prioritization in CI/CD
