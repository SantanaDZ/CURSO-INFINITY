vogais = 0
palavra = input('Digite uma palavra: ')
for l in palavra:
    if l.lower() in "aeiou":
        vogais += 1
print(vogais)
