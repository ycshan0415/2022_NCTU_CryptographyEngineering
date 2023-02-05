# !/bin/python

import string
import math
import random

def create_cipher_dict(key):
    cipher_dict = {}
    alphabet_list = list(string.ascii_uppercase)
    # [A, B, ..., Z]
    for i in range(len(key)):
        cipher_dict[alphabet_list[i]] = key[i]

    return cipher_dict

def encrypt(text, key):
    cipher_dict = create_cipher_dict(key)
    text = list(text)
    newtext = ""
    for elem in text:
        if elem.upper() in cipher_dict:
            newtext += cipher_dict[elem.upper()]
        else:
            newtext += " "
    return newtext

# This function takes input as a path to a long text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration
def create_scoring_params_dict(longtext_path):
    #TODO
    scoring_params = {}
    alphabet_list = list(string.ascii_uppercase)
    # [A, B, ..., Z]
    with open(longtext_path, encoding = "utf-8") as lp:
        for line in lp:
            data_list = list(line.strip())
            # ignore whitespace
            for i in range(len(data_list) - 1):
                former = data_list[i].upper()
                if former not in alphabet_list and former != " ":
                    former = " "
                latter = data_list[i + 1].upper()
                if latter not in alphabet_list and latter != " ":
                    latter = " "
                key = former + latter
                if key not in scoring_params:
                    scoring_params[key] = 1
                else:
                    scoring_params[key] += 1

    return scoring_params
    # pass

# This function takes input as a text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration
def score_params_on_cipher(text):
    #TODO
    scoring_params = {}
    alphabet_list = list(string.ascii_uppercase)
    # [A, B, ..., Z]
    data_list = list(text.strip())
    # ignore whitespace
    for i in range(len(data_list) - 1):
        former = data_list[i].upper()
        if former not in alphabet_list and former != " ":
            former = " "
        latter = data_list[i + 1].upper()
        if latter not in alphabet_list and latter != " ":
            latter = " "
        key = former + latter
        if key not in scoring_params:
            scoring_params[key] = 1
        else:
            scoring_params[key] += 1
    
    return scoring_params
    # pass

# This function takes the text to be decrypted and a cipher to score the cipher.
# This function returns the log(score) metric
def get_cipher_score(text,cipher,scoring_params):
    #TODO
    decrypted = encrypt(text, cipher)
    fx = score_params_on_cipher(decrypted)
    score = 0
    for key, value in fx.items():
        if key in scoring_params:
            score += value * math.log(scoring_params[key])
    # Score(x) = ∏ 𝑅(𝛽_1,𝛽_2)^(𝐹_𝑥(𝛽_1,𝛽_2))
    # log(Score) = Fx * log(R)
    # log(∏) = ∑
    # score = ∑(Fx * log(R))
    return score
    # pass


# Generate a proposal cipher by swapping letters at two random location
def generate_cipher(cipher):
    #TODO
    pos1 = random.randint(0, len(list(cipher)) - 1)
    pos2 = random.randint(0, len(list(cipher)) - 1)
    if pos1 == pos2:
        return generate_cipher(cipher)
    else:
        cipher = list(cipher)
        temp = cipher[pos1]
        cipher[pos1] = cipher[pos2]
        cipher[pos2] = temp
        # swap
        return ''.join(cipher)
    # pass

# Toss a random coin with robability of head p. If coin comes head return true else false.
def random_coin(p):
    #TODO
    result = random.random() < p
    # returns a uniformly distributed pseudo-random floating point number in the range [0, 1).
    # This number is less than a given number p in the range [0,1) with probability p.
    if result:
        return True
    else:
        return False
    # pass

# Takes input as a text to decrypt and runs a MCMC algorithm for n_iter. Returns the state having
# maximum score and also the last few states
def MCMC_decrypt(n_iter,cipher_text,scoring_params):
    current_cipher = string.ascii_uppercase # Generate a random cipher to start
    best_state = ''
    score = 0
    for i in range(n_iter):
        proposed_cipher = generate_cipher(current_cipher)
        score_current_cipher = get_cipher_score(cipher_text,current_cipher,scoring_params)
        score_proposed_cipher = get_cipher_score(cipher_text,proposed_cipher,scoring_params)
        acceptance_probability = min(1,math.exp(score_proposed_cipher-score_current_cipher))
        if score_current_cipher>score:
            best_state = current_cipher
        if random_coin(acceptance_probability):
            current_cipher = proposed_cipher
        if i%500==0:
            print("iter",i,":",encrypt(cipher_text,current_cipher)[0:99])
    return best_state

def main():
    ## Run the Main Program:
    scoring_params = create_scoring_params_dict('war_and_peace.txt')

    with open('ciphertext.txt','r', encoding="utf-8") as f:
        cipher_text = f.read()
    print(cipher_text)

    print("Text To Decode:", cipher_text)
    print("\n")
    best_state = MCMC_decrypt(10000,cipher_text,scoring_params)
    print("\n")
    plain_text = encrypt(cipher_text,best_state)
    print("Decoded Text:",plain_text)
    print("\n")
    print("MCMC KEY FOUND:",best_state)

    with open('plaintext.txt','w+') as f:
        f.write(plain_text)


if __name__ == '__main__':
    main()