def main():
    print_header()
    game_loop()

def print_header():
    print('--------------------------------------------')
    print('          WIZARD GAME')
    print('--------------------------------------------')
    print()

def game_loop():
    while true:

        cmd = imput('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, exiting game... bye!')
            break

if __name__ == '__main__':
    main()