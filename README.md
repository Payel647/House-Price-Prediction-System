#  House Price Prediction using Linear Regression

## 📖 Project Overview
HomeVista Properties operates across multiple cities and manages thousands of residential property sales every year.  
This project aims to build a **machine learning regression model** that can predict the **market price of a house** based on its physical features, location, and construction details.

The system uses **Linear Regression** to learn patterns from historical housing data and generate accurate price predictions.

---

##  Problem Statement
To automate the house pricing process by developing an intelligent ML-based regression model that predicts house prices using historical property data.

---

##  Dataset Description
Each row in the dataset represents a residential house with the following features:

| Feature | Description |
|------|-------------|
| Id | Unique house identifier |
| MSSubClass | Type of dwelling (building class code) |
| MSZoning | General zoning classification |
| LotArea | Lot size in square feet |
| LotConfig | Lot configuration |
| BldgType | Type of building |
| OverallCond | Overall condition rating (1–10) |
| YearBuilt | Year of construction |
| YearRemodAdd | Year of remodeling |
| Exterior1st | Exterior covering |
| SalePrice | Target variable (House Price) |

---

##  Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib & Seaborn
- Scikit-learn

---

##  Data Preprocessing
- Handled missing values
- Encoded categorical variables using One-Hot Encoding
- Feature scaling where required
- Removed irrelevant columns

---

##  Model Used
- Linear Regression

---

##  Model Evaluation
Model performance was evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

##  Results
The Linear Regression model successfully learned relationships between house features and prices, achieving reasonable prediction accuracy on unseen data.

---
