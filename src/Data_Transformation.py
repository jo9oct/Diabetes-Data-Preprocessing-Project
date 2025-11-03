
class data_transformation:

    def __init__(self):
        pass

    # 1. FEATURE ENGINEERING

    # 🧩 a) Age Groups
    def age_group(self,age):
        if age < 30:
            return 'Young'
        elif 30 <= age < 50:
            return 'Middle-aged'
        else:
            return 'Senior'
        
    # 🧩 b) BMI Categories (Based on WHO standards)
    def bmi_category(self,bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
        
    # 🧩 c) Glucose Level Categories
    def glucose_category(self,glucose):
        if glucose < 100:
            return 'Normal'
        elif 100 <= glucose < 140:
            return 'Prediabetes'
        else:
            return 'Diabetes'
        
    # 2. ENCODING

    def encode_labels(df):
        # 🧠 Label Encoding for ordinal columns (BMI_Category has order)
        bmi_order = ['Underweight', 'Normal', 'Overweight', 'Obese']
        bmi_encoder = {label: idx for idx, label in enumerate(bmi_order)}
        df['BMI_Category_Encoded'] = df['BMI_Category'].map(bmi_encoder)

        # 🧩 One-Hot Encoding for nominal categories (Age_Group, Glucose_Category)
        df = pd.get_dummies(df, columns=['Age_Group', 'Glucose_Category'], drop_first=True)

        return df
    
    # 3. SCALING

    def scale_and_compare(df, numeric_cols):
        # Compare StandardScaler vs. MinMaxScaler
        scaler_standard = StandardScaler()
        scaler_minmax = MinMaxScaler()

        standard_scaled = pd.DataFrame(scaler_standard.fit_transform(df[numeric_cols]), 
                                    columns=[f"{col}_std" for col in numeric_cols])
        minmax_scaled = pd.DataFrame(scaler_minmax.fit_transform(df[numeric_cols]), 
                                    columns=[f"{col}_minmax" for col in numeric_cols])
        
        return standard_scaled, minmax_scaled