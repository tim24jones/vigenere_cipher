#functions are untested unless a sample test call exists below them.
def keylen_sep(input_str,keylength): #separate message into strings encoded by each letter of the keyword
    str_list=['']*(keylength)
    for j in range(keylength):
        for i in range(len(input_str)):
            if i%keylength==j:
                str_list[j]=str_list[j]+input_str[i]
    return str_list

# print(keylen_sep('reallylongstringoflettersthatcreateamessagetobesplitupintopieceswhichdoesntneedtoavoidspacesthewayimdoing',4))

def keylist decode(input_str,alpha_str,keylength): #take list of coded strings and switch values for decoded values
    decoded_strings=['']*len(str_list)
    keylen_sep(input_str,alpha_str,keylength)
    for a in range(len(str_list):
        dict_sort(str_list[a],alpha_str)
        for b in range len(str_list[a]):
            decoded_strings[a]=decoded_strings[a]+keydict.get(str_list[a][b])
    return decoded_strings

def keylen_integ(decoded_strings,keylength):
    decoded_strings,keylength
    for i in range(len(decoded_strings[0])):
        for j in range(len(decoded_strings)):
            decoded_list=decoded_list+[decoded_list[i][j]]
    glue=''
    message=glue.join(decoded_list)
    return message
#print(keylen_integ(['aei','bfj','cgk','dhl'],3))
                   
def dict_freq_count(p,letter): #counting function used in dict_freq
    letter=str(letter)
    a=0
    t=0
    for i in range (len(p)):
        if p[i]==letter:
            a=a+1
            t=t+1
        else:
            t=t+1
    dict={letter:a}
    return(dict)

def dict_freq(input_str,alpha_str): #create a list of letters by frequency, also contains dictionary of coded letter frequency, currently not used
    frequency_list=[]
    for i in range(len(alpha_str)):
        frequency_dict={}
        frequency_list=frequency_list+frequency_dict.items()+dict_freq_count(input_str,alpha_str[i]).items()
    valuelist=frequency_list
    return valuelist

# print(dict_freq('abedabededg','abcdefgh')) (tests both dict_freq and dict_freq_count)

def dict_sort(input_str,alpha_str): #sort dictionary by value, use keys of dict_freq and known list of character frequency to create a new dict
    letter_str=' etaoinsrhldcumfpgwybvkxjqz' #... use these chars as values for new dictionary
    keylist=[]
    valuedict=dict_freq(input_str,alpha_str)
    for i in range(len(letter_str)):
        keylist=keylist+[letter_str[i]]
    keydict=dict(zip(keylist,list(valuedict.keys()))
    return keydict

#print(dict_sort('aaaaaaaabbbbbbcccccddddeeef','aeinot'))

#compare letter frequency for each char of keyword, fill in those which match, 
#after that, either:
# show message with blanks for user to guess (first implementation)
# show message and let user choose best of the calculated options
# compare discrepancies and choose options which create words (or the most words)

                                 
#still to be done:
# def decode_with_unknown_keylength(input_str,alpha_str)
#the same as the first, but iterating over keylength
                   
#notes for decoding process:

#letter frequency stats:
#space:16.393
#E:10.44
#T:7.759
#A:6.722
#O:6.388
#I:6.329
#N:6.045
#S:5.443
#R:5.251
#H:4.222
#L:3.403
#D:3.194
#C:2.792
#U:2.282
#M:2.099
#F:2.007
#P:1.789
#G:1.563
#W:1.405
#Y:1.388
#B:1.237
#,
#.
#V:0.8779
#'
#"
#-
#K:0.4515
#X:0.1923
#0
#J:0.1338
#1
#Q:0.1003
#2
#Z:0.0752
#then ():!?5;349/867[]%$|*=_+>\<&^#@`~{}

#can use enchant for spell checking:
#import enchant
#d=enchant.Dict("en_US") 
#or maybe British english could be an option
#d.check("Hello")
#d.check("Helo")
#d.suggest("Helo")
