#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Library:
    def __init__(self):
        self.no_of_Books = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.no_of_Books = len(self.books)
    
    def showInfo(self):
        print(f"The Library has {self.no_of_Books} books.The books are")
        for book in self.books:
            print(book)
        
        
L1 = Library()
L1.addBook("Harry Potter")
L1.addBook("Rich Dad,Poor Dad")
L1.addBook("Elementary and Advanced Mathematics ")
L1.showInfo()


# In[ ]:




