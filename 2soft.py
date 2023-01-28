score = input("Enter Score: ")

try:
    sc=float(score)
    if sc>1:
        print("Please enter a score between 0.0 and 1.0")
    elif sc<0:
        print("Please enter a score between 0.0 and 1.0")
    elif sc>=0.9:
        print ("A")
    elif sc>=0.8:
        print ("B")
    elif sc>=0.7:
        print ("C")
    elif sc>=0.6:
        print ("D")
    else:
        print ("F")
        
except:
    print ("Invalid Entry")
    print ("Please enter a score between  0.0 and 1.0")