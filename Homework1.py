Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Starts with a blank list. 
names = []

new_name = ''

# Uses a while loop.
while new_name != 'done':
    # Asks the user to enter a name or type 'done' to stop.
    new_name = input("Please enter a name or type 'done' to stop:")
    # Does not append 'done' to the list.
    if new_name != 'done':
        #Appends each name to the list.
        names.append(new_name)
    #Asks the user to select one of three methods to print the list (lower, CAPITAL, Title).
    if new_name.lower():
        print(names)
    if new_name.upper():
        print(names)
    if new_name.title():
        print(names)
        
for name in names:
    print(name.title())
    
# Prints the list based on the user's preference.
print(names)

#Clears the list.
names.clear()