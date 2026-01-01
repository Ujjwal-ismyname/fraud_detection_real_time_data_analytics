# import pandas as pd
# import time

# # Load once
# df = pd.read_csv("data/clean_transactions.csv")

# def stream_transactions():
#     print("🚀 Starting real-time transaction stream...")
    
#     for i in range(len(df)):
#         row = df.iloc[[i]]  
#         row.to_csv("current_transaction.csv", index=False)

#         print(f"Streamed transaction {i+1}/{len(df)}")
#         time.sleep(0.5)  

#     print("Stream completed")

# if __name__ == "__main__":
#     stream_transactions()

import pandas as pd
import time

# CONFIG (TUNE HERE)
TOTAL_EVENTS = 3000     # total transactions to stream
DURATION_SECONDS = 300 # 5 minutes
SLEEP_TIME = DURATION_SECONDS / TOTAL_EVENTS

# Load once
df = pd.read_csv("data/clean_transactions.csv")

# Randomly pick a manageable subset
df = df.sample(TOTAL_EVENTS, random_state=42).reset_index(drop=True)

def stream_transactions():
    print("Streaming started")
    print(f"Total events: {TOTAL_EVENTS}")
    print(f"Total duration: {DURATION_SECONDS} seconds")

    for i in range(TOTAL_EVENTS):
        row = df.iloc[[i]]
        row.to_csv("current_transaction.csv", index=False)

        if i % 100 == 0:
            print(f"Streamed {i}/{TOTAL_EVENTS}")

        time.sleep(SLEEP_TIME)

    print("Streaming completed")

if __name__ == "__main__":
    stream_transactions()