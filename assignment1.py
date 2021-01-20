with open('article.txt','rt', encoding='UTF8') as f:
    text=f.read()
word_list =text.replace(',',' ').replace('.',' ').replace('"',' ').split()
word_list_no_duplicate=list(set(word_list))
word_lower=[]
for i in word_list_no_duplicate:
    word_lower.append(i.lower())
word_count=[]
for word in word_lower:
    word_count.append((word_list.count(word),word))
n=0
for result in sorted(word_count, reverse=True):
    n+=1
    print(result[1],result[0])
    if n==3:
        break