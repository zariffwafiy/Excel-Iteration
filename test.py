import pandas as pd, numpy as np, openpyxl, csv, os, re, xlsxwriter

# load excel file (edit the file_path variable accordingly)
file_path = "IVA Error Workshop Fatin.xlsx"
file = pd.read_excel(io = file_path, sheet_name= "Splitting - Zarif")

# create an empty list to store dataframes
df = []

for _, row in file.iterrows():
    tml_id = row["TMLID"] # access the "TMLID" column
    measured_reading = row["MeasuredReading"] # access the "MeasuredReading" column

    # tokenize the "TMLID" values using space as a delimiter
    tokens_tmlid = str(tml_id).split()
    # change the value of measured reading to string, then tokenize the "TMLID" values using space as a delimiter
    tokens_reading = str(measured_reading).split()

    # if there are more than 1 token, create duplicate rows
    if len(tokens_tmlid) > 1:
        
        # handle the - cases
        if tokens_reading == ["-"]:
            tokens_reading = ["0.0 "] * len(tokens_tmlid)
            print(tokens_reading)

            for token1,token2 in zip(tokens_tmlid, tokens_reading):
                new_row = row.copy()

                new_row["TMLID"] = token1 # set the new TMLID value
                new_row["MeasuredReading"] = token2
                new_row["MeasuredReading"] = "-"
                df.append(new_row.to_frame().T) # this will enable the copies to be appended to the original dataframe

        else:
            # create a copy of the row for each token except the first one
            for token1,token2 in zip(tokens_tmlid, tokens_reading):
                new_row = row.copy()

                new_row["TMLID"] = token1 # set the new TMLID value
                new_row["MeasuredReading"] = token2
                df.append(new_row.to_frame().T) # this will enable the copies to be appended to the original dataframe

    else:
        # append the og row when there's only one token
        df.append(new_row.to_frame().T)

df = pd.concat(df, ignore_index=True)
print(df[["TMLID", "MeasuredReading"]])

# save back to excel file
with pd.ExcelWriter(file_path, engine="xlsxwriter", mode="w") as writer:
    df.to_excel(writer, sheet_name="Splitting - Zariff", index = False)