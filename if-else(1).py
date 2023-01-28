gpa =int(input("enter your gpa degree"))
ielts =float(input("enter your IELTS (english) score"))

# we can find how we can get scholarship with our scores

#it depends us our all scores

if gpa==100 and ielts>=8.5:
     print (" you can get exactly Full scholarship for everything in all countires")
elif gpa>=95 and ielts>8:
     print ("you can get scholarship possibly")
elif gpa>=90 and ielts>=7.5:
     print ("you can get 100 % scholarships in Canada or USA")
elif gpa>=87 and ielts>=7:
     print (" you can get scholarship in Europe and Asia")
elif gpa>=80 and ielts>=6.5:
     print ( "you cane get 80 % scholarship in Europe")
elif gpa>=75 and ielts>=6:
     print (" you can get 40% or 50% scholarship in Europe")
elif gpa>=70 and ielts>=5.5:
     print (" you can get scholarship difficulty")

else:
     print("you can't go abroad, you have to be more hardworking")
