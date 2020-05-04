import numpy as np

class env:
    def __init__(self):
        self.min_card, self.max_card = 1, 10
        self.max_dealer = 17
        self.min_game, self.max_game = 0, 21

    def actionSpace(self):
        return (0, 1)

    def startGame(self):
        card1 = np.random.randint(self.min_card, self.max_card + 1)
        card2 = np.random.randint(self.min_card, self.max_card + 1)
        return (card1, card2)

    def draw(self):
        value = np.random.randint(self.min_card, self.max_card)
        
        if np.random.random() <= 1/3:
            return -value
        else:
            return value
    
    def step(self, player_value, dealer_value, action):
        if action == 0:
            player_value += self.draw()

            #check if player went bust
            if not (self.min_game < player_value <= self.max_game):
                reward = -1
                terminated = True
            
            else:
                reward = 0
                terminated = False

        elif action == 1:
            terminated = True
            
            #dealer takes turns now
            while (self.min_game < dealer_value < self.max_dealer):
                dealer_value += self.draw()
            
            #check for the delaer going bust
            if not (self.min_game < dealer_value <= self.max_game):
                reward = 1
            
            elif (player_value > dealer_value):
                reward = 1
            
            elif (player_value == dealer_value):
                reward = 0

            elif (player_value < dealer_value):
                reward = -1
        
        return (player_value, dealer_value, reward, terminated)


e = env()
print(e.step(12, 12, 0))