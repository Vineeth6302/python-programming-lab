def print_list(elements):
    for i in range(limit):
        print (elements)
        
        
        
        
elements=[]
limit=int(input("Enter the length of the list"))
for i in range(limit):
    temp=int(input(f"Enter the number{i+1}:"))
    elements.append(temp)
print_list(elements)
