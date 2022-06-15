#lexical Analyzer

from pickle import TRUE
import string

#input str
#print("-------|  Tubes Teori Bahasa & Automata - Kelompok 11 - IF4412  |-------")
#print(" I Wayan Ardi Satya Putra - Intan Fauzia Anwar - Muamar Fajar Rahmadani ")
#print("        1301201397              1301204539             1301204129\n")
#print("Terminal Kata : ulun | ikam | amang | wadai | iwak | ading")
#print("                abah | maigut | mamakan | manatak ")
#kalimat = input("Masukan Kata yang di cari: ")
def lexical(sentence):
    input_string = sentence.lower() + "#"

    #initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
    "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", 
    "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32",
    "q33", "q34","q35"
    ]

    transition_table = {}

    for i in state_list:
        for alphabet in alphabet_list:
            transition_table[(i, alphabet)] = "ERROR"
        transition_table[(i, "#")] = "ERROR"
        transition_table[(i, " ")] = "ERROR"

    # CFG
    # S ⇾ NN VB NN
    # NN ⇾ Ulun | Ikam | Amang | Wadai | Iwak | Ading | Abah
    # VB ⇾ Maigut | Mamakan | Manatak

    # For starting node (q0)
        transition_table[("q0", " ")] = "q0"

    # Finish state
        transition_table[("q34", "#")] = "ACCEPT"
        transition_table[("q34", " ")] = "q35"

        transition_table[("q35", "#")] = "ACCEPT"
        transition_table[("q35", " ")] = "q35"

    # string "Ulun"
        transition_table[("q35", "u")] = "q1"
        transition_table[("q0", "u")] = "q1"
        transition_table[("q1", "l")] = "q2"
        transition_table[("q2", "u")] = "q3"
        transition_table[("q3", "n")] = "q34"

    # string "Ikam"
    transition_table[("q35", "i")] = "q4"
    transition_table[("q0", "i")] = "q4"
    transition_table[("q4", "k")] = "q7"
    transition_table[("q7", "a")] = "q8"
    transition_table[("q8", "m")] = "q34"

    # string "Amang"
    transition_table[("q35", "a")] = "q9"
    transition_table[("q0", "a")] = "q9"
    transition_table[("q9", "m")] = "q15"
    transition_table[("q15", "a")] = "q16"
    transition_table[("q16", "n")] = "q14"
    transition_table[("q14", "g")] = "q34"

    # string "Wadai"
    transition_table[("q35", "w")] = "q17"
    transition_table[("q0", "w")] = "q17"
    transition_table[("q17", "a")] = "q18"
    transition_table[("q18", "d")] = "q19"
    transition_table[("q19", "a")] = "q20"
    transition_table[("q20", "i")] = "q34"

    # string "Iwak"
    transition_table[("q35", "i")] = "q4"
    transition_table[("q0", "i")] = "q4"
    transition_table[("q4", "w")] = "q5"
    transition_table[("q5", "a")] = "q6"
    transition_table[("q6", "k")] = "q34"

    # string "Ading"
    transition_table[("q35", "a")] = "q9"
    transition_table[("q0", "a")] = "q9"
    transition_table[("q9", "d")] = "q12"
    transition_table[("q12", "i")] = "q13"
    transition_table[("q13", "n")] = "q14"
    transition_table[("q14", "g")] = "q34"

    # string "Abah"
    transition_table[("q35", "a")] = "q9"
    transition_table[("q0", "a")] = "q9"
    transition_table[("q9", "b")] = "q10"
    transition_table[("q10", "a")] = "q11"
    transition_table[("q11", "h")] = "q34"

    # string "Maigut"
    transition_table[("q35", "m")] = "q21"
    transition_table[("q0", "m")] = "q21"
    transition_table[("q21", "a")] = "q22"
    transition_table[("q22", "i")] = "q23"
    transition_table[("q23", "g")] = "q24"
    transition_table[("q24", "u")] = "q25"
    transition_table[("q25", "t")] = "q34"

    # string "Mamakan"
    transition_table[("q35", "m")] = "q21"
    transition_table[("q0", "m")] = "q21"
    transition_table[("q21", "a")] = "q22"
    transition_table[("q22", "m")] = "q26"
    transition_table[("q26", "a")] = "q27"
    transition_table[("q27", "k")] = "q28"
    transition_table[("q28", "a")] = "q29"
    transition_table[("q29", "n")] = "q34"

    # string "Manatak"
    transition_table[("q35", "m")] = "q21"
    transition_table[("q0", "m")] = "q21"
    transition_table[("q21", "a")] = "q22"
    transition_table[("q22", "n")] = "q30"
    transition_table[("q30", "a")] = "q31"
    transition_table[("q31", "t")] = "q32"
    transition_table[("q32", "a")] = "q33"
    transition_table[("q33", "k")] = "q34"

    # lexical Analysis
    idx_char = 0
    state = "q0"
    current_token = ""
    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char
        print(state, current_char)
        state = transition_table[(state, current_char)]
        if state == "q34":
            print("current token: {} is valid".format(current_token))
            current_token = ""
        if state == "ERROR":
            print("error")
            break
        idx_char += 1

    # Conclusion
    if state == "ACCEPT":
        print("semua token yang di input: {} valid".format(input_string))
        return True