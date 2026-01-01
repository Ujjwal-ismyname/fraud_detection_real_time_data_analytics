import pandas as pd

def create_features(df):

    df["log_amount"] = df["TransactionAmt"].apply(lambda x: 0 if x <= 0 else round(x, 4))

    df["hour"] = (df["TransactionDT"] // 3600) % 24

    df["amount_per_hour"] = df["TransactionAmt"] / (df["hour"] + 1)

    features = [
        "TransactionAmt",
        "log_amount",
        "hour",
        "amount_per_hour"
    ]

    X = df[features]
    y = df["isFraud"]

    return X, y

if __name__ == "__main__":
    df = pd.read_csv("data/clean_transactions.csv")
    X, y = create_features(df)
    print("✅ Feature engineering complete")