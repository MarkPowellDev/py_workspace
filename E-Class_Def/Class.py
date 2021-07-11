

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck() # donald is an object
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()