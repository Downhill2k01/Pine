## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the
## name of the character.

define y = Character('y/n, [instability_points]', color="#2E8B57")
define n = Character('????')

## define characters w/ routes

define c = Character('Charlie, [charlie_points]', color="#FBAED2")
define l = Character('Laura, [laura_points]')

define d = Character('Dan, [dan_points]')
define r = Character('Ryan, [ryan_points]')
define j = Character('Jason, [jason_points]')



## The game starts here.

label start:

    ## define character variables + instability

    $ charlie_points = 0
    $ laura_points = 0

    $ dan_points = 0
    $ ryan_points = 0
    $ jason_points = 0

    $ instability_points = 0

    jump day0
