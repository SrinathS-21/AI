import random

class WumpusWorld:
    def __init__(self):
        self.size = 4
        self.world = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.agent_pos = (0, 0)
        self.arrow = True
        self.gold_collected = False
        self.place_elements()

    def place_elements(self):
        # Place pits
        for _ in range(3):
            self.place_random('P')
        # Place Wumpus
        self.place_random('W')
        # Place Gold
        self.place_random('G')
        # Add percepts around Pits (Breeze) and Wumpus (Stench)
        self.add_percepts()

    def place_random(self, element):
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.world[row][col] == '' and (row, col) != (0, 0):
                self.world[row][col] = element
                break

    def add_percepts(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.world[row][col] == 'P':
                    self.add_adjacent_percept(row, col, 'B')
                elif self.world[row][col] == 'W':
                    self.add_adjacent_percept(row, col, 'S')

    def add_adjacent_percept(self, row, col, percept):
        for r, c in self.get_adjacent_cells(row, col):
            if self.world[r][c] == '':
                self.world[r][c] = percept
            elif self.world[r][c] not in ['P', 'W', 'G']:
                self.world[r][c] += percept

    def get_adjacent_cells(self, row, col):
        adjacent = []
        if row > 0: adjacent.append((row - 1, col))
        if row < self.size - 1: adjacent.append((row + 1, col))
        if col > 0: adjacent.append((row, col - 1))
        if col < self.size - 1: adjacent.append((row, col + 1))
        return adjacent

    def print_world(self):
        for row in self.world:
            print(row)

    def move_agent(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            print("Invalid move. Try again.")
            return False

        self.agent_pos = (row, col)
        cell = self.world[row][col]

        if 'P' in cell:
            if self.gold_collected:
                print("You were really close but unfortunately you failed!!! Try next time")
            else:
                print("Game over! Sorry, try next time!!!")
            return True

        if 'W' in cell:
            if self.gold_collected:
                print("You were really close but unfortunately you failed!!! Try next time")
            else:
                print("Game over! Sorry, try next time!!!")
            return True

        if 'G' in cell:
            self.gold_collected = True
            print("You found gold!")
            print("You have unlocked next level, move back to your initial position.")
            self.world[row][col] = self.world[row][col].replace('G', '')

        if 'S' in cell:
            print("You came across a stench")
        if 'B' in cell:
            print("You feel a breeze")

        if self.gold_collected and self.agent_pos == (0, 0):
            print("You won!!!")
            return True

        return False

    def get_possible_moves(self):
        row, col = self.agent_pos
        moves = self.get_adjacent_cells(row, col)
        return moves

def main():
    game = WumpusWorld()
    print("Initially agent is at 0,0")
    while True:
        possible_moves = game.get_possible_moves()
        for move in possible_moves:
            print(f"You can go to {move[0]} {move[1]}")

        try:
            row = int(input("Enter input for row: "))
            col = int(input("Enter input for column: "))
        except ValueError:
            print("Invalid input. Please enter integer values.")
            continue

        print(f"Now the agent is at {row},{col}")
        if game.move_agent(row, col):
            break

if __name__ == "__main__":
    main()
