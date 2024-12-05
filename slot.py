import random

class SlotAI:
    def __init__(self):
        # Defining the outcomes and their probabilities.
        self.outcomes = {
            "Token Burn": {"probability": 0.10},
            "Small Buy": {"probability": 0.10},
            "Big Buy": {"probability": 0.075},
            "Airdrop": {"probability": 0.05},
            "Charity Donation": {"probability": 0.05},
            "Jackpot": {"probability": 0.001},
            "No Win": {"probability": 0.624}
        }
        # Normalize probabilities and generate ranges for weighted outcomes
        self.probability_ranges = self._generate_probability_ranges()

    def _generate_probability_ranges(self):
        """Generates cumulative ranges based on the probability weights."""
        ranges = []
        cumulative = 0
        for outcome, data in self.outcomes.items():
            cumulative += data["probability"]
            ranges.append((cumulative, outcome))
        return ranges

    def spin(self):
        rand = random.random()  # Generate a random float between 0 and 1
        for cumulative, outcome in self.probability_ranges:
            if rand <= cumulative:
                return outcome
        return "LOSE"  # Default to 'LOSE' in case of unexpected input

    def play(self, spins=1):

        total_reward = 0
        results = []
        
        for _ in range(spins):
            outcome = self.spin()
            reward = self.outcomes[outcome]["reward"]
            total_reward += reward
            results.append((outcome, reward))
        
        return results, total_reward


def main():
    
    slot_ai = SlotAI()
    while True:
        try:
            spins = int(input("Number of spins: "))
            if spins <= 0:
                print("Thanks for playing SlotAI! Goodbye!")
                break
            
            results, total_reward = slot_ai.play(spins)
            print("\nResults:")
            for i, (outcome, reward) in enumerate(results, start=1):
                print(f"Spin {i}: {outcome} - Reward: {reward} tokens")
            
            print(f"\nTotal reward: {total_reward} tokens\n")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
