import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv("UNdata_Export_20250403_011008399.csv")


df.columns = ["field0", "Country", "field1", "Year", "field2", "Sex", 
              "field3", "Age group", "field4", "Unit", "field5", "Value"]

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

pivotitaly = df.pivot(index="Year", columns="Sex", values="Value").sort_index()
#Thailand plot
dfthai = pd.read_csv("thailand_enrollment.csv")



dfthai.columns = ["field0", "Country", "field1", "Year", "field2", "Sex", 
              "field3", "Age group", "field4", "Unit", "field5", "Value"]

dfthai["Year"] = pd.to_numeric(dfthai["Year"], errors="coerce")
dfthai["Value"] = pd.to_numeric(dfthai["Value"], errors="coerce")

pivotthai = dfthai.pivot(index="Year", columns="Sex", values="Value").sort_index()


plt.figure(figsize=(12, 6))
plt.plot(pivotitaly.index, pivotitaly["All genders"], label="All Genders (Italy)", color="blue")
plt.plot(pivotitaly.index, pivotitaly["Female"], label="Women (Italy)", color="pink")
plt.plot(pivotthai.index, pivotthai["All genders"], label="All Genders (Thai)", color="teal")
plt.plot(pivotthai.index, pivotthai["Female"], label="Women (Thai)", color="red")

plt.title("Enrollment in Grade 5 in Italy and Thailand by Gender (UN Data)")
plt.xlabel("Year")
plt.ylabel("Population Count")
plt.legend(title="Gender & Country")
plt.grid(True)
plt.tight_layout()
plt.savefig("italythaiplot.png")
plt.show()





