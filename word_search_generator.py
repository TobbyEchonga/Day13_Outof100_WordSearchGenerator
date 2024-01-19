import random

class WordSearchGenerator:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def generate_word_search(self):
        # Place words randomly in the grid
        for word in self.words:
            self.place_word(word)

        # Fill remaining spaces with random letters
        self.fill_grid()

        # Display the word search
        self.display_grid()

    def place_word(self, word):
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])
        if direction == 'horizontal':
            self.place_horizontal(word)
        elif direction == 'vertical':
            self.place_vertical(word)
        elif direction == 'diagonal':
            self.place_diagonal(word)

    def place_horizontal(self, word):
        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - len(word))
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]

    def place_vertical(self, word):
        row = random.randint(0, self.size - len(word))
        col = random.randint(0, self.size - 1)
        for i in range(len(word)):
            self.grid[row + i][col] = word[i]

    def place_diagonal(self, word):
        row = random.randint(0, self.size - len(word))
        col = random.randint(0, self.size - len(word))
        for i in range(len(word)):
            self.grid[row + i][col + i] = word[i]

    def fill_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == ' ':
                    self.grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

# Example Usage
if __name__ == "__main__":
    word_search = WordSearchGenerator(size=10)
    word_search.add_word("PYTHON")
    word_search.add_word("JAVA")
    word_search.add_word("C++")
    word_search.add_word("HTML")
    word_search.generate_word_search()
