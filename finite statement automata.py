class FSA:
    def __init__(self):
        self.current_state = 'q0'  # Initial state
    
    def process_input(self, input_string):
        for char in input_string:
            if self.current_state == 'q0':
                if char == 'a':
                    self.current_state = 'q1'
            elif self.current_state == 'q1':
                if char == 'b':
                    self.current_state = 'q2'
                elif char == 'a':
                    # Stay in the same state if 'a' is encountered again
                    pass
                else:
                    # Reset to initial state for any other character
                    self.current_state = 'q0'
            else:
                # Invalid state, reset to initial state
                self.current_state = 'q0'
        return self.current_state == 'q2'


# Example usage
automaton = FSA()

# Test strings
test_strings = ['aab', 'abcab', 'defab', 'ab']

for string in test_strings:
    is_accepted = automaton.process_input(string)
    if is_accepted:
        print(f'String "{string}" is accepted.')
    else:
        print(f'String "{string}" is not accepted.')
