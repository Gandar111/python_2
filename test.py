words={"a", "b", "c","e"}
nummers={1,12,33,5,6,77}
def methode(word):
     multi= 2*word
     return multi/2
     
erg= [ methode(word) for word in nummers]
print(erg)

        