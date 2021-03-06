import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


name = {
    "mood":["happy","sad","angry","excited"],
    "animal":["dog","bird","zebra","cat"]
}





def ask_flavor():
    """ask flavor and collect it"""
    preferences={}
    for flavor,question in questions.items():
        myinput=input(question+' (y/n)')
        preferences[flavor]=myinput.lower() in ['y']
        print("  ")
        #print(preferences)
    return preferences
        
    

def total_flavor(preferences):
    """choose ingredient for flavor"""
    drinks=[]
    for flavor,prefer in preferences.items():
        if prefer:
            drinks.append(random.choice(ingredients[flavor]))
    return drinks


def drink_name():
    """drink_name"""
   
    print("Your drink name is {0}{1}".format(random.choice(name['mood']),random.choice(name['animal'])))    

            
    
def main():
    preferences = ask_flavor()
    drinks = total_flavor(preferences)
    #print(preferences)
    #print(drinks)
    for ingredient in drinks:
        print("A {}".format(ingredient))
    drink_name()
    print("  ")
    another_drink=input("Would you like one more drink?")
    if another_drink.lower()=='y':
        a=1
        while a>0:
            main()
        

if __name__ == "__main__":
    main()
    
    
    
