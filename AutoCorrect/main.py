# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:53:32 2023

@author: winso
"""
if __name__ == "__main__":
    import string
    def remove_char(s, index):
        return s[:index] + s[index+1:]
    '''
    dict_file = 'words_10percent.txt'
    input_file = 'input_words.txt'
    keyboard_file = 'keyboard.txt'
    '''
    #inputs    
    file_input = open("input.txt").read().strip().split('\n')
    
    file_dict = open('20k.txt').read().strip().split('\n')
    dictionary = dict()
    
    file_keyboard = open('keyboard.txt').read().strip().split('\n')
    file_key = dict()
    #stores the keyboard in a dictionary
    for line in file_keyboard:
        line = line.split(' ')
        temp = line[0]
        line.pop(0)
        file_key[temp]=line
    #stores the word and its commonality as a dictionary
    index = 0;
    for line in file_dict:
        words = line.strip().split(',') 
        dictionary[words[0]] = index
        index+=1
    
    
    outputfile = open("output.txt", "w")
    
    #start of the calculations
    for line in file_input:
        line = line.split(" ")
        correctLine = ""
        #strips the word for comparasons
        for x in range(len(line)):
            if (line[x][len(line[x])-1] == "."):
                line[x] = remove_char(line[x],len(line[x])-1)
            word = line[x].strip()
            word = word.lower()
            
            if word in dictionary:
                if x==0:
                    correctLine += line[x].capitalize()+" "
                elif x!=len(line):
                    correctLine += line[x]+" "
                else:
                    correctLine += line[x]+"."
            else:
                #stores the potentially correct words 
                good_words = []  
                #drop
                for d in range(len(word)):
                    temp = list(word)
                    temp.pop(d)
                    temp = ''.join(temp)
                    if temp in dictionary:
                        good_words.append(temp)
                        
                #insert
                abc = list(string.ascii_lowercase)
                for i in range(len(word)+1):
                    for l in range(len(abc)):
                        temp = list(word)
                        temp.insert(i, abc[l])
                        temp = ''.join(temp)
                        if temp in dictionary:
                            good_words.append(temp)
                            
                #swap
                for i in range(len(word)-1):
                    temp = list(word)
                    first = temp[i]
                    sec = temp[i+1]
                    temp[i] = sec
                    temp[i+1] = first
                    temp = ''.join(temp)
                    if temp in dictionary:
                        good_words.append(temp)
                    
                #replace
                for l in range(len(word)):
                    for letter in file_key[temp[l]]:
                        temp = list(word)
                        temp[l]=letter
                        temp = ''.join(temp)
                        if temp in dictionary:
                            good_words.append(temp)
                # replaces any duplicates
                good_words = set(good_words)
                good_words = list(good_words)
                #if nothign can be found just add the incorrect word
                if len(good_words)==0:
                    if x==0:
                        correctLine += line[x].capitalize()+" "
                    elif x!=len(line):
                        correctLine += line[x]+" "
                    else:
                        correctLine += line[x]+"."
                else:
                    sortedGoodWord = sorted(good_words, key = lambda word: (dictionary[word],word), reverse = False)
                    if x==0:
                        correctLine += sortedGoodWord[0].capitalize()+" "
                    elif x!=len(line):
                        correctLine += sortedGoodWord[0]+" "
                    else:
                        correctLine += sortedGoodWord[0]+"."
            
        correctLine = remove_char(correctLine, len(correctLine)-1)
        correctLine+=".\n"
        outputfile.write(correctLine)
    outputfile.close()