from __future__ import division


def get_int(help_text): #defining a function to ask the user for an interger
    out_put = input(help_text) 
    while out_put.isnumeric() == False: #check input is a number
        out_put = input ("please enter an interger: ") #if false ask again
    return int(out_put)

height = get_int ('Ladder Height ') #get ladder height 

if height > 6000:
    print('WARNING! Ladder height over legal height')
top_space = get_int ('top floor ') #get top floor type
bottom_space = get_int('bottom floor ') #get bottom floor type

rung_length = height + top_space - 10 - bottom_space #accounting for floor type top and bottom and top rung center

maxspace = 300 #set max and min rung spacing        
minspace = 225

lad_list = [] #create emplty list to find lowest remainder 

perfect_sol = False #set perfect solution to flase

for i in range (maxspace, minspace, -1):
    
    x = rung_length % i #check for perfect dividors
    if x == 0: #if there is a perfect dividor 
        print ('rung spacing of ' + str(i)) #print the length
        perfect_sol = True #flips perfect solution
        lad_list.append(x)
        break
        
    lad_list.append(x)    #creates a list of all remainders

'''print (min(lad_list))
print (lad_list)'''

nosol = False

if  min(lad_list) != 0 and maxspace / min(lad_list) < 5:
    print ("No Solution")
    nosol = True

else: 

    if perfect_sol == False: #checks if there's a perfect solution
        for j in range (maxspace, minspace, -1): 
            
            x = (rung_length - (min(lad_list))) % j #reruns test
            if x == 0:
                y = j + int(min(lad_list))
                print ('rung spacing = ' + str(j))
                print ('first step = ' + str(y))   
                break


if nosol == False and rung_length > 1800:
        print (str(height-1800) + 'mm cage needed')
elif nosol == False:
    print ('cage not needed')