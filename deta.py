import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('customer churn.csv')
df.columns = df.columns.str.strip() 
print(df.head())  
print(df.info())
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].astype("float")
print(df.info())
print(df.isnull().sum().sum())
print(df.describe())
print(df.duplicated().sum())
print(df["customerID"].duplicated().sum())
def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
df['SeniorCitizen'] = df["SeniorCitizen"].apply(conv)
print(df.head())
plt.figure(figsize = (3,3))
ax =sns.countplot(x='SeniorCitizen', data=df)
ax.bar_label(ax.containers[0])
plt.title("Chunt of customers by Churn")
ax.bar_label(ax.containers[0])
plt.show()
print(df.describe())  
plt.figure(figsize=(3, 4))
gb = df.groupby("Churn").agg({'Churn': "count"})
plt.pie(gb['Churn'], labels=gb.index, autopct="%1.2f%%")
plt.title("Percentage of Churned Customers", fontsize=10)
plt.show()
plt.figure(figsize=(4, 4))
sns.countplot(x="SeniorCitizen", data=df, hue="Churn")
plt.title("Churn by Senior Citizen")
plt.xlabel("Senior Citizen")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
plt.figure(figsize=(9, 4))
sns.histplot(x="tenure", data=df, bins=72, hue="Churn")
plt.show()
plt.figure(figsize = (4,4))
ax = sns.countplot (x = "Contract", data = df, hue = "Churn") 
ax.bar_label(ax.containers [0]) 
plt.title("Count of Customers by Contract")
plt.show()
columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))
axes = axes.flatten()
for i, col in enumerate(columns):
    if col in df.columns:
        sns.countplot(x=col, data=df, ax=axes[i],hue=df["Churn"])
        axes[i].set_title(f'Countplot of {col}')
        axes[i].tick_params(axis='x', rotation=0)
    else:
        axes[i].text(0.1, 0.1, f"Column '{col}' not found", ha='center', va='center')
        axes[i].set_axis_off()
plt.tight_layout()
plt.show()
print("The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.")
plt.figure(figsize = (6,4)) 
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn") 
ax.bar_label(ax.containers[0])  
ax.bar_label(ax.containers[1])  
plt.title("Churned Customers by Payment Method")  
plt.xticks(rotation = 15)  
plt.show()