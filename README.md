# Godbound Generator V0.12

This program is a fairly simple generator for Kevin Crawford's Godbound roleplaying game.  Right now, it allows you to randomly generate a ruin (of four different sizes), or a court of any of the different types.  These random creations are specifically geared towards information within the free version of Godbound, with no adjustments based on my own personal houserules.

It can also be used, potentially, for any other fantasy-styled game.  You will have to adjucate some things accordingly, but you can use it to quickly and easily populate rooms in dungeons.

## Prerequisites

* [Python3](https://www.python.org/) - The main programming language used.  Specifically, I use version 3.3.5, but use nothing specifically geared towards that version.  Other versions should work (and let me know if they don't!).  Due to the changes between Python2 and Python3, however, it **does** have to be Python3


## Getting Started

The files contained within this program are:
```
    lib/lists.py - the main list file that contains the randomly generated content
    LICENSE.md - the MIT License
    README.md - this file (the readme)
    godbound-generator.py - the main python program
```

First, you can click on the green 'Clone or Download' button, and select to download it as a zip (or clone it), or if you prefer the CLI interface, you can open up your command line - with git installed - and type:

```
git clone https://github.com/multirp/godbound-generator.git
```

This will put the program onto your computer, where you are able to run it.  The easiest way to run it is to just double click the 'godbound-generator.py' file in the chosen directory, but you can also run `py godbound-generator.py` in the downloaded/unzipped directory to start the program.

### Using the Program

The program should be fairly straight forward to use.  It is completely CLI based, meaning there is no graphical interface attached to it.  But, the UI is designed to be fairly simple to navigate anyway (and it's a fairly simple program).

At times, you are given a choice of what to do with numbers next to the choice.  Simply hit the number, then your Enter key, to go to that part of the program.  Since the content is entirely randomly generated aside from a couple of pieces of user input, the menu system is not incredibly robust, but it functions well enough for this program.

#### Note about Saving and Data

This program does not currently store or save any information to the file system.  This means if you close out of the program before copying the information down, then you **will** lose all information that it has - likewise, if you generate a second ruin or court the first will be lost.

If enough people want, I will include a way to save to a file - probably append to a text file - but at present I see no reason to do so.  You can copy and paste from the console, and since it's a random content generator, everything is changing anyway (if you do lose work, just rerandomize it)

## Contributing

In the unlikely event you want to contribute to the program, let me know, and we can work something out.  I tend to be pretty easy going, and have no problem with people adding to my code.

## Authors

* **Me, MultiRP**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Copyright

I own none of the information contained within the libs/lists.py file.  All of that information is taken from the Godbound Roleplaying game by Kevin Crawford (free version).  Mr. Crawford does not hold issues (as of my knowledge at this time) with people creating generators based on his free content - see the RPG.net post [HERE](https://forum.rpg.net/showthread.php?773601-Sine-Nomine-Godbound-Staff-Pick&p=21076036#post21076036) for more details.

At any time, if he changes his opinion and contacts me, I will remove the lists.py file from the program and/or remove the generator in it's entirety.

## Roadmap for the future

There are no major plans for the system right now, I am more or less adding to it as I find need of particular details.  I do have a (short) to-do list, but not everything I may want to get done is included in that.

I am also working on a javascript version of it for use on GitHub Pages, so you can just refresh the screen in order to get a new ruin/court.  It will also allow me to use HTML/CSS to color/style the output in a way that isn't eye-bleedingly terrible.  Though it'll still probably be bad (Function over form, that's me!)

### Things I know I want to add/To-do list
* Potentially add in other random stuff that's Godbound related (Heaven locations, potentially NPCs)
* ~~Replace randint with random.choice~~
* ~~Fix the minor actors printing to strip out the square brackets~~
* ~~Allow to generate multiple ruins/courts without shutting the program down~~

### Things I will NOT likely add

Godbound, by its nature, is a very flexible system that requires GM intervention in order to port content into it.  As such, I will not be doing NPC generation in regards to stuff like ruins or courts.  If the GM randomly generated a court, the people that it contains should fit into the GM's world, and I cannot ensure that.

As with many roleplaying games, the GM is the storyteller.  It's their (and their players) stories, and they know best what type of story they want to play, and what they want to craft.  If I do any NPC generation (not an impossible idea), it will be in a 'vacuum', and not attached to other aspects of the randomly generated content.

## Acknowledgments

* Kevin Crawford - for Godbound
* StackExchange - for having an awesome community that helped piece a couple of things together

## Change Log

v0.12
* Reformatted ruin output to remove unnecessary noise; no more "No X" outputs!
* Added in a menu system to generate another ruin/court, return to the main menu, or exit the program when you finish generating content

v0.11
* Replaced unnecessary randints with choice() - no more list size issues!
* Stripped out the square brackets around the minor actors, to pretty them up a bit

v0.1
* Initial Release
