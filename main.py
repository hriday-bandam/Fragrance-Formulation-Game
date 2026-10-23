#importing all of the scoring and details of each ingredient 
from ingredientdict import ingredientdictionary
from SUMMERdict import SUMMERindex
from WINTERdict	import WINTERindex
from DATEdict import DATEindex

#displays some background information of each fragrance note
def ingredients():
    for i in ingredientdictionary:
        print(i)
    
    
#asks the player what type of fragrance they are making    
def decision():
    argd=input("""Test your knowledge on fragrance making.
      Enter the kind of fragrance you are making (Summer, Winter, Date) """)
    return argd


def loop(w):
    '''takes the perfume score as a parameter and tells if the player passed or failed, 
exits the game or loops it again if the player wants to'''

    if w>=7:
        print("congratulations! You have made a good fragrance!")
    else:
        print("You failed at making a good fragrance, try to do better next time.")
    print("Your score evaluation:",w)
    p=input("Make Another?(y,n) ")
    if p=="n":
        exit()       
        

#lets the user view the ingredients list, then lets the user create a summer fragrance and scores it
def rulesetSUMMER():
    x=input("would you like to see the list of ingredients that can be used in the fragrance?(y,n)")
    if x=="y":
        ingredients()
    valu=0
    ing=input("""Enter all of the ingredients that you would like to use in the fragrance
    (make sure to use only what is displayed in the ingredient catalogue, type each ingredient exactly, 
    and separate each ingredient with a comma with no spaces): """).split(",")
    ing=set(ing)
    for i in range(0,len(ing)):
        if ing[i] in SUMMERindex:
           valu+=SUMMERindex[ing[i]]
    vunc=round((valu/len(ing)),3)
    return vunc


#lets the user view the ingredients list, then lets the user create a winter fragrance and scores it
def rulesetWINTER():
    x=input("would you like to see the list of ingredients that can be used in the fragrance?(y,n)")
    if x=="y":
        ingredients()
    valu=0
    ing=input("""Enter all of the ingredients that you would like to use in the fragrance
    (make sure to use only what is displayed in the ingredient catalogue, type each ingredient exactly, and separate each ingredient with a comma): """).split(",")
    for i in range(0,len(ing)):
        if ing[i] in WINTERindex:
           valu=valu+WINTERindex[ing[i]]
    vunc=round((valu/len(ing)),3)
    return vunc


#lets the user view the ingredients list, then lets the user create a date night fragrance and scores it
def rulesetDATE():
    x=input("would you like to see the list of ingredients that can be used in the fragrance?(y,n)")
    if x=="y":
        ingredients()
    valu=0
    ing=input("""Enter all of the ingredients that you would like to use in the fragrance
    (make sure to use only what is displayed in the ingredient catalogue, type each ingredient exactly, and separate each ingredient with a comma): """).split(",")
    for i in range(0,len(ing)):
        if ing[i] in DATEindex:
           valu=valu+DATEindex[ing[i]]
    vunc=round((valu/len(ing)),3)
    return vunc


#decides which ruleset to apply based on what kind of fragrance the player decides to make
def main(c="Summer"):
    if c=="Summer":
        loop(w=rulesetSUMMER())
        
        
    elif c=="Winter":
        w=rulesetWINTER()
        loop(w)
    elif c=="Date":
        w=rulesetDATE()
        loop(w)

while True:
    try:
        s=decision()
        main(s)
    except Exception as e:
        print("Error Occurred, please try again. Error: ",e)