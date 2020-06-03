from pynput import keyboard
from Board import Board
import testpygame
from testpygame import screen, newfont, drawboxes

b = Board()
#testpygame.init()

def main():
    b.shuffle()
    b.refresh()
    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

def on_press(key):
    b.refresh()

def on_release(key):
    #print('{0} released'.format(
    #    key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key == keyboard.Key.up:
        b.board, b.e_loc = b.move_up(b.board, b.e_loc)
        #drawboxes(b.e_loc, b.board,screen,newfont)
    elif key == keyboard.Key.down:
        b.board, b.e_loc = b.move_down(b.board, b.e_loc)
        #drawboxes(b.e_loc, b.board,screen,newfont)
    elif key == keyboard.Key.left:
        b.board, b.e_loc = b.move_left(b.board, b.e_loc)
        #drawboxes(b.e_loc, b.board,screen,newfont)
    elif key == keyboard.Key.right:
        b.board, b.e_loc = b.move_right(b.board, b.e_loc)
        #drawboxes(b.e_loc, b.board,screen,newfont)
    elif key == keyboard.Key.shift:
        b.solve()

    #stops listener if game is solved
    return b.refresh()






if __name__ == '__main__':
    main()