# Group the usernames by their starting letter
from itertools import groupby 

class IterTools:
    def __init__(self):
        self.usernames =  [] 

    def data_loader(self, file_path):
        with open (file_path, mode = 'r', encoding='utf-8') as f:
            content = f.read().strip()
            for username in content.split(','):
                self.usernames.append(username.strip().strip("'"))
            return self.usernames

    def username_grouper(self):

        sorted_usernames = sorted(self.usernames, key = lambda x:x[0])
        grouped = groupby(sorted_usernames, key = lambda x:x[0])
        return {k: list(g) for k, g in grouped}
    
my_iter = IterTools()

# print (my_iter.data_loader('usernames.txt'))
my_iter.data_loader('usernames.txt')
print(my_iter.username_grouper())