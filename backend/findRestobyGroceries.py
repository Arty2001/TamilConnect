import json
from urllib.request import urlopen
import geopy.distance



url='http://ipinfo.io/json' # obtaining user's location
response=urlopen(url)
data=json.load(response) # converting location to python data 



coordinatesString=data["loc"] # collecting the latitude and longitude of user
tempUserLatitude=coordinatesString[0:7]
tempUserLongitude=coordinatesString[8:16]

    

userLatitude = float(tempUserLatitude) # collecting the latitude and longitude of user
userLongitude = float(tempUserLongitude) 

      
dictionaryStore = { #database for all items contained in store

    "Marche West Island": ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],


    "Jaffna Fruits":     ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Murugan":    ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche M.S":        ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "AMR Fruiterie":     ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Ganesh":     ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Victoria":  ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],


    "Marche Thurgaa":   ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Indien-Punjabi":["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Epicerie Rama-Kishan": ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Lingam":        ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],
  

    "Marche Shanti":        ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],
    

    "Fruits Haby":          ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"], 

    "Aliments Exotiques":["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],
    
    "Marche Jeeveni":   ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Tharsini":  ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Anchovie", "Barracuda", "Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Magaluxmi": ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],


    "Fruiterie Maruti":["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Alexandria":["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Blue Coast":       ["Anchovie", "Barracuda", "Barramundi", "Red snapper","Sprats","Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab"],
    
    "OCN Import":       ["Anchovie", "Barracuda", "Red snapper","Sprats","Barramundi", "Giant Sea Perch", "EmperorMula", "LeatherSkin Fish", "Shark", "Pipefish", "King Fish", "Neela Thuduppu", "Cat Fish", "Calamar", "Tin Fish", "Shrimp", "Crab"],

    "Marche Emmy":      ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Solaire":   ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Mayls":     ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Thanigai":  ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],


     "Marche Bhane":     ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",],

    "Marche Sava":      ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Amma":      ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],
    
    "Marche Nithusika": ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "T.M.S Fruiterie":  ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"],

    "Marche Thuvaarakai":   ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa",
                           "Chicken", "Beef", "Mutton", "Pork", "Turkey", "Lamb",
                           "Bengal Gram", "Red Gram", "Black Gram", "Black Gram Split", "Fenugreek", "Red Chili", "Red Chili Powder", "Asafoetida", "Cloves", "Coriander Seeds", "Cumin", "Mustard", "Pepper", "Tamarind", "Jaggery", "Sesame", "Turmeric", "Almond", "Cashewnut", "Raisin", "Cardamom", "Fennel", "Carom Seeds", "Vermicelli", "Wheat", "Sugar", "Salt", "Flour", "Ghee", "Ginger", "Cinnamon", "Chickpeas", "Coconut Oil", "Grated Coconut", "Sesame Oil", "Olive Oil", "Gingelly Oil", "Vegetable Oil", "Mustard Oil", "Horse Gram", "Ragi", "Butter", "Buttermilk"],

    "Marche Vishnu":    ["Artichoke", "Asparagus", "Eggplant", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cucumbers", "Celery", "Garlic", "Ginger", "Kale", "Corn", "Chinese Cabbage", "Green Cabbage", "Savoy Cabbage", "Carrots", "Jicama", "Kohlrabi", "Leeks", "Lettuce", "Mushrooms", "Okra", "Onions", "Green Onions", "Parsnips", "Peas", "Snag Sugar Peas", "Snow Peas", "Peppers", "Potatoes", "Pumpkin", "Radish", "Rhubarb", "Cauliflower", "Shallots", "Spinach", "Squash", "Tomatoes", "Turnips", "Zucchini", "Drumstick", "Suran", "Bell Peppers", "Curry Leaves",
                           "Bananas", "Apple", "Orange", "Grapes", "Melons", "Strawberries", "Avocados", "Mandarins", "Peaches", "Pineapple", "Raspberries", "Cherries", "Blackberries", "Pears", "Lemons", "Lime", "Mango", "Kiwi", "Grapefruit", "Coconut",
                           "White Rice", "Jasmine Rice", "Basmati Rice", "Roti", "Brown Rice", "Short Grain Rice", "Rice Flour", "Noodles", "Idly Rice", "Soogi", "ATTA Flour", "Steamed Flour", "Roasted Rice Flour", "Matta Rice", "Parboiled Rice", "Red Raw Rice", "Couscous", "Quinoa"]

}

dictionaryAddressStore = [ #database for all store locations
    {
        "name": "Marche West Island",
        "latitude": 45.50417,
        "longitude": -73.77868
    },
    {
        "name": "Jaffna Fruits",
        "latitude": 45.50646,
        "longitude": -73.82878
    },
    {
        "name": "Marche M.S",
        "latitude": 45.507530,
        "longitude": -73.820020
    },
    {
        "name": "Marche Murugan",
        "latitude": 45.561340,
        "longitude": -73.603270
    },
    {
        "name": "AMR Fruiterie",
        "latitude": 45.515110,
        "longitude": -73.684520
    },
    {
        "name": "Marche Ganesh",
        "latitude": 45.494880,
        "longitude": -73.574840
    },
    {
        "name": "Marche Victoria",
        "latitude": 45.494920,
        "longitude": -73.639400
    },
    {
        "name": "Marche Thurgaa",
        "latitude": 45.529157,
        "longitude": -73.622692
    },
    {
        "name": "Marche Indien-Punjabi",
        "latitude": 45.434187,
        "longitude": -73.629329
    },
    {
        "name": "Epicerie Rama-Kishan",
        "latitude": 45.5250805,
        "longitude": -73.6278473
    },
    {
        "name": "Marche Lingam",
        "latitude": 45.5472532,
        "longitude": -73.6599683
    },
    {
        "name": "Marche Shanti",
        "latitude": 45.530702,
        "longitude": -73.643497
    },
    {
        "name": "Fruits Haby",
        "latitude": 45.4937866,
        "longitude": -73.6358417
    },
    {
        "name": "Aliments Exotiques",
        "latitude": 45.4965511,
        "longitude": -73.6418431
    },
    {
        "name": "Marche Jeeveni",
        "latitude": 45.5298436,
        "longitude":-73.6290277
    },
    {
        "name": "Marche Tharsini",
        "latitude": 45.491889,
        "longitude":-73.632661
    },
    {
        "name": "Marche Magaluxmi",
        "latitude": 45.5254788,
        "longitude":-73.62757
    },
    {
        "name": "Fruiterie Maruti",
        "latitude": 45.458631,
        "longitude":-73.661212
    },
    {
        "name": "Marche Alexandia",
        "latitude": 45.5027439,
        "longitude":-73.6353009
    },
    {
        "name": "Marche Emmy",
        "latitude": 45.4956798,
        "longitude":-73.6399742
    },
    {
        "name": "Marche Solaire",
        "latitude": 45.5319,
        "longitude":-73.642369
    },
    {
        "name": "Marche Mayls",
        "latitude": 45.546881,
        "longitude":-73.660262
    },
    {
        "name": "Marche Thanigai",
        "latitude": 45.534217,
        "longitude":-73.6183769
    },
    {
        "name": "Marche Bhane",
        "latitude": 45.530252,
        "longitude":-73.636646
    },
    {
        "name": "Marche Sava",
        "latitude": 45.50279,
        "longitude":-73.636052
    },
    {
        "name": "Marche Amma",
        "latitude": 45.567578,
        "longitude":-73.618867
    },
    {
        "name": "Marche Nithusika",
        "latitude": 45.566688,
        "longitude":-73.699487
    },
    {
        "name": "T.M.S Fruiterie",
        "latitude": 45.5195948,
        "longitude":-73.6975867
    },
    {
        "name": "Marche Thuvaarakai",
        "latitude": 45.5650491,
        "longitude":-73.5885094
    },
    {
        "name": "Marche Vishnu",
        "latitude": 45.546881,
        "longitude": -73.660262
    },
    {
        "name": "Blue Coast",
        "latitude": 45.5874378,
        "longitude": -73.6365683
    },
    {
        "name": "OCN Import",
        "latitude": 45.5326215,
        "longitude": -73.6204589
    },

]

def globalFunction(groceries):

    def findRestobyGroceries(groceries): #Finds if grocery is available in store than adds information of store to a list
        stores = []
        for resto in dictionaryStore:
            foundAllGroceries=True;
            for grocery in groceries:
                if grocery not in dictionaryStore[resto]:
                    foundAllGroceries=False
                    break
            if foundAllGroceries:
                for address in dictionaryAddressStore:
                    if address["name"] == resto:
                        stores.append({
                        "name": resto,
                        "latitude": address["latitude"],
                        "longitude": address["longitude"]
                    })
                        break

                    
        return stores # returning a list of dictionary items
    
    matched_stores = findRestobyGroceries(groceries)

    
    def calculateDistance(matched_stores, user_latitude, user_longitude): # Calculate distance of all the matched stores
        user_coordinates = (user_latitude, user_longitude)
        updatedStores=[]

        for store in matched_stores:
            store_latitude = store["latitude"]
            store_longitude = store["longitude"]
            store_coordinates = (store_latitude, store_longitude)

            distance = geopy.distance.geodesic(user_coordinates, store_coordinates).km #Calculate distance between user and store locations
            store["distance"]=distance #adding distance as a key in dictionary

            updatedStores.append(store)


        return updatedStores

    
    updatedStores = calculateDistance(matched_stores, userLatitude, userLongitude)

    def findClosestStores(updatedStores): # determine the closest store to the user 
        amountOfStores=3
        sortedStores=[]
        closestStores=[]
        
        sortedStores=sorted(updatedStores,key=lambda d: d["distance"]) #sorting distance in ascending order

        
        
        if len(sortedStores)>amountOfStores: # if more than 3 stores,display the first 3,else display all
            closestStores=sortedStores[:3]
    
        else:
            closestStores=sortedStores.copy()      
            

        return closestStores


    closestStores=findClosestStores(updatedStores)
    print(closestStores)



if __name__=="__main__":
    print(globalFunction(["Pineapple", "Chicken", "Turmeric"]))#itslikecallingtheAPI