# Restaurant Rating Prediction & Customer Segmentation System

> A machine learning-powered restaurant recommendation and customer intelligence system that predicts customer ratings, uncovers hidden customer segments, and generates actionable business insights for personalized dining experiences and strategic decision-making.

---

# Table of Contents

- Project Overview
- Business Problem
- Project Objectives
- Dataset Overview
- Project Structure
- Methodology
  - Exploratory Data Analysis
  - Data Preprocessing
  - Feature Engineering
  - Predictive Modeling
  - Clustering Analysis
  - Business Strategy Development
- Model Performance Comparison
- Best Performing Model
- Customer Segmentation Results
- Key Business Insights
- Visualizations
- Business Recommendations
- Business Impact
- Installation & Setup
- Technologies Used
- Future Improvements
- Authors

---

# Project Overview

Restaurant customers have varying preferences, budgets, expectations, and dining behaviors. Understanding these differences is essential for improving customer satisfaction, increasing retention, and providing personalized recommendations.

This project leverages machine learning and customer segmentation techniques to:

- Predict restaurant ratings based on customer and restaurant attributes.
- Understand the key drivers of customer satisfaction.
- Identify distinct customer segments.
- Generate actionable business recommendations.
- Support data-driven decision-making for restaurant recommendation systems.

The project combines predictive analytics, clustering, and business intelligence to transform customer data into meaningful insights.

---

# Business Problem

Traditional recommendation systems often fail to account for the diversity of customer preferences and dining expectations.

This can lead to:

- Poor recommendation quality
- Lower customer satisfaction
- Reduced customer retention
- Inefficient marketing strategies
- Missed revenue opportunities

To address these challenges, this project develops a predictive and segmentation framework capable of understanding customer behavior and supporting personalized dining recommendations.

---

# Project Objectives

## Predictive Analytics

Build machine learning models capable of predicting restaurant ratings using:

- Customer demographics
- Restaurant characteristics
- Dining preferences
- Budget information
- Behavioral indicators

## Customer Segmentation

Identify meaningful customer groups through clustering techniques to support:

- Personalized recommendations
- Customer targeting
- Loyalty programs
- Marketing optimization

## Business Intelligence

Generate actionable business insights that can improve:

- Customer satisfaction
- Recommendation quality
- Restaurant performance
- Customer retention

---

# Dataset Overview

The dataset contains customer, restaurant, and rating information.

## Customer Features

- Birth Year
- Weight
- Height
- Marital Status
- Personality Traits
- Budget Preferences
- Transportation Preferences

## Restaurant Features

- Restaurant ID
- Location Information
- Cuisine Types
- Accessibility Information
- Service Attributes

## Target Variable

**Restaurant Rating**

Additional rating indicators:

- Food Rating
- Service Rating

---

# Feature Engineering

Several business-focused features were created to improve predictive performance and interpretability.

### Engineered Features

- Family Activity Match
- Budget Service Score
- Dining Experience Score
- Location Score
- Cuisine Match
- Accessibility Score
- Social Dining Score
- Budget Numeric

These features capture interactions between customer preferences and restaurant characteristics that are not directly observable from raw data.

---

# Project Structure

```text
restaurant-rating-prediction/
│
├── .git/
│
├── data/
│   ├── raw/
│   │   └── Original datasets
│   │
│   └── processed/
│       └── Cleaned datasets
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_data_preprocessing.ipynb
│   ├── 04_baseline_models.ipynb
│   ├── 05_advanced_models.ipynb
│   ├── 06_model_evaluation.ipynb
│   ├── 07_clustering_analysis.ipynb
│   └── 08_business_strategy.ipynb
│
├── outputs/
│   ├── figures/
│   └── models/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── clustering.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Methodology

## 1. Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand customer behavior, restaurant characteristics, and rating patterns.

### Key Activities

- Data quality assessment
- Missing value analysis
- Distribution analysis
- Correlation analysis
- Customer demographic profiling
- Rating trend analysis

### Key Findings

- Customer satisfaction is strongly influenced by dining experience quality.
- Cuisine compatibility contributes significantly to restaurant ratings.
- Budget preferences affect customer expectations.
- Customer behavior varies significantly across demographic groups.

---

## 2. Data Preprocessing

The dataset underwent extensive preprocessing before model training.

### Steps Performed

- Missing value handling
- Duplicate removal
- Data cleaning
- One-hot encoding
- Feature scaling
- Feature selection

---

## 3. Predictive Modeling

Multiple classification models were developed and evaluated.

### Baseline Model

- Logistic Regression

### Advanced Models

- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- Weighted F1-Score

---

# Model Performance Comparison

| Model | Accuracy | Precision | Recall | Weighted F1 Score |
|---------|---------:|---------:|---------:|---------:|
| **XGBoost Classifier** | **73.53%** | **73.48%** | **73.53%** | **73.48%** |
| Logistic Regression (Baseline) | 72.35% | 73.00% | 72.00% | 72.00% |
| Random Forest Classifier | 70.59% | 70.74% | 70.59% | 70.63% |
| Decision Tree Classifier | 68.24% | 67.80% | 68.24% | 67.88% |

---

# Best Performing Model

## XGBoost Classifier

The XGBoost Classifier achieved the highest performance across all evaluation metrics and was selected as the final prediction model.

### Performance Metrics

| Metric | Value |
|----------|---------:|
| Accuracy | 73.53% |
| Precision | 73.48% |
| Recall | 73.53% |
| Weighted F1-Score | 73.48% |

### Why XGBoost Performed Best

- Captured complex feature interactions.
- Reduced overfitting through regularization.
- Handled nonlinear relationships effectively.
- Delivered the most balanced performance across all rating classes.

---

# Clustering Analysis

Customer segmentation was performed using unsupervised learning techniques.

## K-Means Clustering

Silhouette analysis was used to determine the optimal number of clusters.

### Silhouette Score Results

| Number of Clusters | Silhouette Score |
|------------------|-----------------:|
| 2 | 0.1084 |
| 3 | 0.1004 |
| 4 | 0.1074 |
| 5 | 0.0978 |
| 6 | 0.0928 |
| 7 | 0.1152 |
| 8 | 0.1170 |
| 9 | 0.1089 |
| **10** | **0.1262** |

### Selected Configuration

- Algorithm: K-Means
- Optimal Clusters: 10
- Silhouette Score: 0.1262

---

# Customer Segmentation Results

The clustering analysis identified ten distinct customer segments.

## Key Segments

### Highly Satisfied Premium Diners

**Characteristics**

- Highest overall ratings
- Highest food ratings
- Highest service ratings
- Strong value perception

**Business Opportunity**

- Loyalty programs
- Premium dining experiences
- Customer retention campaigns

### Cuisine-Focused Customers

**Characteristics**

- Strong cuisine alignment
- High satisfaction when preferences are matched

**Business Opportunity**

- Personalized recommendations
- Cuisine-specific promotions

### Family-Oriented Diners

**Characteristics**

- Family-focused dining preferences
- Value-conscious behavior

**Business Opportunity**

- Family packages
- Group dining promotions

### Social Experience Seekers

**Characteristics**

- Strong emphasis on social dining
- Accessibility-conscious

**Business Opportunity**

- Group events
- Social dining experiences

### Budget-Conscious Customers

**Characteristics**

- Price-sensitive
- Promotion-responsive

**Business Opportunity**

- Discounts
- Value-based offers

### Dissatisfied Customers

**Characteristics**

- Lowest satisfaction levels
- Poor dining experience ratings

**Business Opportunity**

- Service quality improvements
- Customer recovery programs

---

# Key Business Insights

## 1. Customer Preferences Drive Satisfaction

Cuisine compatibility emerged as one of the strongest factors influencing restaurant ratings.

## 2. Dining Experience Matters

Food quality and service quality significantly impact overall customer satisfaction.

## 3. Customer Segments Are Distinct

The clustering analysis confirmed that customers exhibit diverse dining preferences and behaviors.

## 4. Personalized Recommendations Can Improve Outcomes

Matching customers with restaurants that align with their preferences can improve satisfaction and engagement.

## 5. Different Customer Groups Require Different Strategies

A single recommendation strategy is unlikely to serve all customer segments effectively.

---

# Recommended Visualizations

## Exploratory Analysis

- Rating Distribution
- Correlation Heatmap
- Budget Distribution

## Model Evaluation

- Model Performance Comparison Chart
- Feature Importance Plot
- Confusion Matrix

## Customer Segmentation

- Silhouette Score Analysis
- Cluster Profile Heatmap
- Cluster Distribution Chart

---

# Business Recommendations

## Personalized Recommendation Engine

Leverage customer preferences and predictive models to recommend restaurants aligned with individual tastes.

**Expected Impact**

- Improved customer satisfaction
- Increased recommendation accuracy

## Customer Retention Programs

Target highly satisfied customers through:

- Loyalty rewards
- Exclusive offers
- Personalized experiences

**Expected Impact**

- Increased retention
- Higher customer lifetime value

## Improve Service Quality

Focus on low-performing customer segments to identify service gaps.

**Expected Impact**

- Higher ratings
- Reduced churn

## Segment-Based Marketing

Develop campaigns tailored to:

- Family-oriented customers
- Budget-conscious customers
- Premium diners

**Expected Impact**

- Better conversion rates
- More efficient marketing spend

## Data-Driven Restaurant Insights

Provide restaurant partners with feedback regarding:

- Customer preferences
- Satisfaction drivers
- Service improvement opportunities

**Expected Impact**

- Improved restaurant performance
- Better customer experiences

---

# Business Impact

Implementation of this framework can help organizations achieve:

- Higher customer satisfaction
- Improved recommendation quality
- Increased customer retention
- Better restaurant engagement
- More effective marketing strategies
- Enhanced decision-making capabilities

---

# Technologies Used

## Programming Language

- Python 3.x

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-Learn
- XGBoost

## Clustering

- K-Means Clustering
- Agglomerative Hierarchical Clustering

## Development Environment

- Jupyter Notebook

---

# Installation & Setup

```bash
# Clone repository
git clone <repository-url>

# Navigate into project
cd restaurant-rating-prediction

# Create virtual environment
python -m venv venv

# Activate environment

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Run notebooks:

```bash
jupyter notebook
```

---

# Future Improvements

Potential enhancements include:

- Real-time recommendation systems
- Deep learning recommendation models
- User behavior tracking
- Restaurant ranking optimization
- Dynamic promotion engines
- Web application deployment
- Real-time customer segmentation

---

# Author
**Angela Mutiga**

---

