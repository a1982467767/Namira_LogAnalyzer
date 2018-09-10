import sys
from loganalyzer.game import Game
from loganalyzer.parser import Parser
from loganalyzer.analyzer import Analyzer 

def main():
    print("in start")
    parser = Parser(sys.argv[1])
    game = Game(parser) 
    analyzer = Analyzer(game)
    print("End")
if __name__ == "__main__":
    main()