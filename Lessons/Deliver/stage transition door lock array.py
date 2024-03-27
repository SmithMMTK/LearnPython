class StateMachine:
    def __init__(self):
        self.current_state = "locked"
        self.lock_key = ["2", "5", "9"]
        self.input_buffer = []

    def process_event(self, event):
        # Check if the current state is "locked"
        if self.current_state == "locked":
            # If the event matches any of the lock key digits
            if event in self.lock_key:
                # Add the event to the input buffer
                self.input_buffer.append(event)
                # If the input buffer matches the lock key
                if self.input_buffer == self.lock_key:
                    # Transition to the "unlocked and stopped" state
                    self.current_state = "unlocked and stopped"
                    # Clear the input buffer
                    self.input_buffer = []
                else:
                    # Otherwise, stay in the "waiting for input of 2nd digit" state
                    # if one digit has been entered, else transition back to "locked"
                    self.current_state = "waiting for input of 2nd digit" if len(self.input_buffer) == 1 else "locked"
            else:
                # If the event does not match any lock key digits, remain in the "locked" state
                self.current_state = "locked"
                # Clear the input buffer
                self.input_buffer = []

        # If the current state is "waiting for input"
        elif self.current_state.startswith("waiting for input"):
            # If the event matches any of the lock key digits
            if event in self.lock_key:
                # Add the event to the input buffer
                self.input_buffer.append(event)
                # If the input buffer matches the lock key
                if self.input_buffer == self.lock_key:
                    # Transition to the "unlocked and stopped" state
                    self.current_state = "unlocked and stopped"
                    # Clear the input buffer
                    self.input_buffer = []
                else:
                    # Otherwise, stay in the "waiting for input of next digit" state
                    self.current_state = "waiting for input of {} digit".format(len(self.input_buffer) + 1)
            else:
                # If the event does not match any lock key digits, transition back to "locked"
                self.current_state = "locked"
                # Clear the input buffer
                self.input_buffer = []

        # If the current state is "unlocked and stopped"
        elif self.current_state == "unlocked and stopped":
            # If any lock key digit is entered, transition back to "locked"
            if event in self.lock_key:
                self.current_state = "locked"
                # Clear the input buffer
                self.input_buffer = []

        # Print the event and current state for debugging purposes
        print(f"Event: {event}, Current State: {self.current_state}")



# Example usage
if __name__ == "__main__":
    sm = StateMachine()
    events = ["2", "5", "9"]

    for event in events:
        print(f"Input: {event}")
        sm.process_event(event)
