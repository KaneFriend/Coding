# this lesson shall be surrounding strings. 

name = "kane friend"
print (name.title())

# to change the title case you can perform the following 

name = "kane friend"
print (name.upper()) # this returns the name variable in all uppercase. 
print (name.lower()) # this returns the name variable in lowercase. 

# using variables in strings. 
first_name = "kane"
last_name = "friend"
full_name = f"{first_name} {last_name}" # the "f" stands for an f-string, the "f" is for format, because python formats the string by replacing the name of any variable in braces with the value. 
print (full_name)


#f-strings are versatile. such as below. 

first_name = "alan"
last_name = "friend"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


#adding whitespaces to strings with tabs or newlines
# to add a tab you can use the character combo of \t:
print ("python")
print("\tPython") # this here tabs it. 

#to add a new line in a string, you can use the character combo of \n:

print ("Languages:\nPython\nPowershell\nC\nbash") 

# you can combine these character combinations like the following:

print ("Languages:\n\tPython\n\tPowershell\n\tC\n\tbash")


# stripping whitespace
    # 
