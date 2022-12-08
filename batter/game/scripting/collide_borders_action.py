from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        # over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
            stat_1 = cast.get_actor_slot(STATS_GROUP, PLAYER1_SLOT)
            stat_1.add_points(PLAYER_SCORE_INC)

        elif y > (FIELD_BOTTOM):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
            stat_2 = cast.get_actor_slot(STATS_GROUP, PLAYER2_SLOT)
            stat_2.add_points(PLAYER_SCORE_INC)
            
            # if stat_2.get_lives() > 0:
            #     callback.on_next(TRY_AGAIN) 
            # else:
            #     callback.on_next(GAME_OVER)
            #     self._audio_service.play_sound(over_sound)