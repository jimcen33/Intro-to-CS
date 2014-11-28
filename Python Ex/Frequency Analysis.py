# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    letterString='abcdefghijklmnopqrstuvwxyz'
    total_char=len(message)
    i=0      #counter
    temp=''  #temporary string for message
    count=0  #count the number of occurrences
    freq_list=[]  #frequency list
    temp=message #Assign message to temp
    while i<=25:               #Loop through the 26 letter-string 
        letter=letterString[i]      
        location=temp.find(letter)       #Find if there exists in the message, yes then increment count  
        if location>=0:
            count+=1
            temp=temp[location+1:]       #Assign temp to the rest of the message 
        else:                           
            i+=1                         #If no, then find the next letter
            freq_list.append(count*1.0/total_char)    #count the number of occurrences
            count=0                      #Reset count for the next letter
            temp=message                 #Reset temp to the full message
    return freq_list



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]}