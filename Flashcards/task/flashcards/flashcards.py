# Write your code here
import json
import sys
from os.path import exists

statistics = {}
hardest_card = {}
count_prints = []

def do_action(statistics, action, hardest_card):
    if action == "add":
        return make_card()
    if action == "remove":
        return remove()
    if action == "import":
        return import_file()
    if action == "export":
        return export_file()
    if action == "ask":
        return ask(statistics)
    if action == "exit":
        log_print("Bye bye!")
        sys.exit(0)
    if action == "log":
        return log()
    if action == "hardest card":
        return hardest_cards(hardest_card)
    if action == "reset stats":
        hardest_card.clear()

        return "Card statistics have been reset."

def log():
    fileName = log_input("File name:\n")

    with open(fileName, "w") as f:
        for count_print in count_prints:
            count_print = count_print.rstrip() + "\n"
            f.write(count_print)

    return "The log has been saved.\n"

def hardest_cards(dict_):
    lijst = []
    string = "hardest cards are "

    statistics_sorted = sorted(dict_.items(), reverse=False)

    if len(dict_) == 0:
        return "There are no cards with errors."

    if statistics_sorted.count(statistics_sorted[0]) > 1:
        for statistic_sorted in statistics_sorted:
            if statistic_sorted[1] == statistic_sorted[0][1]:
                lijst.append(statistic_sorted)

        for small_dict in lijst:
            string += small_dict.keys() + ", "

        return string[:-2]
    return f'The hardest card is "{statistics_sorted[0][0]}". You have {statistics_sorted[0][1]} errors answering it'

def import_file():
    the_file = log_input("File name:\n")

    if exists(the_file):
        with open(the_file, 'r') as f:
            dict_term2 = json.load(f)

        dict_term.update(dict_term2)

        return f"{len(dict_term2)} cards have been loaded.\n"

    return "File not found."

def export_file():
    the_file = log_input("File name:\n")

    with open(the_file, 'w') as f:
        json.dump(dict_term, f)

    return f"{len(dict_term)} cards have been saved.\n"

def remove():
    wich_card = log_input("Which card?\n")

    if wich_card in dict_term:
        defenition = dict_term.pop(wich_card)
        dict_defenition.pop(defenition)


        return "The card has been removed.\n"
    else:

        return f"Can't remove \"{wich_card}\": there is no such card.\n"

def make_card():
    term = log_input(f"The card:\n")
    while term in dict_term:
        term = log_input(f'The term "{term}" already exists. Try again:\n')

    definition = log_input(f"The definition of the card:\n")
    while definition in dict_defenition.keys():
        definition = log_input(f'The definition "{definition}" already exists. Try again:\n')

    dict_term[term] = definition
    dict_defenition[definition] = term


    return f'The pair ("{term}":"{definition}") has been added.\n'

def ask(statistics):
    how_many_times = int(log_input("How many times to ask?\n"))

    last_one = False
    aantal = 0

    for _ in range(how_many_times):
        for i, (term, definition) in enumerate(dict_term.items()):
            if i == how_many_times:
                break

            if aantal+1 == how_many_times:
                last_one = True


            definition_you = log_input(f'Print the definition of "{term}":\n')

            definition2 = None
            for key, value in dict_term.items():
                if definition_you == value:
                    definition2 = key
                    break

            aantal += 1


            if term in hardest_card.keys():
                hardest_card[term] = hardest_card[term] + 1
            else:
                hardest_card[term] = 1

            if last_one == True:
                if definition_you == definition:
                    return "Correct!\n"
                else:
                    if definition2 != None:
                        return f'Wrong. The right answer is "{definition}", but your definition is correct for "{definition2}".\n'
                    else:
                        return f'Wrong. The right answer is "{definition}".\n'
            else:
                if definition_you == definition:
                    log_print("Correct!")
                else:
                    if definition2 != None:
                        log_print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{definition2}".')
                    else:
                        log_print(f'Wrong. The right answer is "{definition}".')

def log_print(message):
    count_prints.append(message)
    
    print(message)

def log_input(message):
    the_input = input(message)

    count_prints.append(message)
    count_prints.append(the_input)

    return the_input


dict_term, dict_defenition = {}, {}
while True:
    action = log_input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
    do_the_action = do_action(statistics, action, hardest_card)

    log_print(do_the_action)
