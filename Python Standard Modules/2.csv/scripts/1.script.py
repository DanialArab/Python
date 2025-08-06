 # 1st sample  question. Simple CSV or text file with documents
 
# - Parse the text data
# - Compute word frequencies
# - Identify documents that contain a certain keyword
# - Build a simple inverted index (word → list of doc_ids)
# - Return top N documents by some metric (e.g., frequency of keyword, length)

import csv 
import string 
from collections import Counter, defaultdict 

class CsvParser:
    def __init__(self):
        self.data = None 

    def data_loader(self, path):
        with open (path, mode = 'r', encoding='utf-8', newline='') as f:
            my_data = csv.DictReader(f)
            self.data = [row for row in my_data]
            return self.data 
        
    def word_fre_per_row(self):
        if not self.data:
            print('run data_loader first')
            return 
        my_dict = {}
        for item in self.data:
            doc_id = item.get('doc_id')
            text = item.get('text', 0)
            w_list = text.split()
            w_list_cleaned = [w.strip(string.punctuation).lower() for w in w_list]
            count = Counter(w_list_cleaned)
            my_dict[doc_id] = count
        return my_dict

    def doc_identifier(self, keyword):
        keyword = keyword.lower()
        if not self.data:
            print ('run data_loader first')
            return 
        
        res = [] 
        for item in self.data:
            doc_id = item.get('doc_id', 0)
            text = item.get('text', '')
            w_cleaned = [w.strip(string.punctuation).lower() for w in text.split()]
            if keyword in w_cleaned:
                res.append(doc_id)
        return res 
    
    def inverted_list(self):
        if not self.data:
             print ('run data_loader first')
             return 
        res = defaultdict(set)
        for item in self.data:
            doc_id = item.get('doc_id')
            text = item.get('text', 0)
            w_list = text.split()
            w_list_cleaned = [w.strip(string.punctuation).lower() for w in w_list]
            for w in w_list_cleaned:
                res[w].add(doc_id)

        return dict(res)

    def top_doc_retriever(self, keyword, top_k):
        keyword = keyword.strip(string.punctuation).lower()

        if not self.data:
             print ('run data_loader first')
             return 
        
        res = defaultdict(int)
        for item in self.data:
            doc_id = item.get('doc_id')
            text = item.get('text', 0)
            w_list = text.split()
            w_list_cleaned = [w.strip(string.punctuation).lower() for w in w_list]
            count = Counter(w_list_cleaned)
            res[doc_id] = count[keyword]
        sorted_res =  [k for k, v in sorted(res.items(), key = lambda x:x[1], reverse = True)][:top_k]
        return sorted_res

    def data_saver(self, output_file, data_to_write):
        with open (output_file, mode = 'w', encoding='utf-8', newline = '') as f:
            fieldnames = data_to_write[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_write)

csv_obj = CsvParser()
# print (csv_obj.data_loader('text.csv'))
data = csv_obj.data_loader('text.csv')

# print (csv_obj.word_fre_per_row())
# print(csv_obj.doc_identifier('Ai'))
# print (csv_obj.inverted_list())
print (csv_obj.top_doc_retriever('the', 2))
csv_obj.data_saver('saved_data.csv', data)