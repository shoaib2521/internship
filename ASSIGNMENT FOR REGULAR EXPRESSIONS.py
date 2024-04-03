#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT FOR REGULAR EXPRESSIONS

# Question--1 

# In[2]:


def replace_with_colon(text):
    modified_text = text.replace(' ',':').replace(',',':').replace('.',':')
    return modified_text
sample_text = 'python exercises, PHP exercises.'
print(replace_with_colon(sample_text))

    


# QUESTION--2

# In[5]:


import pandas as pd
import re
data = {'SUMMARY': ['hello, world!', 'text', 'four, five:; six...']}
df = pd.DataFrame(data)
def remove_special_chars(text):
    return re.sub(r'[^\w\s]', '', text)
df['SUMMARY'] = df['SUMMARY'].apply(remove_special_chars)
print(df)


# QUESTION--3

# In[8]:


import re
def find_long_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    long_words = pattern.findall(text)
    return long_words
text = "Hi sir my name is ,'sheik shoiab',and my batch number is ,'ds2403', 'thankyou'."
result = find_long_words(text)
print("word of at least 4 characters long:",result)


# QUESTION--4

# In[10]:


import re
def find_words_of_length(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(text)
    return words
text = "Hi sir my name is ,'sheik shoiab',and my batch number is ,'ds2403', 'thankyou'."
result = find_words_of_length(text)
print("words of lengths3,4,and 5 chsracters:",result)


# QUESTION--5

# In[15]:


import re
def remove_parentheses(strings):
    pattern = re.compile(r'\([^)]*\)')
    processed_strings = [pattern.sub('',string) for string in strings]
    
    return processed_strings

sample_text = ["example .com","hr@fliprobo .com", "github .com", "hello data science world ","data scientist"]
processed_text = remove_parentheses(sample_text)
for string in processed_text:
    print(string)


# QUESTION--6

# In[31]:


import re
def remove_parentheses_area(text):
    pattern = re.compile(r'\([^)]*\)')
    processed_text = pattern.sub('', text)
    
    return processed_text

with open('sample_text.txt', 'r') as file:
    text = file.read()
processed_text = remove_parentheses(text)
output = processed_text.split(',')

print(output)


# QUESTION--7

# In[33]:


import re
sample_text = "ImportanceOfRegularExpressionsInPython"
pattern = re.compile(r'[A-Z][^A-Z]*')
result = pattern.findall(sample_text)

print(result)


# QUESTION--8

# In[37]:


import re
def insert_spaces(text):
    pattern = re.compile(r'(?<=\d)(?=[A-Za-z])')
    processed_text = pattern.sub(' ',text)
    
    return processed_text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(sample_text)

print(result)


# QUESTION--9

# In[41]:


import re
def insert_spaces(text):
    pattern = re.compile(r'(?<=[A-Z0-9])(?=[A-Z][a-z])|(?<=[a-z0-9])(?=[0-9])')
    
    processed_text = pattern.sub(' ', text)
    
    return processed_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(sample_text)
print(result)


# QUESTION--10

# In[43]:


import pandas as pd

url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(url)
df['first_five_letters'] = df['Country'].str[:5]

print(df.head())


# QUESTION--11

# In[44]:


import re
def is_valid_string(text):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    match = pattern.search(text)
    
    if match:
        return True
    else:
        return False
    
strings = ["hey123", "how_are_you", "2521_", "_paris", "Iwant@string"]
for string in strings:
    print(f"{string}: {is_valid_string(string)}")


# QUESTION--12

# In[61]:


import re
def starts_with_number(text, number):
    pattern = re.compile(r'^' + re.escape(str(number)))
    match = pattern.search(text)
    
    if match:
        return True
    else:
        return False 
    
strings = ["123shoiab", "456aman", "789suraj", "hi123",]
number = 123
for string in strings:
    print(f"{string}: {starts_with_number(string, number)}")
    


# QUESTION--13

# In[62]:


def remove_leading_zeros(ip_address):
    octets = ip_address.split('.')
    octets_without_zeros = [str(int(octet)) for octet in octets]
    cleaned_ip_address = '.'.join(octets_without_zeros)
    
    return cleaned_ip_address

ip_address = "885.568.005.007"
cleaned_ip_address = remove_leading_zeros(ip_address)
print("orginal IP address:", ip_address)
print("cleaned IP address:", cleaned_ip_address)


# QUESTION--14

# In[65]:


import re
with open('sample_text.txt', 'r') as file:
        text = file.read()
        
pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}')
dates = pattern.findall(text)

for date in dates:
    print(date)


# QUESTION--15

# In[68]:


def search_literals(sample_text, searched_words):
    for word in searched_words:
        if word in sample_text:
            print(f"'{word}' found.")
        else:
            print(f"'{word}' not found.")
            
sample_text = "The quick brown fox jumps over the lazy dog."
searched_words = ['fox', 'dog', 'horse']
search_literals(sample_text, searched_words)


# QUESTION--16

# In[71]:


def search_and_find_location(sample_text, searched_word):
    index = sample_text.find(searched_word)
    if index != -1:
        print(f"'{searched_word}' found in the text at index {index}.")
    else:
        print(f"'{searched_word}' not found in the text.")
        
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

search_and_find_location(sample_text, searched_word)


# QUESTION--17

# In[72]:


def find_substrings(sample_text, pattern):
    start_index = 0
    while True:
        index = sample_text.find(pattern, start_index)
        if index == -1:
            break
        print(f"pattern '{pattern}' found at index {index}.")
        start_index = index +1
        
sample_text = 'python exercises, PHP exercises, c# exercises'
pattern = 'exercises'

find_substrings(sample_text, pattern)


# QUESTION--18

# In[73]:


def find_occurrence_and_position(sample_text, pattern):
    start_index = 0
    occurrence = 0
    while True:
        index = sample_text.find(pattern, start_index)
        if index == -1:
            break
        occurrence += 1
        print(f"Occurrence {occurrence} of pattern '{pattern}' found at index {index}.")
        start_index = index + 1
        
sample_text = 'name shoaib, name suraj, name sameer, name qadri'
pattern = 'name'

find_occurrence_and_position(sample_text, pattern)


# QUESTION--19

# In[78]:


from datetime import datetime
def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d-%m-%Y')
    
    return formatted_date
date_str = '2024-04-03'

formatted_date = convert_date_format(date_str)

print("orginal date:", "yyyy-mm-dd:", date_str)
print("formatted date:", "dd-mm-yyyy:", formatted_date)


# QUESTION--20

# In[79]:


import re
def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)
    
    return decimal_numbers
sample_text = "01.12  0132.123  2.31875  145.8  3.01  27.25  0.25"
result = find_decimal_numbers(sample_text)

print("Decimal numbers with precision of 1 or 2:",result)


# QUESTION--21

# In[80]:


def print_numbers_and_positions(text):
    for i, char in enumerate(text):
        if char.isdigit():
            print(f"Digit '{char}' found at position {i+1}")
            
sample_text = "hii2521world2125"
print_numbers_and_positions(sample_text)


# QUESTION--22

# In[81]:


import re
def extract_max_numeric_value(text):
    pattern = re.compile(r'\b\d+\b')
    numeric_values = pattern.findall(text)
    max_value = max(map(int, numeric_values))
    
    return max_value

sample_text = 'My marks in each semester are:947, 896, 926, 524, 734, 950, 642'
result = extract_max_numeric_value(sample_text)
print("Maximum numeric value is :", result)


# QUESTION--23

# In[82]:


import re
def insert_spaces(text):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    
    spaced_text = pattern.sub(' ', text)
    
    return spaced_text
sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces(sample_text)
print(result)


# QUESTION--24

# In[85]:


import re
sample_text = "Hello World, RegularExpressionsAreAwesome!"
pattern = re.compile(r'[A-Z][a-z]+')

matches = pattern.findall(sample_text)

print("Matches:",  matches)


# QUESTION--25

# In[87]:


import re

def remove_continuous_duplicates(sentence):
    pattern = re.compile(r'\b(\w+)(\s+\1)+\b', flags=re.IGNORECASE)
    modified_sentence = pattern.sub(r'\1', sentence)
    
    return modified_sentence
sample_text = "Hello hello world world"
modified_sentence = remove_continuous_duplicates(sample_text)
print("original sentence:",  sample_text)
print("duplicate words removed:",  modified_sentence)


# QUESTION--26

# In[88]:


import re

def ends_with_alphanumeric(text):
    pattern = re.compile(r'\w$')
    match = pattern.search(text)
    
    if match:
        return True
    else:
        return False
    
strings = ["shoaib123", "shoaib", "123shoaib123", "123456"]
for string in strings:
    print(f"Does the string '{string}' ends with an alphanumeric charecter? {ends_with_alphanumeric(string)}")


# QUESTION--27

# In[89]:


import re
def extract_hashtags(text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(text)
    
    return hashtags
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" no wo"""

hashtags = extract_hashtags(sample_text)
print("extract hashtags:", hashtags)


# QUESTION--28

# In[91]:


import re
def remove_special_symbols(text):
    pattern = re.compile(r'<U\+[A-Fa-f0-9]+>')
    cleaned_text = pattern.sub(' ', text)
    
    return cleaned_text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those Who are protesting #demonetization are all different party leaders"
cleaned_text = remove_special_symbols(sample_text)
print("cleaned text:", cleaned_text)


# QUESTION--29

# In[94]:


import re

def extract_date_from_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        
    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    dates = pattern.findall(text)
    
    return dates

filename = 'sample_text.txt'

dates = extract_dates_from_text(filename)
print("Extracted dates:", dates)


# QUESTION--30

# In[96]:


import re
def remove_words_of_length_2_to_4(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    cleaned_text = pattern.sub(' ',text)
    
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly"

cleaned_text = remove_words_of_length_2_to_4(sample_text)
print("cleaned text:",  cleaned_text)


# In[ ]:




