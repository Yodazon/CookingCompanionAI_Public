import sys
sys.path.insert(1, ' ')
from flask import Flask, render_template, request, send_from_directory, session
from markupsafe import Markup
import urllib.parse

import scripts.openai_chatgpt as gpt
import scripts.generateStepsForDishMaking as dishMaker
import scripts.saveMeal as save
app = Flask(__name__, template_folder= 'templates', static_folder='static')
app.secret_key = 'd23/[#3'

PYTHONUNBUFFERED=0





#brings together all the inputs and passes it into chatgpt
@app.route("/recipeGen", methods=['POST'])
def generateRecipe():
#Code to compile items into a single element

    # Retrieve form data
    elements = [request.form.get(f'input{i}') for i in range(len(request.form))]

    # Join elements into a string for OpenAI request
    joined_elements = ', '.join(elements)


    ##Code to submit API request to chat gpt to generate recipes
    #response, dishes = gpt.submit_recipe(joined_elements)
    response,dishes = gpt.submit_recipe(joined_elements)


    return render_template("recipeGen.html", suggestions = response, dishName = dishes)

#Code to bring us to the next page recicpeSteps.html
@app.route('/recipeSteps', methods=['POST'])
def generateRecipeSteps():
        chosenDish = request.form.get('selectedDish')
        
        session['mealName'] = chosenDish

        return render_template('recipeSteps.html', dish=session.get('mealName'))


#Code to generate images and steps of the chosen meal by the user
@app.route('/generateImagesAndSteps', methods=['POST'])
def generateImagesAndSteps():
        
        print("generating recipe and steps")
        #dishName = request.form.get('dish')

        dishText, dishImage = dishMaker.generateDish(session.get('mealName'))
        session['dishImage'] = dishImage

        zipped_data = zip(dishImage, dishText)


        return render_template('recipeSteps.html', dish=session.get('mealName'), dishZipped = zipped_data)

@app.route('/generatedImages/<filename>')
def generatedImages(filename):
       return send_from_directory('generatedImages', filename)



@app.route('/saveCompletion',methods =['POST'])
def saveCompletion():

        mealName = (session.get('mealName')).replace(" ", "")
        mealImage = session.get('dishImage')

        save.makeNewDirectory(mealName)
        save.saveTextInDirectory(mealName)
        for image in mealImage:
                save.saveImagesInDirectory(mealName,image)

        
        return render_template('saveCompletion.html')







#Render different HTML Files
#Main Screen Render
@app.route('/')
def index():
        return render_template('index.html')

#Render screen for recipe chooser
@app.route('/recipeGen')
def recipeGen():
        return render_template('recipeGen.html')


#Render screen to show step by step
@app.route('/recipeSteps')
def recipeSteps():
        return render_template('recipeSteps.html')


@app.template_filter('url_encode')
def url_encode_filter(s):
    return Markup(urllib.parse.quote(s))







if __name__ == '__main__':
        app.run(debug=True)