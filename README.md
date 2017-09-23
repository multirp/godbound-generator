# Generator for Godbound V0.11

This program is a fairly simple generator for Kevin Crawford's Godbound roleplaying game.  Right now, it allows you to randomly generate a ruin (of four different sizes), or a court of any of the different types.  These random creations are specifically geared towards information within the free version of Godbound, with no adjustments based on my own personal houserules.

# System Requirements
* Python 3.3.5

Other than requiring Python, anything else should run just fine.  The program itself is small, and all CLI based, so there should be no real system requirements.

You may be able to get away with other versions of Python3 - I use nothing specific to 3.3.5.  It is incompatible with Python2, however.

# Using the Program
The Godbound Generator is CLI based - I'm terrible at UI's (and arguably terrible at programming, but let's ignore that for now), so you will have to open up a command line in the directory that you downloaded it, and type 'py godbound-generator.py'.

You can also double click on the file in Windows Explorer or similar, if that's more your style.

Within the program itself, it's governed by numeric choices.  You will see a list of choices, and you can pick the one that you want, and in the end you'll wind up with a randomly generated place or group.

Right now, the program closes by itself after you've generated an object.  That's in the future roadmap to take care of, but for now it is functional - I wanted to get this online before I start tinkering with it too much.

## 'Saving' information
At present, this generator has no file i/o.  It is pretty soon on my list, but you can copy and paste information from the terminal screen that you run it in order to generate files yourself.

This program also saves nothing - if you close out of the program before you've copy/pasted the information out of the terminal, you *will* lose everything.  It's easy enough to get back (it's a random generator after all, just make another one!), but it's worth note that you'll physically lose access to that specific ruin or court.

# Roadmap for the future
Right now, I don't have any major plans for how to adjust this.  I will probably add in a Heaven generator as well, and potentially a couple more randomly generated things specific to Godbound.

## Things I know I want to add/To-do list
* ~~Replace randint with random.choice~~
* Provide a built-in way to paste neatly to a file
* ~~Fix the minor actors printing to strip out the square brackets~~
* Potentially add in other random stuff that's Godbound related (Heaven locations, potentially NPCs)
* Allow to generate multiple ruins/courts without shutting the program down

## Things I will NOT likely add
Populating ruins, or auto generating NPCs for courts.  Godbound is designed to require a bit of finesse to fit their skeleton into the world - and that requires GM Adjucation.  You know far better than me what goes at your table and how to handle it.  Any NPC generation will be in a vacuum.

# Copyright/Licensing
I own none of the information contained within the libs/lists.py file.  All of that information is taken from the Godbound Roleplaying game by Kevin Crawford (free version).  Mr. Crawford does not hold issues (as of my knowledge at this time) with people creating generators based on his free content - see the RPG.net post [here](https://forum.rpg.net/showthread.php?773601-Sine-Nomine-Godbound-Staff-Pick&p=21076036#post21076036) for more details.

At any time, if he changes his opinion and contacts me, I will remove the lists.py file from the program and/or remove the generator in it's entirety.

The rest of the program is created by me, and licensed under the MIT license - feel free to do whatever you would like with it, but I ask that you mention where it came from, as well as link to this repository if feasible.

# Change Log
v0.11
    Replaced unnecessary randints with choice() - no more list size issues!
    Stripped out the square brackets around the minor actors, to pretty them up a bit

v0.1
    Initial Release
