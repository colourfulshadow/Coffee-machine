class CoffeeMachine:
    states = ['choosing an action', 'buying', 'filling']

    def __init__(self):
        self.ingredients = {'water': 400,
                            'milk': 540,
                            'beans': 120,
                            'cups': 9,
                            'money': 550}
        self.state = 'choosing an action'
        self.input = None

    def __str__(self):
        return f'''The coffee machine has:
                {self.ingredients['water']} of water
                {self.ingredients['milk']} of milk
                {self.ingredients['beans']} of coffee beans
                {self.ingredients['cups']} of disposable cups
                {self.ingredients['money']} of money'''

    def read_input(self, *args):
        if self.state == 'choosing an action':
            print('Write action (buy, fill, take, remaining, exit):')
            self.input = input()
        elif self.state == 'buying':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            self.input = input()
        elif self.state == 'filling':
            try:
                print(f'Write how many (much) {args[0]} do you want to add:')
                self.input = input()
            except IndexError:
                print('IndexError')

    def operate(self):
        while True:
            self.read_input()
            if self.input == 'exit':
                break
            elif self.input == 'remaining':
                print(self)
            elif self.input == 'buy':
                self.state = 'buying'
                self.buy()
            elif self.input == 'take':
                self.take()
            elif self.input == 'fill':
                self.state = 'filling'
                self.fill()

    def take(self):
        print('I gave you $', self.ingredients['money'])
        self.ingredients['money'] = 0

    def buy(self):

        def process():
            print("Starting to make a coffee\nGrinding coffee beans\nBoiling water\n"
                  "Mixing boiled water with crushed coffee beans\nPouring coffee into the cup\n"
                  "Pouring some milk into the cup\nCoffee is ready!")

        def espresso():
            if self.ingredients['water'] < 250:
                print('Sorry, not enough water!')
            elif self.ingredients['beans'] < 16:
                print('Sorry, not enough beans!')
            else:
                self.ingredients['water'] -= 250
                self.ingredients['beans'] -= 16
                self.ingredients['money'] += 4
                self.ingredients['cups'] -= 1
                print('I have enough resources, making you a coffee!')
                process()

        def latte():
            if self.ingredients['water'] < 350:
                print('Sorry, not enough water!')
            elif self.ingredients['milk'] < 75:
                print('Sorry, not enough milk!')
            elif self.ingredients['beans'] < 20:
                print('Sorry, not enough beans!')
            else:
                self.ingredients['water'] -= 350
                self.ingredients['milk'] -= 75
                self.ingredients['beans'] -= 20
                self.ingredients['money'] += 7
                self.ingredients['cups'] -= 1
                print('I have enough resources, making you a coffee!')
                process()

        def cappuccino():
            if self.ingredients['water'] < 200:
                print('Sorry, not enough water!')
            elif self.ingredients['milk'] < 100:
                print('Sorry, not enough milk!')
            elif self.ingredients['beans'] < 12:
                print('Sorry, not enough beans!')
            else:
                self.ingredients['water'] -= 200
                self.ingredients['milk'] -= 100
                self.ingredients['beans'] -= 12
                self.ingredients['money'] += 6
                self.ingredients['cups'] -= 1
                print('I have enough resources, making you a coffee!')
                process()

        self.read_input()
        if self.input == 'back':
            pass
        elif self.ingredients['cups'] < 1:
            print('Sorry, not enough cups!')
        elif self.input == '1':
            espresso()
        elif self.input == "3":
            cappuccino()
        elif self.input == '2':
            latte()

        self.state = 'choosing an action'

    def fill(self):
        for ingr in self.ingredients:
            if ingr == 'money':
                continue
            else:
                self.read_input(ingr)
                self.ingredients[ingr] += int(self.input)
        self.state = 'choosing an action'


my_CM = CoffeeMachine()
my_CM.operate()
