import json

#i got the piano sounds from: https://github.com/fuhton/piano-mp3

twinkle_twinkle = ['C4','C4','G4','G4','A4','A4','G4',\
                'F4','F4','E4','E4','D4','D4','D4',\
                'G5','G5','F4','F4','E4','E4','D4',\
                'G5','G5','F4','F4','E4','E4','D4',\
                'C4','C4','G4','G4','A4','A4','G4',\
                'F4','F4','E4','E4','D4','D4','C4',\
                ]

shape_of_you = ['C4','C4','C4','D4','D4','E4','D4','E4','F4','G4','C4','C4','C4','D4','D4','E4','D4','E4','F4','G4',
'C4','C4','C4','D4','D4','E4','D4','E4','F4','G4','C4','C4','C4','D4','D4','E4','D4','E4','F4','G4',
'G4','F4','E4','D4','C4','G4','F4','E4','D4','C4','G4','F4','E4','D4','C4']        this does not sound good but you're free to change the tune :)

happy_birthday = ["G4", "G4", "A4", "G4", "C5", "B4",\
                    "G4", "G4", "A4", "G4", "d5", "C5",\
                    "G4", "G4", "G5", "E5", "c5", "B4", "A4",\
                    "F5", "F5", "E5", "C5", "D5", "C5"]


# sticking with modern classics
notes = {
    '1' : twinkle_twinkle,
    '2' : happy_birthday
    '3' : shape_of_you   
}

with open('notes.json', 'w') as file: # you can add a song and when you run this file, it'll create a .json file called notes.json
    json.dump(notes,file) # this will write the notes inside the list which we'll access to play for each block
