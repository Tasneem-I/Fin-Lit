# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Leon", image="leon")
define p = Character("[pname]", color="#1aa7ec")


# The game starts here.

label start:
    $ pname = renpy.input("What would you like to be called as?: ", length=45)
    #$ pc = renpy.input("Choose color -pink or blue?: ")
    #if pc.lower() == "blue":
    #    $ pcolor = "#1aa7ec"
    #else:
    #    $ pcolor = "#1aa7ec"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    p "You've created a new Ren'Py game."

    l "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
