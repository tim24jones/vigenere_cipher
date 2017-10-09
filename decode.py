def decode_with_sequential_alpha(input_str,alpha_str,keylength):
    str_list=[] #list made of strings separated by keyletter
    for i in range(len(keylength):
        for j in range(len(input_str)):
            if j%keylength==i:
                str_list=str_list+[keylength%i]
    for item in len(str_list):
        letter_freq(item)
            #then sort dictionary into a list by alpha_str
            #set highest frequency to space, then e, then t, then a
            #check for the other of these 4 letters to have high frequency before iterating to the next
            #repeat for next list item
            #put together, test for words to verify or display

def letter_freq: #create dictionary for letter freqency

class def decoding_message #possibly useful for later cases, create class with a length of input_str, add letters to middle, display null as _

def check_for_words:


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
