import pandas as pd
import matplotlib.pyplot as plt
import os

##Download and Import the finance data. If there are more or less files, then add additional "File" variables through out the code.
#File 1 is an exapmle of Credit Card Data
#File 2 and 3 are exapmles of Debit Card Data
file1 = pd.read_csv('Credit_Card_Data')
#Debit Card // Removed the "CHeck Slips Column"
file2 = pd.read_csv('Debit_Card_Data')
#Debit Card // Removed the "CHeck Slips Column"
file3 = pd.read_csv('Debit_Card_Data')
#If there are any "Check Slips" column. Manually remove them.

#Update the Data Type for the Date Columns
#Create a New column that will show the Month and Year of the Transaction
file1['Transaction Date'] = pd.to_datetime(file1['Transaction Date'])
file1['Post Date'] = pd.to_datetime(file1['Post Date'])
file1['Year_Month'] = file1['Transaction Date'].dt.strftime('%Y-%m')
file2['Posting Date'] = pd.to_datetime(file2['Posting Date'])
file2['Year_Month'] = file2['Posting Date'].dt.strftime('%Y-%m')
file3['Posting Date'] = pd.to_datetime(file3['Posting Date'])
file3['Year_Month'] = file3['Posting Date'].dt.strftime('%Y-%m')

#1) Modify the Data Column Names so they all match
file1 = file1.rename(columns ={"Transaction Date": "Posting Date"})
#2) Remove all unused columns
file1 = file1.drop(columns=['Post Date', 'Category'])
file2 = file2.drop(columns=['Details', 'Balance'])
file3 = file3.drop(columns=['Details', 'Balance'])

frames = [file1, file2, file3]
f_data = pd.concat(frames)

findata = f_data
findata = findata[findata.Type != 'ACCT_XFER']
findata = findata[findata.Type != "ACH_CREDIT"]
findata = findata[findata.Type != "Adjustment"]
findata = findata[findata.Type != "Payment"]

findata2_group = findata.groupby('Year_Month').sum().sort_values(by='Year_Month')
print(findata2_group)

findata2_group.plot.bar(color="blue")
plt.show()
