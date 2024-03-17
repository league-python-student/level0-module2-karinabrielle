# When you are done, this program will draw an ellipse 
# that travels across the screen when the mouse is pressed.

# ***********  SOUND ***************
# Some computers are unable to play sounds. 
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher 

can_play_sounds = False

def setup():
    size(800, 200)
    global x

    # 1. Set the variable named x to 50.
    x = 400
def draw():
    background(200, 200, 200)
    global x
    
    # 2. Draw an ellipse of height and width 50. Make sure to use the x variable
   
     # for its X position. Pick a y value that places it half way down the window.ellipse
    fill('#F07999')
    circle = ellipse(x, 100, 50, 50)
    # 3. Fill in the ellipse with a nice color. Remember to put it above the code
    # where you draw the ellipse.
    
    # 4. If the mouse is pressed change the x value so that the dot moves to the right
    if mousePressed:
        x+=5
    # 5. If your dot moves slowly, make it move faster. If it moves too quickly,
    # slow it down (you have to figure out what part of your code to change)
    if x > 775:
        play_sound()
    # 6. Use an if statement to play a sound (ding) when your dot crosses the finish
    # line (right side of window). A playSound() method is provided (you have to
    # uncomment the code at the bottom of this program to get this to work)
    

global sound_played
sound_played = False
def play_sound():
    global sound_played 
    if can_play_sounds:
        if not sound_played:
            minim = Minim()
            sound = minim.loadSample("ding.wav")
            sound.trigger()
            sound_played = true
            pass
    fill(0)
    textSize(36)
    text("WINNER!!", width/2, height/2)
    
