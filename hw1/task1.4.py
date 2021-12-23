words = ['разработка', 'администрирование', 'protocol', 'standard']
b_words = []
for i in words:
    b_words.append(i.encode('utf-8'))
print(b_words)
for j in b_words:
    print(j.decode('utf-8'))
