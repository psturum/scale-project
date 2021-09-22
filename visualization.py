from PIL import Image, ImageFont, ImageDraw

# import cv2 library
import cv2
  
# read the images
high_carbon = Image.open("pictures/visualization_pics/High_Carbon_viz_01.png")
medium_carbon = Image.open("pictures/visualization_pics/Medium_Carbon_viz_01.png")
low_carbon = Image.open("pictures/visualization_pics/Low_Carbon_viz_01.png")
white_pic = Image.open("pictures/visualization_pics/white.png")

# Transform emission into visualization 
def load_emission_pic(emission):
    if (emission > 9000/3*2):
        high_carbon.save("pictures/temporary_pics/emission.png")
    elif (emission > 9000/3):
        medium_carbon.save("pictures/temporary_pics/emission.png")
    else:
        low_carbon.save("pictures/temporary_pics/emission.png")

# Transform leaderboard into visualization
def load_leaderboard_pic(leaderboard_pic, leaderboard, name):
    # Call draw Method to add 2D graphics in an image
    pic = Image.open(leaderboard_pic)
    drawing = ImageDraw.Draw(pic)
    font = ImageFont.truetype("font/micro_se.ttf", 150)
    font1 = ImageFont.truetype("font/micro_se.ttf", 140)

    # Add Text to leaderboard
    if(leaderboard[0][1]!="NA"):
        # First place
        drawing.text((450, 600), leaderboard[0][1], fill=(255, 255, 255), font = font)
        drawing.text((1500, 700), str(int(leaderboard[0][0])), fill=(255, 255, 255), font = font1)
    if(leaderboard[1][1]!="NA"):
        # Second place
        drawing.text((450, 1100), leaderboard[1][1], fill=(255, 255, 255), font = font)
        drawing.text((1500, 1200), str(int(leaderboard[1][0])), fill=(255, 255, 255), font = font1)
    if(leaderboard[2][1]!="NA"):
        # Third place
        drawing.text((450, 1600), leaderboard[2][1], fill=(255, 255, 255), font = font)
        drawing.text((1500, 1700), str(int(leaderboard[2][0])), fill=(255, 255, 255), font = font1)

    pic.save(name, Path = "pictures/temporary_pics")

def load_submission_pic(username, score):
    img = white_pic
    img = img.resize((1000, 750))
    drawing = ImageDraw.Draw(img)
    font = ImageFont.truetype("font/micro_se.ttf", 100)
    text_score = str(score)
    drawing.text((100, 100), "Holdnavn: ", fill=(0, 0, 0), font = font)
    drawing.text((100, 200), username, fill=(0, 0, 0), font = font)
    drawing.text((100, 450), "CO2 Udledning: ", fill=(0, 0, 0), font = font)
    drawing.text((100, 550), text_score + " gCO2e", fill=(0, 0, 0), font = font)
    img.save("pictures/temporary_pics/team_score.png")


# Helper function to combine pictures vertically
def combine_pics(pic1, pic2, i):
    img1 = cv2.imread(pic1)
    img2 = cv2.imread(pic2)
    resized = cv2.resize(img1, (500, 750))
    resized1 = cv2.resize(img2, (500, 750))
    im_v = cv2.vconcat([resized, resized1])
  
    # Write the output image
    cv2.imwrite("pictures/temporary_pics/combined" + str(i) + ".png", im_v)


# Helper function to combine pictures horrtizontally
def combine_pics1(pic1, pic2):
    img1 = cv2.imread(pic1)
    img2 = cv2.imread(pic2)
    resized = cv2.resize(img1, (1000, 1500))
    resized1 = cv2.resize(img2, (1000, 1500))
    im_v = cv2.hconcat([resized, resized1])
  
    # show the output image
    cv2.imwrite("pictures/temporary_pics/combined2.png", im_v)



