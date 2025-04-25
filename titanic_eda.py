!pip install tabulate

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Set style for visualizations
sns.set(style="whitegrid", palette="muted", font_scale=1.2)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Load dataset
df = pd.read_csv('Titanic-Dataset.csv')

# 1. Data Cleaning
# Missing values before cleaning
missing_before = df.isnull().sum().reset_index()
missing_before.columns = ['Column', 'Missing Values']
print("\nMissing Values Before Cleaning:\n", tabulate(missing_before, headers='keys', tablefmt='pretty', showindex=False))

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill Age with median
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Fill Embarked with mode
df = df.drop('Cabin', axis=1)  # Drop Cabin column

# Missing values after cleaning
missing_after = df.isnull().sum().reset_index()
missing_after.columns = ['Column', 'Missing Values']
print("\nMissing Values After Cleaning:\n", tabulate(missing_after, headers='keys', tablefmt='pretty', showindex=False))

# Save cleaned dataset
df.to_csv('/content/cleaned_titanic.csv', index=False)
print("\nCleaned dataset saved as /content/cleaned_titanic.csv")

# 2. Datatypes
dtypes_df = pd.DataFrame({
    'Column': df.columns,
    'Datatype': df.dtypes.values
})
print("\nDatatypes of Columns:\n", tabulate(dtypes_df, headers='keys', tablefmt='pretty', showindex=False))

# 3. Summary Statistics
# Numeric stats
numeric_stats = df.describe().reset_index()
print("\nNumeric Columns Stats:\n", tabulate(numeric_stats, headers='keys', tablefmt='pretty', showindex=False))

# Categorical counts
cat_cols = ['Sex', 'Pclass', 'Embarked']
for col in cat_cols:
    counts = df[col].value_counts().reset_index()
    counts.columns = [col, 'Count']
    print(f"\n{col} Counts:\n", tabulate(counts, headers='keys', tablefmt='pretty', showindex=False))

# 4. Visualizations (All 10x6 for consistent width)
# Histogram: Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Age', pad=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/content/age_distribution.png')
plt.show()
plt.subplots_adjust(hspace=0.5)  # Gap between plots

# Boxplot: Fare by Pclass
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Fare', data=df, palette='Blues')
plt.title('Fare by Passenger Class', pad=20)
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.tight_layout()
plt.savefig('/content/fare_by_pclass.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Correlation Heatmap (Only numeric columns)
plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap', pad=20)
plt.tight_layout()
plt.savefig('/content/correlation_heatmap.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Pairplot: Selected features
sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']], hue='Survived', palette='husl')
plt.suptitle('Pairplot of Features by Survival', y=1.02)
plt.savefig('/content/pairplot_survived.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Bar Plot: Survival by Sex
plt.figure(figsize=(10, 6))
sns.countplot(x='Sex', hue='Survived', data=df, palette='Set2')
plt.title('Survival by Sex', pad=20)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/content/survival_by_sex.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Bar Plot: Survival by Pclass
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='Set3')
plt.title('Survival by Passenger Class', pad=20)
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/content/survival_by_pclass.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Violin Plot: Age by Survival
plt.figure(figsize=(10, 6))
sns.violinplot(x='Survived', y='Age', data=df, palette='Pastel1')
plt.title('Age by Survival', pad=20)
plt.xlabel('Survived')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('/content/age_by_survival.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Violin Plot: Fare by Survival
plt.figure(figsize=(10, 6))
sns.violinplot(x='Survived', y='Fare', data=df, palette='Pastel2')
plt.title('Fare by Survival', pad=20)
plt.xlabel('Survived')
plt.ylabel('Fare')
plt.tight_layout()
plt.savefig('/content/fare_by_survival.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Family Size Analysis
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
plt.figure(figsize=(10, 6))
sns.countplot(x='Family_Size', hue='Survived', data=df, palette='Accent')
plt.title('Survival by Family Size', pad=20)
plt.xlabel('Family Size')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/content/survival_by_family_size.png')
plt.show()
plt.subplots_adjust(hspace=0.5)

# Fare Range Analysis
df['Fare_Range'] = pd.qcut(df['Fare'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
plt.figure(figsize=(10, 6))
sns.countplot(x='Fare_Range', hue='Survived', data=df, palette='Spectral')
plt.title('Survival by Fare Range', pad=20)
plt.xlabel('Fare Range')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/content/survival_by_fare_range.png')
plt.show()

# 5. Pivot Tables
# Survival by Sex and Pclass
pivot_sex_pclass = pd.pivot_table(df, values='Survived', index='Sex', columns='Pclass', aggfunc='mean').reset_index()
print("\nSurvival Rate by Sex and Pclass:\n", tabulate(pivot_sex_pclass, headers='keys', tablefmt='pretty', showindex=False))

# Survival by Embarked
pivot_embarked = pd.pivot_table(df, values='Survived', index='Embarked', aggfunc='mean').reset_index()
print("\nSurvival Rate by Embarked:\n", tabulate(pivot_embarked, headers='keys', tablefmt='pretty', showindex=False))

# 6. Inferences for README
print("\nInferences for README:")
inferences = [
    "1. Age distribution peaks around 20-30 years, with fewer children and elderly.",
    "2. First-class passengers paid significantly higher fares.",
    "3. Pclass and Fare have a negative correlation.",
    "4. Younger passengers and those paying higher fares had higher survival rates.",
    "5. Females and higher-class passengers had higher survival probabilities.",
    "6. Survivors were slightly younger and paid higher fares.",
    "7. Passengers traveling alone or with large families had lower survival rates.",
    "8. Higher fare ranges correlated with higher survival rates."
]
for inf in inferences:
    print(inf)