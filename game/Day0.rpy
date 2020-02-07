label day0:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest road

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "This road is longer than I remembered"

    "Two days' drive from the city."

    "The acrid smell of pine sap gradually crept into the car over the last few miles as we entered the forest."

    "I haven't visited this town in at least ten years; it's strange how much and how little I remember of it"

    "I used to stay at this cabin over the summer with my family"

    "And now I’m using it to get away from them"

    "Funny how that works"

    "A voice I haven’t heard in hours pipes up from behind me, snapping me back to reality"

    d "what percent are you at?"

    "I doubt dan is talking to me, and instead to the girl sitting in the passenger’s seat,"

    "My phone is running GPS and playing music."

    d "charlie?"
#beer can?
    "He taps her shoulder with the bottom of his beer can and charlie takes out one earbud"

    c "what? Oh…"

    c "uh...Sixty percent but you can use it if you want."

    d "thanks"

    "She turns to me"

    c "Where’s Ryan's car?"

    y "Should be right behind us"

    d "nobody there"

    "I shrug"

    y "the others are probably just going to be a little late to the cabin, no big deal"

    c "well how long until we get there?"

    y "I’m not really sure"

    c "I don’t know about you but I’m freaking tir-"

    #cRASH!

    "My foot slams on the breaks"

    "My mouth is flooded with the taste of copper"

    "Everyone in the car is screaming"

    "My eyes open after only a few seconds to see that the windshield is cracked beyond repair"

    "There is a smear of blood on the window"

    "I put the car in park and step out, ignoring the commotion from within"

    "My head spins like a roulette wheel"

    "I regain lucidity to the realization that my passengers have exited my car just like I have"

    y "I think we hit a deer"

    c "yOU THINK?"

    d "oh my GOD!"

    "I sit down off to the side of the road onto the dirt"

    "There's no deer"

    "Where did it go?"

    "I look at the road behind me; theres nothing on it but a pothole"

    d "what the hell?"

    d "we didn’t hit a fucking pothole, did we?"

    c "well what do we do now?"
#cjhange this
    c "we cant call the police, we have so much alcohol"

    menu :
        "What now?"

        "call police":
            #$
            jump post_crash_call1

        "call friends":
            $ instability_points += 1
            jump post_crash_friends1

label post_crash_friends1:
     y "im gonna call ryan and ask him to pick us up"

     c "call jason, ryans driving"

     "i pick up the phone and dial jason's number"

     j "hello?"

     y "yeah, we uh, hit a deer"

     j "oh my god! are you okay?"

     y "yeah i just need yall to get over here"

     "just as i say that i see their car turn the corner around the pines"

     "ryan stops the car on the 'shoulder' of the road"

     "everyone but laura gets out"



     





    jump the_end

    return
