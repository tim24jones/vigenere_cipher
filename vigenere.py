def char_to_number(char,alpha_str):
    for i in range(len(alpha_str)):
        if alpha_str[i]==char:
            return i

def num_to_char(num,alpha_str):
    return alpha_str[num]

def caesar(input_char,char,alpha_str):
    return num_to_char((char_to_number(input_char,alpha_str)+char_to_number(char,alpha_str))%len(alpha_str),alpha_str)

def vigenere(keyword,input_str,alpha_str):
    output=[]
    for i in range(len(input_str)):
        output=output+[caesar(input_str[i],keyword[i%len(keyword)],alpha_str)]
    return output

#sample query:
#print(vigenere('keyword','jjjjjjj','abcdefghijklmnopqrstuvwxy'))
