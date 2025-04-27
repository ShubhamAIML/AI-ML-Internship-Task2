# **Titanic Dataset: Exploratory Data Analysis (EDA)**  
**Task 2 | Elevale AI & ML Internship**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Pandas](https://img.shields.io/badge/Pandas-1.3.0-green)  
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.0-orange)  

---

## **📋 Overview**  
This repository presents an **in-depth Exploratory Data Analysis (EDA)** of the Titanic dataset for the **Elevale AI & ML Internship Task 2**. The goal is to uncover patterns, trends, and relationships in the data using descriptive statistics and visualizations. Tools used include **Pandas** for data manipulation, **Matplotlib** and **Seaborn** for plotting, and Python's built-in formatting for outputs. The analysis includes feature engineering to enhance insights and meets the task's objectives of data understanding and pattern recognition.  

Run the analysis on Colab: [Colab Notebook](https://colab.research.google.com/drive/1HoMJCVGDj1-dG905Tkz-rVjA72TznYcp?usp=sharing). [Kaggle Notebook]([https://colab.research.google.com/drive/1HoMJCVGDj1-dG905Tkz-rVjA72TznYcp?usp=sharing](https://www.kaggle.com/code/shubham1921/exploratory-data-analysis-on-titanic-dataset).

---

## **🔍 Analysis Steps**  
1. **Data Loading**: Imported the `Titanic-Dataset.csv` dataset using Pandas.  
2. **Data Cleaning**: Addressed missing values by filling `Age` with the median, `Embarked` with the mode, and dropping the `Cabin` column due to excessive missing data.  
3. **Descriptive Statistics**: Computed summary statistics (mean, median, standard deviation, etc.) for numeric features and value counts for categorical features.  
4. **Visualizations**: Generated 10 visualizations, including histograms, boxplots, heatmaps, and more, all standardized to 10x6 dimensions for consistency.  
5. **Feature Engineering**: Created `Family_Size` (SibSp + Parch + 1) and `Fare_Range` (binned fares) to explore additional patterns.  
6. **Inferences**: Derived key insights from statistical summaries and visualizations to understand survival trends.  

---

## **📂 Repository Structure**  
```
AI-ML-Internship-Task2/
├── data/
│   ├── Titanic-Dataset.csv       # Original dataset
│   └── cleaned_titanic.csv       # Cleaned dataset
├── visuals/                      # Visualization PNGs
│   ├── age_distribution.png      # Age distribution histogram
│   ├── fare_by_pclass.png        # Fare vs Pclass boxplot
│   ├── correlation_heatmap.png   # Numeric feature correlations
│   ├── pairplot_survived.png     # Feature pairplot by survival
│   ├── survival_by_sex.png       # Survival by sex bar plot
│   ├── survival_by_pclass.png    # Survival by class bar plot
│   ├── age_by_survival.png       # Age vs survival violin plot
│   ├── fare_by_survival.png      # Fare vs survival violin plot
│   ├── survival_by_family_size.png  # Survival by family size
│   └── survival_by_fare_range.png   # Survival by fare range
├── titanic_eda.py                # Python script for EDA
└── README.md                     # Project documentation
└── task 2.pdf                    # Task 2 
```

---

## **📊 Outputs**  

### **Cleaned Dataset**  
- **File**: `cleaned_titanic.csv`  
- **Description**: The original dataset with missing values resolved. `Age` was filled with the median (~28 years), `Embarked` with the mode ('S'), and the `Cabin` column was dropped. The cleaned dataset has **891 rows** and **11 columns**, ready for analysis.  

### **Datatypes**  
| **Column**    | **Datatype** | **Description**                              |
|---------------|--------------|----------------------------------------------|
| PassengerId   | int64        | Unique identifier for each passenger         |
| Survived      | int64        | Survival status (0 = Did not survive, 1 = Survived) |
| Pclass        | int64        | Passenger class (1 = First, 2 = Second, 3 = Third) |
| Name          | object       | Passenger's full name                        |
| Sex           | object       | Gender (male/female)                         |
| Age           | float64      | Age in years (decimals from median fill)     |
| SibSp         | int64        | Number of siblings/spouses aboard            |
| Parch         | int64        | Number of parents/children aboard            |
| Ticket        | object       | Ticket number                                |
| Fare          | float64      | Ticket fare in pounds                        |
| Embarked      | object       | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

### **Visualizations**  
The following table lists the 10 visualizations created, each saved as a PNG file with a consistent **10x6 dimension** for uniformity. All plots are styled with clear labels, vibrant colors, and proper spacing.  

| **File Name**             | **Plot Type** | **Description**                              | **Key Insight**                              |
|---------------------------|---------------|----------------------------------------------|----------------------------------------------|
| `age_distribution.png`    | Histogram     | Displays the distribution of passenger ages with a kernel density estimate (KDE). | Most passengers were **20-30 years old**, with fewer children and elderly. |
| `fare_by_pclass.png`      | Boxplot       | Shows the distribution of ticket fares across passenger classes (1st, 2nd, 3rd). | **First-class passengers** paid significantly higher fares, with some outliers. |
| `correlation_heatmap.png` | Heatmap       | Visualizes correlations between numeric features (e.g., Age, Fare, Pclass). | **Pclass and Fare** have a strong negative correlation (-0.55). |
| `pairplot_survived.png`   | Pairplot      | Scatterplot matrix of Age, Fare, SibSp, and Parch, colored by survival status. | **Survivors** tend to be younger and paid higher fares, with distinct clusters. |
| `survival_by_sex.png`     | Bar Plot      | Compares survival counts between males and females. | **Females** had a much higher survival rate (**74%**) than males (**19%**). |
| `survival_by_pclass.png`  | Bar Plot      | Shows survival counts across passenger classes. | **First-class passengers** had the highest survival rate (**63%**), third-class lowest (**24%**). |
| `age_by_survival.png`     | Violin Plot   | Illustrates age distributions for survivors and non-survivors. | **Survivors** were slightly younger on average, with a wider age range. |
| `fare_by_survival.png`    | Violin Plot   | Compares fare distributions between survivors and non-survivors. | **Survivors** paid higher fares on average, with a broader fare range. |
| `survival_by_family_size.png` | Bar Plot  | Displays survival counts by family size (SibSp + Parch + 1). | **Small families (2-4 members)** had higher survival rates; solo or large families had lower. |
| `survival_by_fare_range.png`  | Bar Plot  | Shows survival counts by fare ranges (Low, Medium, High, Very High). | **Higher fare ranges** (High, Very High) were associated with better survival rates. |

*(All plots are saved in the `visuals/` folder.)*

### **Inferences**  
- **Age Distribution**: The majority of passengers were aged **20-30 years**, with fewer children and elderly, indicating a young adult-heavy demographic.  
- **Fare and Class**: **First-class passengers** paid significantly higher fares, reflecting their socio-economic status.  
- **Correlation**: A strong **negative correlation** exists between **Pclass and Fare** (lower classes paid less).  
- **Survival Trends**: **Younger passengers** and those with **higher fares** had better survival chances, likely due to prioritization in rescue efforts.  
- **Gender and Class**: **Females** and **first-class passengers** had notably higher survival rates (**~74%** for females, **~63%** for first-class).  
- **Survivor Profile**: **Survivors** were generally younger and paid higher fares, suggesting age and wealth influenced survival.  
- **Family Size Impact**: Passengers traveling **alone** or with **large families (>4 members)** had lower survival rates, while **small families (2-4)** fared better.  
- **Fare Ranges**: Passengers in **higher fare ranges** (High, Very High) had increased survival probabilities, reinforcing the link between wealth and survival.  

---

## **⚙️ Libraries Used**  
```python
import pandas as pd        # Data loading, cleaning, and analysis  
import matplotlib.pyplot as plt  # Visualization support  
import seaborn as sns      # Enhanced visualizations  
```

---

## **📌 How to Use**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/AI-ML-Internship-Task2.git
   ```  
2. Run the script:  
   ```bash
   python titanic_eda.py
   ```  
   *Or open in Colab using the link above.*

---

## **🔗 References**  
- **Dataset Source**: [Kaggle Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)  
- **Documentation**: [Pandas](https://pandas.pydata.org/), [Seaborn](https://seaborn.pydata.org/)  

---

## **🎯 Goals Achieved**  
✅ Performed **in-depth EDA**  
✅ Extracted **actionable insights** on survival trends  
✅ Created **10 publication-ready visualizations**  

---
