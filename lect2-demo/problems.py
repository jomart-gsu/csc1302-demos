# print all the numbers from 1 to 10
l = range(1, 11)
i = 0
while i < len(l):
    print(l[i])


# FUNCTION that takes a string and converts it to lowercase

def convert_to_lowercase(s):
    return s.lower()

print(convert_to_lowercase("AAAAHHHHH"))


# Age program

age = input("What is your age?")
if age >= 35:
    print("You can run for president")
elif age >= 25:
    ...
else:
    ...


# sum up every other element of a list
def sum_every_other(l):
    return sum(l[::2])

# clearer/longer version
def sum_every_other(l):
    total = 0
    for i in range(len(l)):
        if i % 2 == 0:
            total += l[i]
    return total


print(sum_every_other([1,2,3,4]))




# functions to check if a string is a palindrome
def is_palindrome(s):
    return s[::-1] == s  # [::-1] reverses a list or string

def is_palindrome(s):
    i = 0
    j = len(s) - 1  # why len(s) - 1 instead of just len(s)??

    # move i and j toward each other, checking that opposite letters match
    while i < j:
        if s[i] != s[j]:
            return False
    return True


# code-breaking
code = "Ilhbapmbs pz ilaaly aohu bnsf. Lewspjpa pz ilaaly aohu ptwspjpa. Zptwsl pz ilaaly aohu jvtwsle. Jvtwsle pz ilaaly aohu jvtwspjhalk. Msha pz ilaaly aohu ulzalk. Zwhyzl pz ilaaly aohu kluzl. Ylhkhipspaf jvbuaz. Zwljphs jhzlz hylu'a zwljphs luvbno av iylhr aol ybslz. Hsaovbno wyhjapjhspaf ilhaz wbypaf. Lyyvyz zovbsk ulcly whzz zpsluasf. Buslzz lewspjpasf zpslujlk. Pu aol mhjl vm htipnbpaf, ylmbzl aol altwahapvu av nblzz. Aolyl zovbsk il vul-- huk wylmlyhisf vusf vul --vicpvbz dhf av kv pa. Hsaovbno aoha dhf thf uva il vicpvbz ha mpyza buslzz fvb'yl Kbajo. Uvd pz ilaaly aohu ulcly. Hsaovbno ulcly pz vmalu ilaaly aohu *ypnoa* uvd. Pm aol ptwsltluahapvu pz ohyk av lewshpu, pa'z h ihk pklh. Pm aol ptwsltluahapvu pz lhzf av lewshpu, pa thf il h nvvk pklh. Uhtlzwhjlz hyl vul ovurpun nylha pklh -- sla'z kv tvyl vm aovzl!"

# count every letter and assume the most frequent one is e
counts = {}
for letter in code:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

# print(counts)

new_code = ""
# we found that 'l' is the most frequent, which is 7 positions ahead of 'e' (efghijkl)
# so now let's shift all the characters in the code back by 7 positions
for letter in code:
    # you can look up ord(), but tl;dr it converts characters to ASCII values
    # 'a' is 77, for example
    letter_val = ord(letter)
    new_letter_val = letter_val - 7
    new_letter = chr(new_letter_val)  # chr() moves us from a number to a character (reverse of ord())
    new_code += new_letter

print(new_code)

# TODO:
# - make early letters "wrap around"
# - handle capital letters?
# Give these a shot if you want more Python practice!

