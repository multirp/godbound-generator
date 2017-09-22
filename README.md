# Generator for Godbound V0.1

This program is a fairly simple generator for Kevin Crawford's Godbound roleplaying game.  Right now, it allows you to randomly generate a ruin (of four different sizes), or a court of any of the different types.  These random creations are specifically geared towards information within the free version of Godbound, with no adjustments based on my own personal houserules.

# System Requirements
You will require at least Python 3.3.5.  You may be able to get away with other versions (I use nothing particularly specific to that version, the program is pretty basic), but it is incompatable with Python 2.

System specs should be ridiculously low; as long as you have a proper version of Python, you should be able to run it.

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
* Replace randint with random.choice
* Provide a built-in way to paste neatly to a file
* Fix the minor actors printing to strip out the square brackets
* Potentially add in other random stuff that's Godbound related (Heaven locations, potentially NPCs)
* Allow to generate multiple ruins/courts without shutting the program down

## Things I will NOT likely add
Populating ruins, or auto generating NPCs for courts.  Godbound is designed to require a bit of finesse to fit their skeleton into the world - and that requires GM Adjucation.  You know far better than me what goes at your table and how to handle it.  Any NPC generation will be in a vacuum.
