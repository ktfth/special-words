
novo_conjunto=[]
novo= []
stopwords= []
novo_stopwords = []

with open("./textos/A_Canção_dos_tamanquinhos_Cecília_Meireles.txt", encoding='utf-8') as file:
    for line in file:
       line=line.replace(",","")

       novo = line.split()
       novo_conjunto.extend(novo)

print(novo_conjunto)

with open("./stopwords/stopwords.txt", encoding='utf-8') as file:
    for line in file:
        stopwords.append( line.replace("\n",""))

