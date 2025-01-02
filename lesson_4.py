#this lesson is all about lists, defining lists, printing responses

cars = ["hyundai", "audi", "tesla", "volkswagen", "alfa romeo"]
for car in cars:
    
    print(f"{car.title()}: do you like this car brand?") 
    print(f"same here, i love {car.title()}, theyre my fave car\n")



#next section will be surrounding slicing lists

players = ["charlie", "ryan", "bob", "geoff", "dylan"]
print(players[0:3]) # what this does is return the variables inside the string "players" at positions 0, to 3.


# this next section encorportates a for loop to loop through the subset of elements within the list. 

players = ["charlie", "ryan", "bob", "geoff", "dylan"]
print ("here are the first three players on my team")
for player in players[:3]: # this for loop lets you choose the values in the players field up to the third individual through the use of [:3]
    print(player.title())

# this next section shall be about copying lists. this is to ensure the intactness of the original list, whilst also being able to add or change values inside that without affecting the integrity. 

my_foods = ["pizza", "chicken", "ramen", "steak"]
friends_food =my_foods[:]

my_foods.append("kaarage")
friends_food.append("tomatoes")

print ("my favourite foods are:")
print (my_foods)

print("\nmy friends favourite foods are:")
print(friends_food)




