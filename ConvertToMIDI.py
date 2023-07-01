

from midiutil import MIDIFile

# MIDI note number, 65 should be silence, this is just based off my preset in FL Studio, so you'll need to change this
# around for your use-case. This starts at 0 and ends at 9
notes = [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 70  # In BPM
volume = 100  # 0-127, as per the MIDI standard


def ConvertNumbersToMIDI(numToConvert, startingTime, fileName):
    MyMidi = MIDIFile(1)
    MyMidi.addTempo(track, time, tempo)
    lTime = startingTime
    for n in numToConvert:
            for s in n:
                if " " not in s:
                    MyMidi.addNote(track, channel, notes[int(s)], lTime, duration, volume)
                    lTime = lTime + 1
                elif " " in s:
                    MyMidi.addNote(track, channel, notes[10], lTime, duration, volume)
                    lTime = lTime + 1
                elif s is not type('string'):
                    print("Something went wrong here, the digit could not be converted to a midi note!")
    with open((fileName + "_main.mid"), "wb") as output_file1:
        MyMidi.writeFile(output_file1)
        
        
def GeneratePreamble(startingTime, fileName, lengthOfMessage, first3Digits):
    MyMidi = MIDIFile(1)
    MyMidi.addTempo(track, time, tempo)
    lTime = startingTime
    x = 3  #beats of silence
    y = 3  #ID repeats
    z = 1  #Times to repeat the first 3 digits of the pad, and length of message
    print("DEBUG::: Length of Message = " + lengthOfMessage + "\nDEBUG::: First 3 Digits of Pad = " + first3Digits)
    
    print("\nEnter your 3 digit ID")
    r1 = input("ID: ")
    if len(r1) == 3:
        while y > 0:  #Play the ID 3 times
            for n in r1:
                MyMidi.addNote(track, channel, notes[int(n)], lTime, duration, volume)
                lTime = lTime + 1
            while x > 0:  #3 Beats of silence
                MyMidi.addNote(track, channel, notes[10], lTime, duration, volume)
                lTime = lTime + 1
                x = x - 1
            y = y - 1
            x = 3
        MyMidi.addNote(track, channel, notes[10], lTime, duration, volume)
        lTime = lTime + 1
        while z >= 0:
            for d in first3Digits:  #This should be from the PAD string, used to identify the pad to use
                MyMidi.addNote(track, channel, notes[int(d)], lTime, duration, volume)
                lTime = lTime + 1
            while x > 0:
                MyMidi.addNote(track, channel, notes[10], lTime, duration, volume)
                lTime = lTime + 1
                x = x - 1
            x = 3
            for l in lengthOfMessage:  #Calculated from number of spaces + 1
                MyMidi.addNote(track, channel, notes[int(l)], lTime, duration, volume)
                lTime = lTime + 1
            while x > 0:
                MyMidi.addNote(track, channel, notes[10], lTime, duration, volume)
                lTime = lTime + 1
                x = x - 1
            z = z - 1
            x = 3
            
        with open((fileName + "_pre.mid"), "wb") as output_file2:
            MyMidi.writeFile(output_file2)
    else:
        print("MUST be 3 digits, preamble generation aborted!")
        