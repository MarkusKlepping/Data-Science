import pandas as pd

# Task 2
df = pd.read_csv("yob2021.txt", sep=',', header=None, names=['Name', 'Gender', 'Count'])


# Task 3
print("first 10 entries", df.head(10))


# task 4
print ("Rows, Columns", df.shape)

# task 5
df_total = df["Count"].sum()
print("Total babies born:",df_total )

# task 6
female_df = df[df['Gender'] == 'F']

print( "Total Femal Babies", female_df["Count"].sum())

male_df = df[df["Gender"] == "M"]

print ("Total Male Babies", male_df["Count"].sum())

# task 7
print(df[df["Name"] == "Markus"])


# task 8
total_male_babies = male_df["Count"].sum()
relative_male_babies = int(total_male_babies) / int(df_total) * 100
print("Percentage of boys from total births", relative_male_babies)


print("Therefore, the percentage of female births is: ", 100 - relative_male_babies )


# task 9
top_5_females = female_df.sort_values(by = "Count", ascending=False).head(5)

top_5_males = male_df.sort_values(by = "Count", ascending=False).head(5)

top_5_names = pd.concat([top_5_females, top_5_males])

print (top_5_names)


# task 10
top_5_names.to_excel("top5Names.xlsx")