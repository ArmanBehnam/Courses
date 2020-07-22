#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("D:/Arman/Learn/Udacity/New folder/ud120-projects-master/final_project/final_project_dataset.pkl", "rb"))

enron_data["SKILLING JEFFREY K"]["bonus"]
enron_data["SKILLING JEFFREY K"]
import pandas as pd
a = pd.DataFrame(enron_data)
a.head()
a.columns
a.index
len(a.index)
a.loc[:,a.loc['poi',:] == True]
enron_data["PRENTICE JAMES"]['total_stock_value']
enron_data['COLWELL WESLEY ']['from_this_person_to_poi']
enron_data['SKILLING JEFFREY K']['exercised_stock_options']
import numpy as np
b = [enron_data['FASTOW ANDREW S']['total_payments'],enron_data['LAY KENNETH L']['total_payments'],enron_data['SKILLING JEFFREY K']['total_payments']]
print(np.argmax(b),b[np.argmax(b)])
sum(a.loc['salary',:]!='NaN')
p = pd.read_csv('D:/Arman/Learn/Udacity/New folder/ud120-projects-master/final_project/poi_names.txt')
for i in range(len(p.index)):
	if p.index[i][1] == 'y':
		print(p.index[i][1])

sum(a.loc['email_address',:]!='NaN')
