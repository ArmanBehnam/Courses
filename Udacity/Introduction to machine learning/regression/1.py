import sys
import pickle
sys.path.append("D:/Arman/Learn/Udacity/New folder/ud120-projects/tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("D:/Arman/Learn/Udacity/New folder/ud120-projects-master/final_project/final_project_dataset_modified.pkl", "rb") )

with open("D:/Arman/Learn/Udacity/New folder/ud120-projects-master/final_project/final_project_dataset_modified.pkl", "rb") as f:
    data_dict = pickle.load(f)
