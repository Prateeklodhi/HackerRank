# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
playerOne = {
    "age": 25,
    "username": "Assassinleon",
    "weapons": ["sniper"],
    "is_active": True,
    "clan": None
}

# 2 iterate and print all the keys in the above user.
for key in playerOne.keys():
    print(key)
# 3 Add a new weapon to your user
playerOne["weapons"].append("Pistol")
# 4 Add a new key to include 'is_banned'. Set it to false
playerOne.update({"is_banned": False})
print(playerOne)
# 5 Ban the user by setting the previous key to True
playerOne.update({"is_banned": True})
print(playerOne)
# 6 create a new user2 my copying the previous user and update the age value and username value.
playerTwo = playerOne.copy()
playerTwo.update({"age": 26})
playerTwo.update({"username": "Tanu(Mrs.Lodhi)"})
print(playerTwo)
