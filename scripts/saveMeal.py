#Code to save Meal to a folder for a future reference
#Will save images and text instructions for the meal into a folder, named by the dish
#Example
#Folder Name: EggbaconToast
# -imagesOfSteps - EggbaconToast_step#.png
# -textOfSteps - EggbaconToast_steps.txt

#For this project, we will save txt files and image files in folders
#An expansion to this exercise is to integrate a SQL database
import os, glob, shutil
from PIL import Image


#Create new directory with path, where mealName is the name of the meal the user has made, example EggBaconToast
def makeNewDirectory(mealName):

    path_image = f'\\app\\savedMeals\\{mealName}\\imagesOfSteps'
    path_text = f'\\app\\savedMeals\\{mealName}\\textOfSteps'
    try:
        os.makedirs(path_image)
        os.makedirs(path_text)
    except OSError as error:
        print(error)


#images from generatedImages are set to be deleted once the app closes or the user decides to make a new recipe
#Therefore this is a more permanent way of saving the data
#The variable image, is in the format of "step#.jpg"
def saveImagesInDirectory(mealName, image):
    path = f'\\app\\savedMeals\\{mealName}'
    img_temp = Image.open(f'\\app\\generatedImages\\{image}')
    file_list = glob.glob(os.path.join('\\app\\generatedImages\\',f'{image}'))

    saveImageName = mealName + '_' + image

    #To save photos in the new directory
    img_temp.save(f'{path}\\imagesOfSteps\\{saveImageName}')

    #To remove photos from the temp directory
    for f in file_list:
        os.remove(f)



def saveTextInDirectory(mealName):

    text_NEW_path = f'C:\\Coding\\Github\\HackathonFeb16\\app\\savedMeals\\{mealName}\\textOfSteps\\{mealName}' + '_'+ 'steps.txt'
    text_TEMP_path = f'C:\\Coding\\Github\\HackathonFeb16\\app\\generatedText\\{mealName}' + '.txt'
    
    shutil.move(text_TEMP_path, text_NEW_path)






     








