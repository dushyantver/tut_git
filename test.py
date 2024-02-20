import pandas as pd

Data = [
    {"name":"san", "age":45, "city":"alvar"},
    {"name":"ram", "age":32, "city":"del"},
    {"name":"kush", "age":53, "city":"puner"}
]

pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)