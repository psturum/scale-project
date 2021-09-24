from PIL import Image, ImageFont, ImageDraw
import cv2
  
# read the images
high_carbon = Image.open("pictures/visualization_pics/High_Carbon_viz_01.png")
medium_carbon = Image.open("pictures/visualization_pics/Medium_Carbon_viz_01.png")
low_carbon = Image.open("pictures/visualization_pics/Low_Carbon_viz_01.png")
white_pic = Image.open("pictures/visualization_pics/white.png")
font_ = ImageFont.truetype("font/Bunny Lover.ttf", 100)
font1_ = ImageFont.truetype("font/Bunny Lover.ttf", 140)
font2_ = ImageFont.truetype("font/Bunny Lover.ttf", 180)
font = ImageFont.truetype("font/micro_se.ttf", 150)
font1 = ImageFont.truetype("font/micro_se.ttf", 120)
font2 = ImageFont.truetype("font/micro_se.ttf", 160)
font3 = ImageFont.truetype("font/micro_se.ttf", 100)


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

    # Add Text to leaderboard
    if(leaderboard[0][1]!="NA"):
        # First place
        drawing.text((450, 600), leaderboard[0][1], fill=(255, 255, 255), font = font1)
        drawing.text((1500, 750), str(int(leaderboard[0][0])), fill=(255, 255, 255), font = font3)
    if(leaderboard[1][1]!="NA"):
        # Second place
        drawing.text((450, 1100), leaderboard[1][1], fill=(255, 255, 255), font = font1)
        drawing.text((1500, 1250), str(int(leaderboard[1][0])), fill=(255, 255, 255), font = font3)
    if(leaderboard[2][1]!="NA"):
        # Third place
        drawing.text((450, 1600), leaderboard[2][1], fill=(255, 255, 255), font = font1)
        drawing.text((1500, 1750), str(int(leaderboard[2][0])), fill=(255, 255, 255), font = font3)

    pic.save(name, Path = "pictures/temporary_pics")

def load_submission_pic(username, score):
    img = white_pic
    img = img.resize((1000, 750))
    drawing = ImageDraw.Draw(img)
    text_score = str(score)
    drawing.text((40, 100), "Hold: ", fill=(0, 0, 0), font = font1)
    drawing.text((40, 220), username, fill=(0, 0, 0), font = font1)
    drawing.text((40, 450), "Udledning: ", fill=(0, 0, 0), font = font1)
    drawing.text((40, 570), text_score + " gCO2", fill=(0, 0, 0), font = font1)
    img.save("pictures/temporary_pics/team_score.png")

# Helper function to combine pictures vertically
def combine_pics(pic1, pic2, i):
    img1 = cv2.imread(pic1)
    img2 = cv2.imread(pic2)
    resized = cv2.resize(img1, (750, 500))
    resized1 = cv2.resize(img2, (750, 500))
    im_v = cv2.hconcat([resized, resized1])
    # save the output image
    cv2.imwrite("pictures/temporary_pics/combined" + str(i) + ".png", im_v)

# Helper function to combine pictures horrtizontally
def combine_pics1(pic1, pic2):
    img1 = cv2.imread(pic1)
    img2 = cv2.imread(pic2)
    resized = cv2.resize(img1, (1500, 1000))
    resized1 = cv2.resize(img2, (1500, 1000))
    im_v = cv2.vconcat([resized, resized1]) 
    height, width, channels = im_v.shape
    resized2 = cv2.resize(im_v, (2000, 1500))
    # save the output image
    cv2.imwrite("pictures/temporary_pics/combined2.png", resized2)

def load_input_output(input_pics, food):
    #resizeing images
    background = cv2.imread("pictures/visualization_pics/matrix.png")
    resized = cv2.resize(background, (2000, 1500))
    picture1 = cv2.imread(input_pics[0])
    resized1 = cv2.resize(picture1, (500, 300))
    picture2 = cv2.imread(input_pics[1])
    resized2 = cv2.resize(picture2, (500, 300))
    picture3 = cv2.imread(input_pics[2])
    resized3 = cv2.resize(picture3, (500, 300))
    #Writing resized pictures
    cv2.imwrite("pictures/temporary_pics/background.png", resized)
    background1 = Image.open("pictures/temporary_pics/background.png")
    cv2.imwrite("pictures/temporary_pics/pic1.png", resized1)
    img0 = Image.open("pictures/temporary_pics/pic1.png")
    cv2.imwrite("pictures/temporary_pics/pic2.png", resized2)
    img1 = Image.open("pictures/temporary_pics/pic2.png")
    cv2.imwrite("pictures/temporary_pics/pic3.png", resized3)
    img2 = Image.open("pictures/temporary_pics/pic3.png")
    #Combining images
    background1.paste(img0, (75, 220))
    background1.paste(img1, (700, 220))
    background1.paste(img2, (1350, 220))
    #Tegner predictions
    drawing = ImageDraw.Draw(background1)
    drawing.text((130, 1350), food[0], fill=(0, 255, 0), font = font_)
    drawing.text((770, 1350), food[1], fill=(0, 255, 0), font = font_)
    drawing.text((1400, 1350), food[2], fill=(0, 255, 0), font = font_)
    background1.save("pictures/temporary_pics/input_output.png")
    path = "pictures/temporary_pics/input_output.png"
    return path

def resize_pics(picname):
    background = cv2.imread("pictures/visualization_pics/" + picname)
    resized = cv2.resize(background, (2000, 1500))
    cv2.imwrite("pictures/temporary_pics/" + picname, resized)
    path = "pictures/temporary_pics/" + picname
    return path
