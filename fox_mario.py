import re


def remove_end_char(input_st):
    if not input_st[-1].isalnum():
        input_st = input_st[:-1]
    return input_st 


def generate_clean_words(eng_sentence, encrypted_sentence):
    eng_sentence = remove_end_char(eng_sentence)
    encrypted_sentence = remove_end_char(encrypted_sentence)
    eng_sentence = eng_sentence.upper()
    encrypted_sentence = encrypted_sentence.upper()
    eng_list = eng_sentence.split()
    encrp_list = encrypted_sentence.split()
    
    assert len(eng_list) == len(encrp_list)
    return eng_list, encrp_list


def generate_word_map(eng_list, encrp_list):
    word_map = {}
    for w1, w2 in zip(eng_list, encrp_list):
        for ch1, ch2 in zip(w1, re.findall('..', w2)):
            word_map[ch2] = ch1

    assert len(word_map) == 26
    return word_map


def test_word_map(word_map, input_test):
    output_test = ""  
    for char in re.findall('..', input_test):
        output_test += word_map[char]
    
    assert output_test == "PYTHON"
    return output_test


def main():
    eng_sentence = "The quick brown fox jumps over the lazy dog."
    encrypted_sentence = "VNOUNL UHEVJPZQWZ RIIWARFJTF PGARMX SKEVYOLYXC ARBANLIW VNOUNL HSKECDQM QPARDE."
    input_test = "LYQMVNOUARTF"
    eng_list, encrp_list = generate_clean_words(eng_sentence, encrypted_sentence)
    word_map = generate_word_map(eng_list, encrp_list)
    output_test = test_word_map(word_map, input_test)
    print("Decrypted message is:: %s" % output_test)


if __name__ == '__main__':
    main()

