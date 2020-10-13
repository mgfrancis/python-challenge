# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:59:16 2020

@author: opusm
"""

import os
import csv


filename = os.path.join('D:\\Python_Challenges\\python-challenge\\Pybank','Resources','budget_data.csv')

total_months = 0
total_profit = 0
prev_profit = []
next_profit= []
mth_profit = []
mthly_change = []
total_change = 0

# Open the file in "read" mode ('r') and store the contents in the variable "webtxt"
with open(filename,'r', encoding = "utf8") as budget:
    budgetlist = csv.reader(budget)
  
    budget_header = next(budgetlist)
    
    for row in budgetlist:
        
        if row[0] != 0:
            total_months += 1
            mth_profit.append(row[0])
            
        if row[1] != 0:
            total_profit += int(row[1])
            prev_profit.append(int(row[1]))
            #next_profit.append(int(row[1]))
            
    next_profit = prev_profit[1:]
    
    #calculate monthly changes
    for data in range(len(next_profit)):
        
        mthly_change.append(next_profit[data] - prev_profit[data])
        total_change += (next_profit[data] - prev_profit[data])
    
    #calculate ave_change
    ave_change = total_change / len(next_profit)
    
    #get max and min profits
    max_profit = max(mthly_change)
    min_profit = min(mthly_change)
    
    #get min and max index for corresponding month
    max_index = mthly_change.index(max_profit)
    min_index = mthly_change.index(min_profit)
    
    max_date = mth_profit[max_index + 1]
    min_date = mth_profit[min_index + 1]
    
#apply formatting
if total_profit >=0 :
    total_profit = '${:}'.format(total_profit)
else: total_profit = '${:-}'.format(total_profit)
        
if ave_change >= 0:
    ave_change = '${:0.2f}'.format(ave_change)
else: ave_change = '${:-0.2f}'.format(ave_change)

if max_profit >= 0 or min_profit >=0: 
    max_profit = '(${:})'.format(max_profit)
    min_profit = '(${:})'.format(min_profit)
else:
    max_profit = '(${:-})'.format(max_profit)
    min_profit = '(${:-})'.format(min_profit)


#create new csv
filename = os.path.join('D:\\Python_Challenges\\python-challenge\\Pybank','summary_budget.csv')

summary_rows = (['Financial Analysis'],['-------------------------------------'],[f'Total Months:  {total_months}'],[f'Total:  {total_profit}'],[f'Average Change:  {ave_change}'],[f'Greatest Increase in Profits:  {max_date}   {max_profit}'],[f'Greatest Decrease in Profits:  {min_date}  {min_profit}'])
                
# Open the file in "write" mode ('w') and store the contents in the variable "modbudget"
with open(filename,'w', newline='') as modbudget:
    summary = csv.writer(modbudget)
    
    summary.writerows(summary_rows)
  
   