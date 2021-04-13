# -*- coding: utf-8 -*-

novo_conjunto=[]
novo= []
stopwords= []
novo_stopwords = []

with open("./textos/A_Canção_dos_tamanquinhos_Cecília_Meireles.txt", encoding='utf-8') as file:
    for line in file:
       line=line.replace(",","")

       representation = line.split(' ')
       for word in representation:
           x = word.encode('utf-8')
           x = x.replace(b'\xe2\x80\xa6', b'')
           word = x.decode('utf-8')
           novo.append(word)
       novo_conjunto.extend(novo)

print(novo_conjunto)

with open("./stopwords/stopwords.txt", encoding='utf-8') as file:
    for line in file:
        stopwords.append( line.replace("\n",""))
