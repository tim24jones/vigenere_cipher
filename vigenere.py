def char_to_number(char,alpha_str):
    for i in range(len(alpha_str)):
        if alpha_str[i]==char:
            return i

def num_to_char(num,alpha_str):
    return alpha_str[num]

def caesar(input_char,char,alpha_str,mode):
    if mode=='encode':
        return num_to_char((char_to_number(input_char,alpha_str)+char_to_number(char,alpha_str))%len(alpha_str),alpha_str)
    if mode=='decode':
        return num_to_char((char_to_number(input_char,alpha_str)-char_to_number(char,alpha_str))%len(alpha_str),alpha_str)
    else:
        print("Last argument must be 'encode' or 'decode'")
    #yes, it's just the difference between + and minus
    
def vigenere(keyword,input_str,alpha_str,mode):
    output=[]
    for i in range(len(input_str)):
        output=output+[caesar(input_str[i],keyword[i%len(keyword)],alpha_str,mode)]
    return output

#sample query:
#vigenere('keyword','string to be encoded','abcdefghijklmnopqrstuvwxy ','encode')
#don't need z in the alphabet if it's neither in the keyword nor the message
