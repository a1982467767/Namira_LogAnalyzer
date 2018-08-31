from game.game import Game
from parser.parser import Parser
from analyzer import Analyzer 
import sys

parser = Parser(sys.argv[1])
game = Game(parser) 
analyzer = Analyzer(game)