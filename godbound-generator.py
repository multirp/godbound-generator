import os
from lib import lists
from random import randint
from random import choice

def main():
    os.system("clear")

    menu = """
MultiRP's Godbound Generator v0.1

Welcome to the Godbound Generator!  This generator randomly generates ruins and
courts for use with Kevin Crawford's Godbound setting.  Right now, this only
includes the basic Godbound information with it (and only the free version, if
you find any Deluxe version information inside of this, please let me know!) and
does not include any house rules or the like that are used within my own games. 
This is basically just a way to quickly and easily generate randomized content.

What do you want to do?

    1: Generate a Ruin
    2: Generate a Court
    3: Get help about this program
    4: Quit
"""
    print(menu)
    menuChoice = input("1-4: ")


    if menuChoice == '1':
        ruin()
    elif menuChoice == '2':
        court()
    elif menuChoice == '3':
        genhelp()
    elif menuChoice == '4':
        exit()
    else:
        input("Please choose 1-4 from the menu above!")
        main()

def genhelp():
    os.system("clear")
    helpscreen = """
This program was essentially created because I was trying out the Godbound
system and found that, while the random creation of ruins and courts was
somewhat interesting, it would be handy to have a place to instantly be able to
generate new content.

This program also allows for content to be added, removed, and modified quite
easily (look in the lists.py file!) so you can truly make a generator that fits
your own campaigns.

Using the program is (hopefully) simple.  I give menus where appropriate so you
can decide what exactly you want to do, and make things easy to perform...
hopefully.

There is no UI other than what you see.  I'm horrible at graphic design, and
this was just a quick hack (but then, it could be argued that i'm pretty
subpar at programming too!) but this should allow people to generate their
own content.

    """
    helpscreen2 = """
One thing to keep in mind is that I sort of 'creatively interpreted' Godbound's
rules in ruin generation.  For instance, the Godbound book states that "Not
every location needs all of these things.  Indeed, about a quarter of your
locations should be empty and largely devoid of anything important" (page 118).

I took this to heart, giving each room a flat 25% chance to not contain anything
of importance, as well as gave each individual room aspect (Treasures, moods,
and the like) a chance to not happen as well.

With luck, this means that you don't have to do much thinking about what to
include or not include, as the randomized creation takes care of it for you.

If you want to change the percentages, they are the variables with the word
'Chance' in them that use a random integer from 1 to 100.
    """
    print(helpscreen)
    input("Hit Enter to go to the next page")
    print(helpscreen2)
    input("Hit Enter to return to the main menu")
    main()

def ruin():
    os.system("clear")
    createRuin = """
You are currently creating a Ruin.  Within Godbound's rules, a 'Ruin' is any
potentially dangerous place that has some reason for the Godbound to be there,
and, usually, some reward at the end.

Most systems devote time and space to determining exact composition of ruins,
but Godbound tends to require that the GM flavor things to make it fit within
the rules they have set, and what they want that ruin for.

In this light, a forest during the day is much the same as a castle at night,
or a shard of Heaven between dimensions.  Ruins can be literally anything, and
the random generation for them tends to be pretty loose, and needs to be
interpreted and fleshed out into your actual world.

Menu:
    1: Generate a Small ruin (6 rooms)
    2: Generate a Medium ruin (10 rooms)
    3: Generate a Large ruin (14 rooms)
    4: Generate a Huge ruin (20 rooms)
    5: I don't want a ruin, take me back to the menu!
    """
    print(createRuin)
    menuChoice = input("1-5: ")
    if menuChoice == '1':
        rooms = 6
    elif menuChoice == '2':
        rooms = 10
    elif menuChoice == '3':
        rooms = 14
    elif menuChoice == '4':
        rooms = 20
    elif menuChoice == '5':
        main()
    else:
        input("Please choose 1-5 from the menu above!  Press Enter to continue")
        ruin()

    print("The ruin's purpose is: " + choice(lists.purposeList))
    print("The ruin's main hazard is: " + choice(lists.hazardList))
    print("The ruin's main reward is: " + choice(lists.rewardList))
    print("")
    finishedRooms = 0

    # This while loop takes the 'rooms' variable from above and compares it to
    # the 'finished Rooms' variable.  Once they match, the while loop breaks
    # off.
    while finishedRooms < rooms: 
        purpose = choice(lists.roomPurposeList)
        emptyChance = randint(1,100)

        # There is a 25% chance that a given room is empty.
        if emptyChance < 25:
            roomEmpty = "This room is otherwise not special"
        else:
            # These are the various dice rolls that determine the spread of the
            # rooms within the ruin.  They're brought to the very top to help
            # a bit with legibility, they were originally under each section
            valuablesChance = randint(1,100)
            moodChance = randint(1,100)
            movementChance = randint(1,100)
            physicalPerilChance = randint(1,100)
            occupantPerilChance = randint(1,100)
            magicalPerilChance = randint(1,100)

            # All of these rolls function the same.  You have a variable, and
            # compare it to a d100 percentile die roll.  If the roll is under
            # the constant (or equal to), that aspect of the room is special,
            # and will be pulled out of a list.  Otherwise, it returns a
            # 'nothing special' string to input at the very end
            if valuablesChance <= 60:
                valuables = choice(lists.roomValuablesList)
            else:
                valuables = "No Special Treasure"
            if moodChance <= 50:
                mood = choice(lists.roomMoodList)
            else:
                mood = "No Special Mood"
            if movementChance <= 40:
                movement = choice(lists.roomMovementProblemsList)
            else:
                movement = "No Special Problems"
            if physicalPerilChance <= 35:
                physicalPeril = choice(lists.roomPhysicalPerilList)
            else:
                physicalPeril = "No Special Physical Perils"
            if occupantPerilChance <= 30:
                occupantPeril = choice(lists.roomOccupantPerilList)
            else:
                occupantPeril = "No Special Occupant Perils"
            if magicalPerilChance <= 20:
                magicalPeril = choice(lists.roomMagicalPerilList)
            else:
                magicalPeril = "No Special Magical Peril"

        # This formats the actual room description, starting off with a generic
        # "RoomX" name, where X is equal to the number of the generated room.
        # It then gives it's purpose on the same line, and itemizes all of the
        # things that are special about it

        # Yes, the repeated emptyChance is intended. There isn't a change to the
        # variable between the two occurances (so they should always be the
        # same), and I ran into a bug where it would fail to print out rooms
        # when I was trying to use the non-null 'empty' string for comparison
        # instead
        print("Room"+ str(finishedRooms+1) + " details (" + purpose + ")")
        if emptyChance < 25:
            print("   There is nothing special about this room")
            print("")
        else:
            print("   Mood: " + mood)
            print("   Treasure: " + valuables)
            print("   Ingress/Egress Problems: " + movement)
            print("   Physical Peril: " + physicalPeril)
            print("   Occupant Peril: " + occupantPeril)
            print("   Magical Peril: " + magicalPeril)
            print("")

        finishedRooms = finishedRooms + 1
    input("Press Enter key to close...") 

def court():
    os.system("clear")
    createCourt = """
You are currently creating a Court.  A Court within Godbound is a group of
people who control some major part of an institution within your campaign.  A
king and his aides, a criminal mastermind, a blacksmith and his trainees, etc.

Much like ruins, courts are fairly bare-bones, relying on the GM to integrate
them into the setting, but this generator helps to provide a leg up and get
some of the stuff out of the way so the GM can focus on creating the encounters.

Menu:
    1: Generate an Aristocratic court
    2: Generate a Bureaucratic court
    3: Generate a Business court
    4: Generate a Community court
    5: Generate a Criminal court
    6: Generate a Temple court
    7: Explain the types of courts
    8: I don't want a court, get me to the main menu!
    """
    courtTypes = """
The courts are broken up into six different types: Aristocratic, Bureaucratic,
Business, Community, Criminal, and Temple.  These are, roughly, described like
this:

Aristocratic: A basic type of leadership-style court that can be autocratic or
democratic.  Most kingdoms are founded on aristocrasy, and bloodline relations.

Bureaucratic: Found mostly in higher-population areas, this court runs things
without bloodline assistance (like a king), or other oversight.  Most modern
governments would be made like this.

Business: A business court is, well, a business.  A merchant and his entourage,
a blacksmith, or similar.  Essentially a smaller group focused on making money.

Community: A smaller community that tends to be run by local people, rather than
the faceless men of other areas.  The major difference between this and
bureaucratic is one of scale.

Criminal: Any sort of criminal organization, or others that make their trade
on the illicit front.  Thieves guilds, assassin hideouts, fences, and the like.

Temple: The clergy.  Not much else to say, but they tend to be the priests and
their associates or the like.
    """
    print(createCourt)
    menuChoice = input("1-8: ")

    # This list does a couple of things.  It controls the main menu for the type
    # of court you want to make, but it also establishes some 'baseline'
    # variables like majorActorsList.  These variables point towards the lists
    # in the lists.py file that correspond to the type of court it is.  I'm
    # doing this to only have to type up the random generation once, rather than
    # once per court type
    if menuChoice == '1':
        courtType = "Aristocratic"
        courtMoodName = "Court Mood"
        courtMoodList = lists.aristocraticCourtMood
        majorActorsList = lists.aristocraticMajorActors
        minorActorsList = lists.aristocraticMinorActors
        powerSourcesList = lists.aristocraticPowerSources
        conflictsList = lists.aristocraticConflicts
        consequencesList = lists.aristocraticConsequences
        defensesList = lists.aristocraticDefenses
    elif menuChoice == '2':
        courtType = "Bureaucratic"
        courtMoodName = "How the Buraeucracy is Regarded"
        courtMoodList = lists.bureaucraticCourtMood
        majorActorsList = lists.bureaucraticMajorActors
        minorActorsList = lists.bureaucraticMinorActors
        powerSourcesList = lists.bureaucraticPowerSources
        conflictsList = lists.bureaucraticConflicts
        consequencesList = lists.bureaucraticConsequences
        defensesList = lists.bureaucraticDefenses
    elif menuChoice == '3':
        courtType = "Business"
        courtMoodName = "How the business is currently doing"
        courtMoodList = lists.businessCourtMood
        majorActorsList = lists.businessMajorActors
        minorActorsList = lists.businessMinorActors
        powerSourcesList = lists.businessPowerSources
        conflictsList = lists.businessConflicts
        consequencesList = lists.businessConsequences
        defensesList = lists.businessDefenses
    elif menuChoice == '4':
        courtType = "Community"
        courtMoodName = "Community Temperment"
        courtMoodList = lists.communityCourtMood
        majorActorsList = lists.communityMajorActors
        minorActorsList = lists.communityMinorActors
        powerSourcesList = lists.communityPowerSources
        conflictsList = lists.communityConflicts
        consequencesList = lists.communityConsequences
        defensesList = lists.communityDefenses
    elif menuChoice == '5':
        courtType = "Criminal"
        courtMoodName = "Main line of crime"
        courtMoodList = lists.criminalCourtMood
        majorActorsList = lists.criminalMajorActors
        minorActorsList = lists.criminalMinorActors
        powerSourcesList = lists.criminalPowerSources
        conflictsList = lists.criminalConflicts
        consequencesList = lists.criminalConsequences
        defensesList = lists.criminalDefenses
    elif menuChoice == '6':
        courtType = "Temple"
        courtMoodName = "Temple mood"
        courtMoodList = lists.templeCourtMood
        majorActorsList = lists.templeMajorActors
        minorActorsList = lists.templeMinorActors
        powerSourcesList = lists.templePowerSources
        conflictsList = lists.templeConflicts
        consequencesList = lists.templeConsequences
        defensesList = lists.templeDefenses
    elif menuChoice == '7':
        os.system("clear")
        print(courtTypes)
        input("Press Enter to return to the courts menu")
        court()
    elif menuChoice == '8':
        main()
    else:
        input("Please choose 1-8 from the menu above!  Please press Enter")
        court()

    # Like before, these random integers function as the die roller, in this
    # case for most of the necessary court things, as well as the number of
    # actors of note within the court (3-5 major and 4-8 minor, change to fit)
    powerStructureType = randint(0,5)
    courtMood = randint(0,11)
    courtConflict = randint(0,11)
    courtConsequences = randint(0,11)
    courtDefenses = randint(0,11)

    numMajorActors = randint(3,5)
    numMinorActors = randint(4,8)
    minorActors = [] # Empty list to store the minor actors in

    # Formatting the court layout.  At the very end are the two while loops that
    # give us our actors.  I chose to do it this way so they came after the
    # basic court information (like court type), but didn't want them in the
    # middle of what was otherwise a plain print statement.  I kind of like the
    # layout myself
    print("Court Type: " + courtType + " (" + choice(lists.courtPowerStructure)
                                                    + ")")
    print("   " + courtMoodName + ": " + choice(courtMoodList))
    print("   Court Conflict: " + choice(conflictsList))
    print("   Court Defenses: " + choice(defensesList))
    print("   Consequences of Destruction: " + choice(consequencesList))
    print("")

    # We're going to roll for our major and minor actors (and power sources)
    # from here.  The major actors will be printed directly, since they have
    # other information attached to them, and are 'major' actors.  The minor
    # actors are appended to the minorActors list, and printed all at once, with
    # little fanfare
    while numMajorActors > 0:
        print("Major Actor: " + choice(majorActorsList) + " (Power Source: "
            + choice(powerSourcesList) + ")")
        numMajorActors = numMajorActors - 1
    print("")
    while numMinorActors > 0:
        minorActors.append(choice(minorActorsList))
        numMinorActors = numMinorActors - 1
    # This takes the list of minor actors, and formats them more appropriately
    # with commas, and no square brackets, and prints them out
    print('Minor Actors: ' + ', '.join(minorActors))

    input("Press Enter key to close...") 


main()
