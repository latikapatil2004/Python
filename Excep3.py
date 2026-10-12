'''Q3. List Index Error
Create a list of five numbers. Ask the user to enter an index and display the corresponding element. Handle an invalid index.
'''



list=[1,2,3,4,5]
try:
    index=int(input("Enter index"))
    for i in range(len(list)):
        if index==i:
            print(list[i]);
            
    if(index<0 and index>len(list)):
        print("index not match")
except Exception as e :
    print("index not match",e)