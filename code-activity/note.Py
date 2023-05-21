
# Get student stage & test marks
stage_mark = int(input())
test_mark = int(input())




if (((stage_mark + test_mark ) // 2) < 40) :
  print("Student cannot pass exam.")
  print("Student final mark : F")
else :
    exam=int(input())
    mark=((stage_mark*0.25)+(test_mark*0.25))+(0.5*exam)
    print(mark)
    if (mark <= 100 and mark >= 80):
       print("Student final mark : A")
       #70 <= mark < 80
    elif  (mark < 80 and mark >= 70):
        print("Student final mark : B")

       #60 <= mark < 70
    elif  (mark < 70 and mark >= 60):
        print("Student final mark : C")

       #50 <= mark < 60
    elif  (mark < 60 and mark >= 50):
        print("Student final mark : D")

       #mark < 50
    elif  (mark < 50 ):
        print("Student final mark : E")

       



      


    