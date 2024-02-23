# The following code will do the following
# At this point, the user has chosen what they want to make from what they have, when the user clicks "show me the steps! shown in the "recipeSteps.html", two API calls will occur. 1. Chatgpt 3.5 (openai_chatgpt.py) will be called to create a 5 step process to complete the chosen dish. Once completed, these steps will be sent to Dallie 2 (openai_dallie.py) to show a visual of each step being made
#Once complete, the user will see the steps and be able to read what to do!
import scripts.openai_chatgpt as chatgpt
import scripts.openai_dallie as dall


#Function will do two API calls
def generateDish(dishName):
    path=[]
    filepath = "\\app\\generatedImages"
    prompt = f"The user has decided what they would like to make based off of ingredients that they have The dish they have chosen is {dishName}. As previously done before, I want a 5 step process in making the users choice of {dishName}. Please separate the steps in this manner (for example) '1. Instructional Step of cooking' and the continue the steps in numerical fashion. Separate each step by a \n. This formatting is a strict request"

    response = chatgpt.call_OpenAI(prompt)

    #Parses out my data
    dishStepInstructions = response.split('\n')
    #Clean up response
    dishStepInstructions = [element for element in dishStepInstructions if len(element) >5]



    #To save text in the temp folder
    dishName_temp = dishName.replace(" ","")
    textPath = "\\app\\generatedText\\" +dishName_temp + ".txt"
    with open(textPath, 'w') as textFile:
        textFile.write(response)




    print(dishStepInstructions)

    #To save images
    for i, cookStep in enumerate( dishStepInstructions,start=1):

        if (i >= 2):
            x = dall.generateImage(cookStep,cookStep[i-1], f"step{i}.jpg", filepath)
        else:
            x = dall.generateImage(cookStep,'',f"step{i}.jpg", filepath)

        path.append(f'step{i}.jpg')
    

    return dishStepInstructions, path