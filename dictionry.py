name=str(input("Enter the student name:"))

dic={"sam":23,"om":56,"alice":56}
if name in dic:
    print(f"{name} marks is:{dic[name]}") 
else:
    print("Student Not found")