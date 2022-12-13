from flask import Flask, render_template

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

    # render template with elf calories
    return render_template('index.html', elf_calories={
        'max': elf_calories[0], 'top3': sum(elf_calories[0:3])
    })
