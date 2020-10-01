import io

def main():
    d1 = []#school
    d2 = [] #sex
    d3 = [] #age
    d4 = [] #address
    d5 = [] #family size
    d6 = [] #parent status
    d7 = [] # mum ed
    d8 = [] # dad ed
    d9 = [] # mum job
    d10 = [] # dad job
    d11 = [] # school reason
    d12 = [] # guardian
    d13 = [] # travel time
    d14 = [] # study time
    d15 = [] # failures
    d16 = [] # ed support
    d17 = [] # family support
    d18 = [] # tutor hired
    d19 = [] # extra activities
    d20 = [] # nursery attended
    d21 = [] # wants higher ed
    d22 = [] # has internet
    d23 = [] # in relationship
    d24 = [] # quality family relations
    d25 = [] # freetime
    d26 = [] # go out
    d27 = [] # work day alcohol
    d28 = [] # weekend alcohol
    d29 = [] # health
    d30 = [] # absences
    d31 = [] # Period 1
    d32 = [] # Period 2
    d33 = [] # Final Period
    

    input = io.open("student-por-tab.txt") # automatically defaults to input

    totalStudents = 0
    datalines = []
    stopit = False
    while stopit == False: # read all data
        t = input.readline()
        t = t.rstrip('\n')
        t = t + ";"
        if totalStudents < 640:
            datalines.append(t)
            totalStudents += 1
            #print(str(totalStudents))
        else:
            stopit = True
        
    print("--------------")

    for c in range(640):
        t = datalines[c] # copy a libe of data

        newword = ""
        wordcount = 1
        textcount = 0
        while wordcount < 34:
            #print("at " + str(wordcount))
            if t[textcount] != '"' and t[textcount] != ';':
                newword = newword + t[textcount]

            if t[textcount] == ';':
                #print("saving " + newword)

                if wordcount == 1:
                    d1.append(newword)
                elif wordcount == 2:
                    d2.append(newword)
                    #print(newword)
                elif wordcount == 3:
                    d3.append(int(newword)) # age
                elif wordcount == 4:
                    d4.append(newword)
                elif wordcount == 5:
                    d5.append(newword)
                elif wordcount == 6:
                    d6.append(newword)
                elif wordcount == 7:
                    d7.append(newword)
                elif wordcount == 8:
                    d8.append(newword)
                elif wordcount == 19:
                    d9.append(newword)
                elif wordcount == 10:
                    d10.append(newword)
                elif wordcount == 11:
                    d11.append(newword)
                elif wordcount == 12:
                    d12.append(newword)
                elif wordcount == 13:
                    d13.append(int(newword)) # traveltime
                elif wordcount == 14:
                    d14.append(int(newword)) # study time
                elif wordcount == 15:
                    d15.append(int(newword))# failures
                elif wordcount == 16:
                    d16.append(newword)
                elif wordcount == 17:
                    d17.append(newword)
                elif wordcount == 18:
                    d18.append(newword)
                    
                if wordcount == 19:
                    d19.append(newword)
                elif wordcount == 20:
                    d20.append(newword)
                elif wordcount == 21:
                    d21.append(newword)
                elif wordcount == 22:
                    d22.append(newword)
                elif wordcount == 23:
                    d23.append(newword)
                elif wordcount == 24:
                    d24.append(int(newword)) # family quality
                elif wordcount == 25:
                    d25.append(int(newword)) # freetime
                elif wordcount == 26:
                    d26.append(int(newword)) # go out
                elif wordcount == 27:
                    d27.append(int(newword)) # workday alcohol
                elif wordcount == 28:
                    d28.append(int(newword)) # weekend alcohol
                elif wordcount == 29:
                    d29.append(int(newword)) # health
                elif wordcount == 30:
                    d30.append(int(newword)) # absences
                elif wordcount == 31:
                    d31.append(int(newword)) # period 1
                elif wordcount == 32:
                    d32.append(int(newword)) # period 2
                elif wordcount == 33:
                    d33.append(int(newword)) # final period

                wordcount += 1
                
                newword = ""
            textcount += 1


    yesPassed1 = 0
    yesFailed1 = 0
    yesPassed2 = 0
    yesFailed2 = 0
    yesPassed3 = 0
    yesFailed3 = 0
    yesPassed4 = 0
    yesFailed4 = 0
    yesFailed5 = 0
   

    
    print("Total " + str(totalStudents))
    
    for c in range(totalStudents):
        #print("c " + str(c))
        #print(str(c) + " " + d20[c])
        #print(" " + str(d33[c]))
        
        numberdata = int(d14[c]) # search for this data
        
        if int(d28[c])  == 1 and int(d33[c]) > 9 and int(d27[c])  == 1: #10-20 is the past mark
            yesPassed1 += 1
        if int(d28[c]) == 2 and int(d33[c]) > 9 and int(d27[c])  == 2: #10-20 is the past mark
            yesPassed2 += 1

    yesPassed5 = 0
        if int(d28[c]) == 3 and int(d33[c]) > 9 and int(d27[c])  == 3: #10-20 is the past mark
            yesPassed3 += 1
        if int(d28[c]) == 4 and int(d33[c]) > 9 and int(d27[c])  == 4: #10-20 is the past mark
            yesPassed4 += 1
        if int(d28[c]) == 1 and int(d33[c]) < 10 and int(d27[c])  == 5 : #10-20 is the past mark
            yesFailed1 += 1
        if int(d28[c]) == 2 and int(d33[c]) < 10 and int(d27[c])  == 1 : #10-20 is the past mark
            yesFailed2 += 1
        if int(d28[c]) == 3 and int(d33[c]) < 10 and int(d27[c])  == 2 : #10-20 is the past mark
            yesFailed3 += 1
        if int(d28[c]) == 4 and int(d33[c]) < 10 and int(d27[c])  == 3 : #10-20 is the past mark
            yesFailed4 += 1
        if int(d28[c]) == 5 and int(d33[c]) < 10 and int(d27[c])  == 4: #10-20 is the past mark
            yesFailed5 += 1
        if int(d28[c]) == 5 and int(d33[c]) > 9 and int(d27[c])  == 5: #10-20 is the past mark
            yesPassed5 += 1
        
            
           
#yes = university, no = no university"
#data check to analysie the fairness of the data
            
    print("all week alcohol consumption log plot")
    print(str(yesPassed1) + "pass and study time 1") 
    print(str(yesFailed1) + "fail and study time 1")
    print(str(yesPassed2) + "pass and study time 2")
    print(str(yesFailed2) + "fail and study time 2")
    print(str(yesPassed3) + "pass and study time 3")
    print(str(yesFailed3) + "fail and study time 3")
    print(str(yesPassed4) + "pass and study time 4")
    print(str(yesFailed4) + "fail and study time 4")
    print(str(yesPassed5) + "pass and study time 5")
    print(str(yesFailed5) + "fail and study time 5")
    

main()


