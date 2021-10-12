print("\nDigite uma frase para verificar se é palindrome")
word = input()

print("\nAo contrário: " + "".join(reversed(word)))

word = word.replace(" ", "")
print ('\nA frase possui: ' + str(len(word)) + " caracteres")

print("\nO caracter do meio é > " + word[int((len(word)) / 2)] + " <")

if str(word) == "".join(reversed(word)) :
    print("\nÉ Palindrome")
else:
    print("\nNão é Palindrome\n")
    
