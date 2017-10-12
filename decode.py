def keylen_sep(input_str,alpha_str,keylength:) #separate message into strings encoded by each letter of the keyword
    str_list=[] #list made of strings separated by keyletter
    for i in range(len(keylength):
        for j in range(len(input_str)):
            if j%keylength==i:
                str_list=str_list+[keylength%i]
     return str_list

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
    for i in range(len(decoded_strings)):
        for j in range(len(decoded_strings[i]):
            decoded_list=decoded_list[i][j] #function still to be finished
                   
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
    for i in range(len(alphastr)):
        dict_freq={}
        dict_freq=dict_freq.items()+dict_freq_count(newstr,alphastr[i]).items()
        sorted_tuple_list=sorted(dict_freq.items(),key=lambda x:x[1]
        valuelist=dict_freq.items
        return valuelist

def dict_sort(input_str,alpha_str): #sort dictionary by value, use keys of dict_freq and known list of character frequency to create a new dict
    letter_str=' etaoinsrhldcumfpgwybvkxjqz' #... use these chars as values for new dictionary
    keylist=[]
    valuelist=dict_freq(input_str,alpha_str)
    for i in range len(letter_str):
        keylist=keylist+letter_str[i]
    keydict=dict(zip(keylist,valuelist))
    return keydict

#compare letter frequency for each char of keyword, fill in those which match, 
#after that, either:
# show message with blanks for user to guess (first implementation)
# show message and let user choose best of the calculated options
# compare discrepancies and choose options which create words (or the most words)

Could use a new class to show these:

class def decoding_message #possibly useful for later cases, create class with a length of input_str, add letters to middle, display null as _
    __init__():#all the variables used for decoding
    __str__(partial_keyword,partial_input_str):

#in the future:
def decode_with_unsequential_alpha(input_str,keylength)
# have to order completely by letter frequency.  Could use word suggest, monocharacters 'I' and 'a', common digraphs, trigraphs etc. to help

def decode_with_unknown_keylength(input_str,alpha_str)
#this will be the same as the first, but iterate over keylength
                   
#and hopefully putting them together to the ultimate goal:
def decode(input_str):
#which should output both the keyword and the output_string
                   
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

#decode with known key length (probably recommended as first step), detect possible words
#decode probably limited to letters only initially
#could display version with most English words or letters within words
#extend by repeating for increased key length
