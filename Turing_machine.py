def turing_machine(tape):
    rows, cols = len(tape), 126 - 32 + 1
    transition_table = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for state in range(len(tape)):
        current_tape = tape[0:state+1]
        for symbol in range(32, 126):

            if state + 1 < len(tape) and chr(symbol) == tape[state + 1]:
                transition_table[state][symbol - 32] = state + 1
                continue

            current_sub_tape = current_tape[1:] + chr(symbol)
       
            k = 0
            while (k < len(current_sub_tape) and
                   not current_sub_tape[k:len(current_sub_tape)] == current_tape[0:len(current_tape) - k]):
                k += 1

            transition_table[state][symbol - 32] = len(current_sub_tape) - 1 - k

    return transition_table

def count_occurrence(tape, pattern):
    count = 0
    state = -1
    transition_table = turing_machine(pattern)
    tape_list = list(tape)
    pattern_list = list(pattern)
    for i in range(len(tape)):
        if state == -1 and not tape_list[i] == pattern_list[0]:
            continue

        if state == -1:
            state = 0
        else:
            symbol = ord(tape_list[i])
            state = transition_table[state][symbol - 32]

        if state == len(pattern) - 1:
            count += 1
    return count

if __name__ == '__main__':
    tape = open("tape.txt").read().strip()
    pattern = open("pattern.txt").read().strip()
  
    count = count_occurrence(tape, pattern)
    
    print(count," occurrences of the pattern in the tape.")
