users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
Jonathan_twitter=users["Jonathan"]["twitter"] #note: is variables and index case sensitive, if so, how to make it not to?
print(Jonathan_twitter)
# 2. Get Erik's hometown
Erik_hometown=users["Erik"]["home_town"]
print(Erik_hometown)
# 3. Get the list of Erik's lottery numbers
Erik_lottery=users["Erik"]["lottery_numbers"]
print(Erik_lottery)
# 4. Get the species of Avril's pet Monty
Avril_pet_species=users["Avril"]["pets"][0]['species']
print(Avril_pet_species)
# 5. Get the smallest of Erik's lottery numbers
smallest_num=Erik_lottery[0]
for num in Erik_lottery:
  if smallest_num>num:
    smallest_num=num
    print(smallest_num)

# 6. Return an list of Avril's lottery numbers that are even
Avril_lottery=users["Avril"]["lottery_numbers"]
even_lottery=[]
for num in Avril_lottery:
  if num%2==0:
   even_lottery.append(num)

print(even_lottery)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

Erik_lottery.append(7)
print(Erik_lottery)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"]="Edinburgh"
print(users["Erik"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append("'name': 'fluffy', 'species': 'dog'")
print(users['Erik']['pets'])

# 10. Add another person to the users dictionary

users.update({
 "Jooey": {
    "twitter": "Jooey123",
    "lottery_numbers": [11, 22, 33, 44, 99, 55],
    "home_town": "Iceland",
    "pets": [
      {
        "name": "archie",
        "species": "bird"
      }
    ]
  }
})
print(users)
