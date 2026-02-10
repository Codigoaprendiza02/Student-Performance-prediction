# Student Performance Prediction using Machine Learning

## Project Overview
This project aims to predict a student’s exam performance based on academic habits, lifestyle factors, family background, and school-related attributes. Using exploratory data analysis and machine learning models, the project builds a regression-based prediction system and deploys it as an interactive web application using Streamlit.

The project demonstrates a complete machine learning lifecycle, from data understanding and analysis to model training, evaluation, and deployment.

---

## Problem Statement
Student academic performance is influenced by multiple factors such as study hours, attendance, prior academic history, family environment, motivation, and access to resources.  
The objective of this project is to build a predictive model that estimates a student’s **exam score** based on these factors.

---

## Dataset Description
- Total records: 6607
- Target variable: `Exam_Score`
- Feature types:
  - Numerical features (study hours, attendance, sleep hours, etc.)
  - Categorical features (gender, parental involvement, school type, motivation level, etc.)

### Key Features
| Feature | Description |
|------|-------------|
| Hours_Studied | Number of hours spent studying |
| Attendance | Attendance percentage |
| Sleep_Hours | Average daily sleep duration |
| Previous_Scores | Scores from previous exams |
| Tutoring_Sessions | Number of tutoring sessions attended |
| Physical_Activity | Hours spent in physical activities |
| Gender | Student gender |
| School_Type | Public or Private school |
| Parental_Involvement | Level of parental engagement |
| Internet_Access | Availability of internet |
| Motivation_Level | Student’s motivation level |
| Exam_Score | Final exam score (target variable) |

---

## Exploratory Data Analysis (EDA)
The EDA phase focused on understanding data distribution, relationships between variables, and identifying patterns that influence student performance.

## Plots & Visualizations

All generated plots are available in the following directory:

**[assets/plots](assets/plots/)**

- Correlation heatmaps  
- Feature importance plots  
- Relationship visualization plots.  

---

### Key Insights
- Hours studied and previous academic performance have the strongest positive correlation with exam scores.
- Attendance plays a significant role in student outcomes.
- Motivation level and parental involvement positively impact performance.
- Lifestyle factors such as sleep hours and physical activity show a weaker but positive influence.
- Socio-economic factors (family income, access to resources) contribute meaningfully to performance variation.
- Outliers were present but retained as they represent realistic student behaviors.

---

## Data Preprocessing
- Missing values in categorical features were handled by removing incomplete rows.
- Numerical features were kept in original scale.
- Categorical features were encoded using One-Hot Encoding.
- A unified preprocessing pipeline was created to ensure consistency during training and deployment.

---

## Feature Engineering
- Numerical and categorical features were separated.
- One-hot encoding was applied to categorical variables.
- Feature transformations were integrated using `ColumnTransformer`.
- The preprocessing and model were combined into a single pipeline to avoid data leakage and ensure deployment reliability.

---

## Model Building
Multiple regression models were trained and evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Model Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Model Performance Comparison

### Before Hyperparameter Tuning
| Model | MAE | RMSE | R² |
|------|-----|------|----|
| Linear Regression | 1.064 | 2.284 | 0.664 |
| Random Forest | 1.183 | 2.428 | 0.621 |
| Gradient Boosting | 0.850 | 2.181 | 0.694 |

### After Hyperparameter Tuning
| Model | MAE | RMSE | R² |
|------|-----|------|----|
| Ridge Regression | 1.065 | 2.284 | 0.664 |
| Random Forest (Tuned) | 1.137 | 2.361 | 0.641 |
| Gradient Boosting (Tuned) | 0.715 | 2.123 | 0.710 |

### Final Model Selection
The **tuned Gradient Boosting Regressor** was selected as the final model due to:
- Lowest MAE
- Lowest RMSE
- Highest R² score

---

## Model Deployment
The final model and preprocessing steps were saved as a single pipeline and deployed using Streamlit.

### Application Features
- User-friendly input form
- Real-time prediction of exam score
- Consistent preprocessing using trained pipeline
- Fully reproducible predictions

---

## Application User-Interfaces

Below are screenshots of user interfaces demonstrating the workflow and outputs of the project.

<img src="assets/screenshots/streamlit app1.png" width="300" />
<img src="assets/screenshots/streamlit app2.png" width="300" />
<img src="assets/screenshots/streamlit app3.png" width="300" />

---

## Project Structure
```
student_performance_prediction/
├── .venv/                      # Virtual environment (local, not tracked)
├── assets/
│   ├── plots/                  # Generated EDA & model evaluation plots
│   └── screenshots/            # Streamlit app user interfaces 
│
├── data/
│   ├── raw/                    # Original, unprocessed datasets
│   ├── processed/              # Cleaned & feature-engineered datasets
│   └── data-dictionary.md      # Description of dataset features
│
├── notebooks/
│   ├── data-understanding.ipynb # Data inspection & schema understanding
│   ├── exploratory-data-analysis.ipynb # EDA & visualizations
│   └── model-training.ipynb    # Model training & evaluation
│
├── app.py                      # Application / inference script
├── model.pkl                   # Trained ML model
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Runtime environment (deployment)
├── README.md                   # Project documentation
└── .gitignore                  # Ignored files & folders

```


---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## How to Run the Project Locally

1. Clone the repository

```
git clone <repository_url>
cd student_performance_prediction
```

2. Create Virtual environment
```
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies
```
pip install -r requirements.txt
```

4. Run Streamlit app
```
streamlit run app.py
```
---
## Future Improvements
- Add performance category classification (Excellent / Good / Needs Improvement)
- Provide personalized study recommendations
- Improve model explainability using SHAP
- Deploy on Streamlit Cloud or other cloud platforms
- Add user authentication and data storage

---

## Conclusion
This project demonstrates a complete machine learning workflow, including data analysis, feature engineering, model tuning, and deployment. It highlights how academic, lifestyle, and socio-economic factors jointly influence student performance and provides a practical tool for performance prediction.

---


## Author

**Riyanshi Verma**  
AI/ML Enthusiast | Machine Learning & Data Science

---

© 2026 Riyanshi Verma. All rights reserved.


