class StateMachine:
    def __init__(self):
        self.current_state = "locked"

    def process_event(self, event):
        if self.current_state == "locked":
            if event == "2":
                self.current_state = "waiting for input of 2nd digit"
                print("Transitioned from locked to waiting for input of 2nd digit")
            else:
                print(f"Invalid event {event} from state {self.current_state}")
        elif self.current_state == "waiting for input of 2nd digit":
            if event == "5":
                self.current_state = "waiting for input of 3rd digit"
                print("Transitioned from waiting for input of 2nd digit to waiting for input of 3rd digit")
            else:
                print(f"Invalid event {event} from state {self.current_state}")
        elif self.current_state == "waiting for input of 3rd digit":
            if event == "9":
                self.current_state = "unlocked"
                print("Transitioned from waiting for input of 3rd digit to unlocked")
            else:
                print(f"Invalid event {event} from state {self.current_state}")
        else:
            print(f"Invalid event {event} from state {self.current_state}")
 


# Example usage
if __name__ == "__main__":
    sm = StateMachine()
    events = ["2", "5", "9"]

    for event in events:
        print(f"Input: {event}")
        sm.process_event(event)
