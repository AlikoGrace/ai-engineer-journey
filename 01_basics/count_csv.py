# Write a script that reads a CSV file, counts rows by one column, and prints the top 5.
"""
Algorithm
1.Open the csv file
2.Go through it row by row
3.For each row, look at one column(eg country)
4.Keep count of the number of times you have seen that value (eg. Ghana)
5.Sort the count from the biggest to smallest
6.Print the top 5 or first 5.
"""

import csv
countries={}


with open("/Users/gracealiko/Downloads/orders.csv","r", encoding="utf-8", newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        country=row["country"]

        if country not in countries:
           countries[country]=1
        
        else: countries[country]+=1    
            
    # print(countries) 
    countries_count=countries.items() 
    # print(contries_count)
sorted_countries=sorted(countries_count,key=lambda pair: pair[1], reverse=True)
print(sorted_countries[:5])

            
        
        
            

        
    

   
