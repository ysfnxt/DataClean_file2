import pandas as pd
df = pd.read_csv("new_file2")

# To remove values where phone number is not available
# df.drop(df[(df["phone_numbers"] == '[]')].index, inplace = True)

# df.to_csv("personal_email_and_phone.csv")

df.drop(df[(df["phone_numbers"] != '[]')].index, inplace = True)
df.to_csv("personal_email_no_phone.csv")