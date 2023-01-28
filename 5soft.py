#in this program the input ask us which programming language you want to learn

lang = input("What's the programming language you want to learn? ")


#in this program we can define the type of job with programming language

# we can write with  the switch- case.

# the language should be written near the case

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
        
    case "C#":
        print("You can become a Backend developer")
        
    case "HTML":
        print("You can become a Front-end developer")
        
    case "CSS":
        print ("You can become describer the presentation of a document written in HTML")
                
    case "Swift":
        print ("You can be a IOS developer")
        
    case "Java":
        print("You can become a mobile app developer")
        
    case "UX/IX":    
        print("you can become a web designer")
        
    case other:
        print("it doesnt matter for you, you can learn what you want")
