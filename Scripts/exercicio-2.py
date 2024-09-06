# Substituindo caractere repetido
name = "Fifa 23"

char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]

name2 = "Resident Evil"
char = name2[3].lower()
new_name2 = name2.replace(char, '$')
print(new_name2[:3] + char + new_name2[4:])

# Troca de caracteres
str1 = "cad"
str2 = "opx"
strResult1 = str2[:2]  + str1[2]
strResult2 = str1[:2] + str2[2]
print(strResult1, " - ", strResult2)