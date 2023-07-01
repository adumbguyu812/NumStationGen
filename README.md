# NumStationGen

This is a dumb little project I've done a few times, all bad. I have a mild obsession with number stations, and wanted to see if I could "make" one myself. Turns out it's pretty simple.
This one I'm a bit more proud of though, as it actually works and can output straight to a MIDI file. Why would you want that you ask? Well to put in a DAW so I don't have to manually put the numbers into order!

This is pretty crude in my eyes and ugly/clunky to use, but it _does_ work. Writing the text file is especially ugly, but still kinda readable.
I more than likely won't do many or even any updates to this, but who knows.

# How to use this

Before you can use this, you will need to install Python obviously, but also MIDIUtils. It's as simple as `pip install midiutils`

Once you do that, we can get started:

1. Open a cmd or powershell prompt in the root directory of the program.
2. Run `python main.py` and you should be guided through the process
   -It _should_ be self-explainitory, but let me know if it's not!
3. If you chose to write to a MIDI file, you should have 2 new files with the file name you chose, with a "_main" and "_pre" suffix
4. Import these into your DAW of choice and setup your instriment how ever you want it to work. By default it's setup so C6# is 0, and it goes up to A6# as 9. B6 is used as silence, so just keep that in mind.

To decrypt messages made by this script:
1. Take the number from the message, 7 for example
2. divide it by the corresponding number from the key/pad, 4 for example
   -If it has a remainder (like 7/4) it translates to a "1", and if it's clean division (like 6/3) it translates to a "0"
   -Put in simpler terms, you take the modulus of the msg÷key and 0 = 0 and anything else is 1
4. once you have a string of binary, you can put it into most ASCII-Binary converters to get the message in plain text
   -At some point I may make this a native thing in the program, just enter the message and key and it spits out the binary and text. probably make it read from a file if the user chooses to make it easier 
