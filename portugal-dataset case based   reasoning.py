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
    d34 = [] # Probability result
    d35 = [] # Predicted grade
    totaldifferences = 0 #all the differences right or wrong 
    maximumcorrect = 0
    correctdifferences = 0 #only the differences amongst the correct answers
    

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
        
    print("no missing data")

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
                    d34.append(0.0) # blank probability score
                    d35.append(0.0) # blank predicted final score

                wordcount += 1
                
                newword = ""
            textcount += 1

    comparisonstudent = 624
    perfectmatches = 0 #how many perfect matchers are there
    list_of_perfectmatches = [] #student index numbers that have a perfect match 
    list_of_nextbest = [] #student index numbers of next best
    nextbestscore = [] #next best scores
    bestmatchscore = 0 #current best match score
    maximum_matches = 11 #maximum number of matches
    studentmatches = 0 #how many number of matches a particular student has

    
    print("Total " + str(totalStudents))
    
    for c in range(600):
        studentmatches = 0
        if d14[c] == d14[comparisonstudent]: #study hours
            studentmatches += 1
        if d15[c] == d15[comparisonstudent]: #failures
            studentmatches += 1
        if d16[c] == d16[comparisonstudent]: #school support
            studentmatches += 1
        if d18[c] == d18[comparisonstudent]: #private tutor
            studentmatches += 1
        if d21[c] == d21[comparisonstudent]: #desire for higher education
            studentmatches += 1
        if d22[c] == d22[comparisonstudent]: #internet at home
            studentmatches += 1
        if d27[c] == d27[comparisonstudent]: #weekday alcohol consumption
            studentmatches += 1
        if d28[c] == d28[comparisonstudent]: #weekend alcohol consumption 
            studentmatches += 1
        if d7[c] == d7[comparisonstudent]: #mother's education  
            studentmatches += 1
        if d8[c] == d8[comparisonstudent]: #father's education  
            studentmatches += 1
        if d17[c] == d17[comparisonstudent]: #home support  
            studentmatches += 1
            
        if maximum_matches == studentmatches:
            perfectmatches += 1
            list_of_perfectmatches.append(c)
            bestmatchscore = maximum_matches
        elif bestmatchscore < studentmatches: #student matches is a temporary variable for the number of matches for one student 
            list_of_nextbest.append(c)
            nextbestscore.append(studentmatches)
            bestmatchscore = studentmatches



    #print("perfect matches" + str(perfectmatches))
    #print(" the students that match")
    #print(list_of_perfectmatches)
    print("next best matches")
    print(list_of_nextbest)
    print(nextbestscore)

    averagescore = 0 # initialising the total number of scores divided by the number of students to zero 
    lowestscore = 20
    highestscore = 0
    totalscores = 0

    for n in range(perfectmatches): # number of  students that have perfect matches
        totalscores += d33[list_of_perfectmatches[n]]
        if d33[list_of_perfectmatches[n]] < lowestscore: # students  index numbers that have a perfect match of the final score less than the lowest score 
            lowestscore = d33[list_of_perfectmatches[n]]
        if d33[list_of_perfectmatches[n]] > highestscore:
            highestscore = d33[list_of_perfectmatches[n]]
    print("highest score is " + str(highestscore))
    print("lowest score is " + str(lowestscore))
    print("average score is " + str(totalscores/perfectmatches))
    print("students actual final score is" + str(d33[comparisonstudent]))


    if perfectmatches == 0: # there are no perfect matches  
        l = len(list_of_nextbest)-1
        print ("next best matches = " + str(nextbestscore[l]) + "Actual grade = " + str(d33[list_of_nextbest[l]]))
    
    
        
            
        
                  
            

        
                  
            

        
                  
            

        
                  
            

        
                  
            

        
                  
            

        
                  
            

        
                  
            
main()

