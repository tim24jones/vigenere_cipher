#alphabet handling leftover code

    mode=input("Please select mode: Type 'printable' to use numbers, letters, punctuation, and spaces but not whitespaces other control characters. Type 'letters and numbers' 'letters' 'lowercase' or 'numbers' to use those options, or 'custom' to type a different alphabet.")
    modelettered=filter(lambda x:x in (string.letters)
    if modelettered.lower==('printable'):
        alpha_str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+\\|]}[{\'\";:/?.>,< '
        message_str=filter(lambda x:x in (string.digits+string.letters+string.punctuation+' '),input_str)
    elif modelettered.lower==('lettersandnumbers'):
        alpha_str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        message_str=filter(lambda x:x in (string.digits+string.letters+' '),input_str) 
    elif modelettered.lower==('letters'):
        alpha_str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        message_str=filter(lambda x:x in (string.letters+' '),input_str) 
    elif modelettered.lower==('lowercase'):
        alpha_str='abcdefghijklmnopqrstuvwxyz '
        message_str=filter(lambda x:x in (string.lowercase+' '),input_str) 
    elif modelettered.lower==('uppercase'):
        print('SHOUTING!')
        beta_str='abcdefghijklmnopqrstuvwxyz '
        alpha_str=beta_str.upper
        message_str=filter(lambda x:x in (string.uppercase+' '),input_str) 
    elif modelettered.lower==('numbers'):
        print("Base 10 assumed.  You can use 'letters and numbers' mode or 'custom' for others")
        alpha_str='0123456789 '
        message_str=filter(lambda x:x in (string.digits+' '),input_str) 
    elif modelettered.lower==('custom'):
        alpha_str_input=("Type the full alphabet you will use, in order, with no letter repetitions.  Include a space if you need it.")
        if check_for_repetitions(alpha_str):
            return alpha_str=alpha_str_input
        else:
            answer=input("Use alphabet without repetitions?\n",alpha_no_dups(alpha_str_input)"\n Type 'yes' or start over.")
            if answer==yes:
                return alpha_str=alpha_no_dups(alpha_str_input)
            else:
                Print("This didn't seem to work.  Why don't you start over.")
        else:
            Print("I did not understand that option.  Why don't you start over.")
    message_str=filter(lambda x:x in (string.digits+string.letters+string.punctuation+' '),input_str) #taking out all characters other than digits, lettters, punctuation and spaces
    vigenere(keyword,message_str)
    #glue together list into output_string

def alpha_no_dups(input_string):
#check for duplicate characters in a string
