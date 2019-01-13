import re

vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к',
              'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']











intab = "".join(vowels)
outtab = "*"
print(intab)
trantab = str.maketrans("", "", intab)

str = "корова"
print(str.translate(trantab))




