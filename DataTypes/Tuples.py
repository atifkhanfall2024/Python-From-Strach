# Tuples () , [] , {} 

Animal_names = ("Dog" , "lion" , "Donkey" , "Monkey")

(Anim_1 , Anim_2 , Anim_3 , Anim_4) = Animal_names

print(f"Animals names is  {Anim_1} , {Anim_2} , {Anim_3} , {Anim_4}")


# we can also swap its valules by simple technique 

No_of_students ,No_of_Quizzes = 10 ,5


print(f"Numbers of students before swapping is : {No_of_students}  , and number of Quizzes is : {No_of_Quizzes}")

No_of_students , No_of_Quizzes = No_of_Quizzes , No_of_students


print(f"Numbers of students After swapping is : {No_of_students}  , and number of Quizzes is : {No_of_Quizzes}")


## MemberShip Testing 

print(f"Check if the thing is avalible or not ? {"Dog" in Animal_names}")

