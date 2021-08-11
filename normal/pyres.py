import sys
import warnings
warnings.filterwarnings("ignore")
from pyresparser import ResumeParser

cv=sys.argv[1]
data = ResumeParser(cv).get_extracted_data()
#print(data)
if (data['name'] != None):
    print("Name: "+data['name'])
if (data['email'] != None):
    print("Email: "+data['email'])
if (data['mobile_number'] != None):
    print("Mob No: "+data['mobile_number'])
if (data['skills'] != None):
    print("skills: "+str(data['skills']))
if (data['designation'] != None):
    print("designation: "+str(data['designation']))
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
