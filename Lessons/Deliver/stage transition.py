class AutomaticTransmission:
    def __init__(self):
        self.state = "Park"  # Initial state

    def shift_gear(self, action):
        if self.state == "Park" and action == "Release Brake":
            self.state = "Neutral"
            print("Transitioned from Park to Neutral")
        elif self.state == "Neutral":
            if action == "Shift to Drive":
                self.state = "Drive"
                print("Transitioned from Neutral to Drive")
            elif action == "Shift to Reverse":
                self.state = "Reverse"
                print("Transitioned from Neutral to Reverse")
        elif self.state == "Drive" and action == "Shift to Low Gear":
            self.state = "Low Gear"
            print("Transitioned from Drive to Low Gear")
        elif self.state in ["Reverse", "Drive", "Low Gear"] and action == "Shift to Park":
            self.state = "Park"
            print(f"Transitioned to Park from {self.state}")
        else:
            print(f"Invalid action {action} from state {self.state}")

    def current_state(self):
        return self.state


# Example usage
transmission = AutomaticTransmission()

# Simulating various actions
actions = ["Release Brake", "Shift to Drive", "Shift to Low Gear", "Shift to Park", "Shift to Reverse"]

for action in actions:
    print(f"Action: {action}")
    transmission.shift_gear(action)
    print(f"Current State: {transmission.current_state()}\n")
