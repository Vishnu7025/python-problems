# for i in range(1,100+1):
#     if i%3==0 and i%5 == 0:
#         print("fizzbuzz")
#         continue
#     if i%3==0:
#         print('fizz')
#         continue
#     if i%5 == 0:
#         print('buzz')
#         continue
#     print(i)

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for letter in sentence:
    if letter in vowels:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
