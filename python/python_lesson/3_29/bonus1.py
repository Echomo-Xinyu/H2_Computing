# this bonus1 is to solve thr problem of lisa's workbook problem
# quote as below

'''
1. Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters. Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. The format of Lisa's book is as follows:

a. There are n chapters in Lisa's workbook, numbered from 1 to n.
b. The ith chapter has P[i] problems, numbered from 1 to P[i].
c. Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
d. Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
e. The page number indexing starts at 1.

Write a function that, when given n, k and P, will return the number special problems in the book.

The above diagram depicts an example where n = 5, k = 3 and P = [4,2,6,1,10].
'''

# @n: number of chapters; @k: number of question in one page; 
# @P[]: array ith element store number of question in ith chapter
def findNumber(n, k, P):
    count = 0
    page_index = 1
    for i in range(n):
        chapter_question = P[i]
        chapter_pages = int((chapter_question+k-1)/k)
        for j in range(chapter_pages):
            if page_index >= j*k+1 and page_index <= min((j+1)*k, chapter_question):
                count += 1
            page_index += 1
    return count

print(findNumber(4, 1, [1, 1, 1, 1]))
print(findNumber(5, 3, [4, 2, 6, 1, 10]))

