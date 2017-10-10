def keylen_sep(input_str,alpha_str,keylength:) #separate message into strings encoded by each letter of the keyword
    str_list=[] #list made of strings separated by keyletter
    for i in range(len(keylength):
        for j in range(len(input_str)):
            if j%keylength==i:
                str_list=str_list+[keylength%i]

def dict_freq(str_list) #create dict of letter frequency
    return dict_freq

def dict_sort(dict_freq,alpha_str) #sort dictionary
    return letter_list

#create dictionary of letter_list to letter_frequency (defined string etaoinsrh...

#fill in message one letter at a time, check for new words after each time, reject or confirm letter by use of new words, iterate to next likely frequency if non-word strings show up.  If all have non-word strings, output option with most word strings.

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
