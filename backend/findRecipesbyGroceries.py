dictionaryRecipes = [   #Database for the main recipes
    {
        "name": "Oats Idli",
        "value": "Oats Idli",
        "ingredients": [
            "1 cup oats",
            "½ cup fine rava(sooji or cream of wheat)",
            "fine textured ½ cup Curd(yogurt), fresh or sour",
            "1 cup water or add as required",
            "1 teaspoon eno or ½ teaspoon baking soda",
            "⅓ to ½ cup grated carrot or 1 small to medium-sized carrot",
            "1 tablespoon chopped coriander leaves(cilantro)",
            "salt as required"
        ],
        "imagesource": "https://www.vegrecipesofindia.com/wp-content/uploads/2019/01/oats-idli-recipe-1-500x500.jpg",
        "description": "These easy oats idli are light, fluffy, cakes perfect for a quick breakfast or healthy on-the-go snack. Made with oats, curd (yogurt), semolina, herbs and spices, this instant oats idli recipe requires no fermentation and is quick to make.",
        "rating": "OUTSTANDING",
        "author": {
            "name": "Dassana Amit",
            "image": "https://secure.gravatar.com/avatar/1f1e0a18cf458d170463061bfd17da5c?s=48&d=mm&r=g"
        }
    },
    {
        "name": "Chicken Curry",
        "value": "Chicken Curry",
        "ingredients": [
        "2 lbs chicken, whole chicken cut into sections OR any bone-in chicken thigh or leg pieces (large thigh pieces should be cut in half)",
        "2 - 3 tbsp coconut oil",
        "½ onion yellow or red, diced or sliced.",
        "4 garlic cloves minced",
        "1 inch ginger minced",
        "6 - 7 curry leaves or 2 bay leaves",
        "2 ½ tbsp roasted Sri Lankan curry powder",
        "1 cinnamon stick or 1 small regular cinnamon stick",
        "½ tsp salt plus more to taste",
        "1 tsp cayenne pepper or chili powder (less if you like it less spicy)",
        "1 tbsp paprika not smoked or sweet paprika",
        "2 serrano peppers (or regular green chili) cut length-wise, with or without seeds",
        "3 roma tomatoes cut into cubes (or 2 medium-sized regular tomatoes)",
        "½ cup coconut milk",
        "½ cup water"
    ],
    "imagesource": "https://www.theflavorbender.com/wp-content/uploads/2018/02/Sri-Lankan-Chicken-Curry-The-Flavor-Bender-2-1-700x1049.jpg",
    "description": "This Sri Lankan chicken curry ticks all the boxes! It's a versatile recipe that you can adapt to your taste and still be absolutely delicious.",
    "rating": "OUTSTANDING",
    "author": {
        "name": "Dini K.",
        "image": "https://www.theflavorbender.com/about-dini/"
    }
    },
    {
        "name": "Mutton Curry",
        "value": "Mutton Curry",
        "ingredients": [
        "4 tablespoons vegetable oil (or canola oil or sunflower cooking oil)",
        "2 large onions, sliced thin",
        "2 large tomatoes, diced",
        "2 tablespoons garlic paste",
        "1 tablespoon ginger paste",
        "2 teaspoons garam masala powder",
        "2 teaspoons coriander powder",
        "1 teaspoon cumin powder",
        "1/2 teaspoon turmeric powder",
        "1/2 teaspoon red chili powder",
        "2 pounds goat (or sheep leg), cut into bite-sized chunks",
        "Kosher salt, to taste",
        "Chopped fresh coriander (cilantro), garnish"
        ],
        "imagesource": "https://www.thespruceeats.com/thmb/Ff1BC_PpJdxkij66NamL7Bo5Row=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/goat-mutton-curry-1957594-hero-01-afaf638173cd47d595c7ad99a018cf01.jpg",
        "description": "Spicy mutton kulambu recipe made by cooking mutton in an onion, tomato, and coconut masala. This goes well with paratha, idli, and dosa.",
        "rating": "OUTSTANDING",
        "author": {
            "name": "Petrina Verma Sarkar",
            "image": "N/A"
        }
    },
    

    
    ]


def findRecipesbyGroceries(groceries):
    
    matchingIngredients=[]
    for ingredient in dictionaryRecipes:
        counter=0
        for grocery in groceries:
            for groceryFinder in ingredient["ingredients"]:
                if grocery in groceryFinder:
                    counter+=1       
        
        sizeOfIngredientsList=len(ingredient["ingredients"]) #obtaining length of the ingredients list
        matchingPercentage=(counter/(sizeOfIngredientsList))*100 # calculating percentage value
        ingredient["Matching Percentage"]=matchingPercentage #adding percentag value to dictionary key
        matchingIngredients.append({
            "name": ingredient["name"],
            "Match percentage": round(matchingPercentage,2)
        })

    
    #sortedRecipes=sorted(dictionaryRecipes,key=lambda d: d["Matching Percentage"], reverse=True) #sort recipes from highest match to lowest match

    sortedRecipes=sorted(matchingIngredients,key=lambda d: d["Match percentage"], reverse=True)
       
    return sortedRecipes


if __name__ == "__main__":
    print(findRecipesbyGroceries(["tomato"]))

# "oat","water","rava","yogurt","baking soda","coriander","carrot","salt"