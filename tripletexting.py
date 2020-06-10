# Problem: https://open.kattis.com/problems/tripletexting

# Get input
message = input("")

# Init var
word_len = int(len(message) / 3)
word_v1 = message[:word_len]
word_v2 = message[word_len:word_len * 2]
word_v3 = message[word_len * 2:]

# We are told two of three words will match and the two that do
# must be what grandma meant. Print that word
if word_v1 == word_v2 or word_v1 == word_v3:
    print(word_v1)
else:
    print(word_v2)
