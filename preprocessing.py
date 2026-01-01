import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    drop_cols = [col for col in df.columns if 'id_' in col.lower()]
    df = df.drop(columns=drop_cols, errors='ignore')

    df.fillna(-1, inplace=True)

    cat_cols = df.select_dtypes(include=['object']).columns
    encoder = LabelEncoder()

    for col in cat_cols:
        df[col] = encoder.fit_transform(df[col].astype(str))

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/train_transaction.csv")
    clean_df = preprocess_data(df)
    clean_df.to_csv("data/clean_transactions.csv", index=False)
    print("Preprocessing complete")