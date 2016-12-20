import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Game(object):
    '''Interface for abstract strategy games.'''


    @abc.abstractmethod
    def copy(self):
        '''Returns a copy of the game'''
        pass

    @abc.abstractmethod
    def cur_player(self):
        '''
        Returns the index of the player in turn, starting with 0:
        0 (Player 1), 1 (Player 2), etc.
        '''
        pass

    def is_over(self):
        '''Returns true if the game is over.'''
        return len(self.legal_moves()) == 0

    @abc.abstractmethod
    def legal_moves(self):
        '''
        Returns a list of legal moves for the player in turn.
        The move representation is game-specific.
        '''
        pass

    @abc.abstractmethod
    def make_move(self, move):
        '''Makes one move for the player in turn. Returns self.'''
        pass

    def make_moves(self, *moves):
        '''Makes a series of moves. Returns self.'''
        for move in moves:
            self.make_move(move)
        return self

    @abc.abstractmethod
    def outcomes(self):
        '''
        Returns a list of outcomes for each player at the end of the game.
        '''
        pass

    def outcome(self, player_idx):
        '''Returns the outcome for the given player'''
        return self.outcomes()[player_idx]

    @abc.abstractmethod
    def reset(self):
        '''Restarts the game. Returns self.'''
        pass
