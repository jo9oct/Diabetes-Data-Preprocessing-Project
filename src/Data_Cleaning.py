
import pandas as pd
import numpy as np

class cleaning_data:

    def __init__(self):
        pass
    
    def missing_value_summary(self, df):
        # Features where zero is biologically impossible
        bio_cols = ['Glucose', 'Diastolic_BP', 'Skin_Fold', 'Serum_Insulin', 'BMI']

        # Replace biologically impossible zeros with NaN
        df[bio_cols] = df[bio_cols].replace(0, np.nan)

        # Missing value counts and percentages
        missing_counts = df.isna().sum()
        missing_percent = (missing_counts / len(df)) * 100
        missing_summary = pd.DataFrame({
            "Missing Count": missing_counts,
            "Missing %": missing_percent.round(2)
        })
        return missing_summary,df
     
    def impute_missing_values(self,df):
        # Mean or median imputation depending on distribution
        # (Using median for skewed data)
        df['Glucose'].fillna(df['Glucose'].median(), inplace=True)
        df['Diastolic_BP'].fillna(df['Diastolic_BP'].median(), inplace=True)
        df['Skin_Fold'].fillna(df['Skin_Fold'].median(), inplace=True)
        df['Serum_Insulin'].fillna(df['Serum_Insulin'].median(), inplace=True)
        df['BMI'].fillna(df['BMI'].median(), inplace=True)
        return df
    
    # Function to detect and treat outliers using IQR
    def treat_outliers_iqr(self, data, column):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        # Count before treatment
        outliers = ((data[column] < lower) | (data[column] > upper)).sum()
        print(f"{column}: {outliers} outliers detected.")
        
        # Cap the outliers to lower/upper limits
        data[column] = np.where(data[column] < lower, lower,
                    np.where(data[column] > upper, upper, data[column]))
        return data