import logic_game

if __name__ == '__main__':
    mat = logic_game.start_game()

while(True):
    x = input("Silakan Masukkan Arah: ")
    if (x == 'W' | x == 'w'):
        mat, flag = logic_game.move_up(mat)
        status = logic_game.get_current_state(mat)
        print(status)
        
        if (status == 'Game Not Over'):
            logic_game.add_new_2(mat)
        else:
            break
    elif (x == 'A' | x == 'a'):
        mat, flag = logic_game.move_left(mat)
        status = logic_game.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic_game.add_new_2(mat)
        else:
            break
    elif (x == 'S' | x == 's'):
        mat, flag = logic_game.move_down(mat)
        status = logic_game.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic_game.add_new_2(mat)
        else:
            break
    elif (x == 'D' | x == 'd'):
        mat, flag = logic_game.move_right(mat)
        status = logic_game.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic_game.add_new_2(mat)
        else:
            break
    else:
        print("Arah yang kamu masukkan tidak sesuai!!!")
    print(mat)