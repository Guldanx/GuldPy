import sys

END_OF_ACTIVITY = ['exit', 'stop', 'quit', 'stop running']
CONFIRMATION = ['yes', 'of course', 'indeed', 'completely', 'exactly', 'without a doubt', 'definitely']
REFUSAL = ['no', 'not at all', 'definitely not']

KNOWLEDGE = END_OF_ACTIVITY + CONFIRMATION + REFUSAL

def main():
    print('I am running, but not living.')
    while True:
        print("Waiting for next entry ...")
        entry = get_input()
        if understand(entry):
            action = respond_to(entry)
            if action == 'end_activity':
                break
        else:
            print("I don't get it.")
    print('I am stopping, but not dying.')
    return True

def get_input():
    return input('> ').lower()

def understand(entry):
    if entry in KNOWLEDGE:
        return True
    return False

def respond_to(entry):
    action = ""
    if entry in END_OF_ACTIVITY and give_confirmation():
        action = 'end_activity'
    elif entry in CONFIRMATION + REFUSAL:
        print("'" + entry + "' what ?")

    return action

def give_confirmation():
    print('Are you sure ?')
    while True:
        entry = get_input()
        if understand(entry):
            if is_confirmation(entry):
                return True
            elif is_refusal(entry):
                return False
            else:
                print('It is irrelevant.')
        else:
            print("I don't get it.")

def is_confirmation(entry):
    return entry in CONFIRMATION

def is_refusal(entry):
    return entry in REFUSAL

if __name__ == '__main__':
    main()