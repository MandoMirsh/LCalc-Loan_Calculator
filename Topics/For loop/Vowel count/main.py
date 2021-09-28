string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowel_num = 0
for x in string:
    if x in vowels:
        vowel_num += 1
print(vowel_num)
