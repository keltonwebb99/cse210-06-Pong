from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket1 = cast.get_actor_slot(RACKET_GROUP, PLAYER1_SLOT)
        racket2 = cast.get_actor_slot(RACKET_GROUP, PLAYER2_SLOT)
        if self._keyboard_service.is_key_down(PLAYER2_LEFT): 
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(PLAYER2_RIGHT): 
            racket2.swing_right()  
        else: 
            racket2.stop_moving()   

        if self._keyboard_service.is_key_down(PLAYER1_LEFT): 
            racket1.swing_left()
        elif self._keyboard_service.is_key_down(PLAYER1_RIGHT): 
            racket1.swing_right()  
        else: 
            racket1.stop_moving()         