from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    # read file
    
    with open('./inputs/input.txt', 'r') as f:
        text = f.read()
        
    # split on empty lines
    text = text.split('\n\n')

    # create elf array of calories
    elves = [
        elf.split('\n') for elf in text
    ]

    # for each elf sum all of their calories carried
    elf_calories = [
        sum([
            int(calories) for calories in elf
        ])
        for elf in elves
    ]

    # sort the output highest to lowest
    elf_calories.sort(reverse=True)

    # respond with the calories in question
    response = (f"<p>The elf carrying the most calories is carrying {elf_calories[0]} calories</p>" +
                f"<p>The top 3 elves are carrying a total of {sum(elf_calories[0:3])} calories</p>")
    return response
