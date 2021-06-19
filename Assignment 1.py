#!/usr/bin/env python
# coding: utf-8

# Before start working on the problems, here is a small example to help you understand how to write your own answers. In short, the solution should be written within the function body given, and the final result should be returned. Then the autograder will try to call the function and validate your returned result accordingly.
# 
# 
# Find a list of all of the names in the following string using regex.

# In[4]:


import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    
    return re.findall("[A-Z][\w]*", simple_string)

    raise NotImplementedError()


# The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class. Create a regex to generate a list of just those students who received a B in the course.

# In[6]:


import re
def grades():
    with open ("/Users/williamwoodfine/Downloads/Coursera Assignments/Assignment 1/grades.txt", "r") as file:
        grades = file.read()
        bnames = []
        for x in re.finditer("([\w]*[\s][\w]*)([:][\s][B])", grades):
            bnames.append(x.group(1)) 
    return bnames
            
            

    raise NotImplementedError()



# Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# 
# a host (e.g., '146.204.224.152')
# a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
# the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
# 
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}

# In[7]:


import re
def logs():
    with open("/Users/williamwoodfine/Downloads/Coursera Assignments/Assignment 1/logdata.txt", "r") as file:
        logdata = file.read()
    dictionaries=[]
    pattern="""
    (?P<host>\d*\.\d*\.\d*\.\d*)
    (\s\-\s)
    (?P<user_name>.*)
    (\s\[)
    (?P<time>.*)
    (\]\s\")
    (?P<request>.*)
    (\")
             
    """
    for x in re.finditer(pattern, logdata, re.VERBOSE):
        dictionaries.append(x.groupdict())
    return (dictionaries)
    
    raise NotImplementedError()
    
logs()


print(names())
print(grades())
print(logs())
# In[ ]:




