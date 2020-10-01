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


    yesPassed = 0
    yesFailed = 0
    noPassed = 0
    noFailed = 0

    
    print("Total " + str(totalStudents))
    
    for c in range(totalStudents):
        #print("c " + str(c))
        #print(str(c) + " " + d20[c])
        #print(" " + str(d33[c]))
        
        numberdata = int(d14[c]) # search for this data
        
        if numberdata < 4 and d33[c] > 9:
            yesPassed += 1
        if numberdata  < 4 and d33[c] < 10:
            yesFailed += 1
        if numberdata > 3 and d33[c] > 9:
            noPassed += 1
        if numberdata > 3 and d33[c] < 10:
            noFailed += 1
#yes = more than 5 hours , no = less than 5 hours"
#data check to analysie the fairness of the data
            
    print("weekly study time 9 or less hours/10 or more hours")
    totalYesNo = yesPassed + yesFailed + noPassed + noFailed
    print("Total counted : " + str(totalYesNo))
    print("yes passed " + str(yesPassed) + " % " + str(yesPassed*100/totalYesNo))
    print("yes failed " + str(yesFailed) + " % " + str(yesFailed*100/totalYesNo))
    print("no passed " + str(noPassed) + " % " + str(noPassed*100/totalYesNo))
    print("no failed " + str(noFailed) + " % " + str(noFailed*100/totalYesNo))


main()

