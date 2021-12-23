word1 = 'разработка'
word2 = 'cокет'
word3 = 'декоратор'

word1_bytes = word1.encode('utf-8')
print(word1_bytes)
print(type(word1_bytes))

word2_bytes = word2.encode('utf-8')
print(word2_bytes)
print(type(word2_bytes))

word3_bytes = word3.encode('utf-8')
print(word3_bytes)
print(type(word3_bytes))

print(word1_bytes.decode('utf-8'))
print(type(word1_bytes.decode('utf-8')))
