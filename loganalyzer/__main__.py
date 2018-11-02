import sys
import os
import argparse
from loganalyzer.Game import Game
from loganalyzer.Parser import Parser
from loganalyzer.Analyzer import Analyzer 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Input file path", required=True, dest='path')
    parser.add_argument("--save_path", help="Output saving path.", dest='save_path')
    parser.add_argument('--version', action='version', version='1.0.0')
    args = parser.parse_args()
    if args.save_path is None:
        args.save_path = args.path+".log"
    return args
def write_to_file(save_path,analyzer):
    f = open(save_path,'w')
    # self.game           = game
    # self.play_on_cycles = game.get_play_on_cycles()
    # self.pass_status    = 0 # 0 --> no kick,  1 --> one kicker detected
    # self.pass_last_kicker = -1
    # self.pass_last_kick_cycle = -1
    # self.i = 0
    
    #results
    #right TEAM
    f.writelines("Right Team"+os.linesep)
    f.writelines(analyzer.game.right_team.name+os.linesep)
    f.writelines("pass:"+str(analyzer.pass_r )+os.linesep)
    f.writelines("intercept:"+str(analyzer.intercept_r )+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_r )+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_r )+os.linesep)
    # f.writelines("possesion:"+str(analyzer.possesion_r )+os.linesep)
    # f.writelines("used_stamina:"+str(analyzer.used_stamina_r )+os.linesep)
    #left TEAM
    f.writelines(os.linesep)
    f.writelines("Left Team"+os.linesep)
    f.writelines(analyzer.game.left_team.name+os.linesep)
    f.writelines("pass:"+str(analyzer.pass_l )+os.linesep)
    f.writelines("intercept:"+str(analyzer.intercept_l )+os.linesep)
    f.writelines("on_target_shoot:"+str(analyzer.on_target_shoot_l )+os.linesep)
    f.writelines("off_target_shoot:"+str(analyzer.off_target_shoot_l )+os.linesep)
    # f.writelines("possesion:"+str(analyzer.possesion_l )+os.linesep)
    # f.writelines("used_stamina:"+str(analyzer.used_stamina_l )+os.linesep)
    f.close()
def main():
    args=parse_args()
    path = args.path
    save_path = args.save_path
    parser = Parser(path)
    game = Game(parser) 
    analyzer = Analyzer(game)
    analyzer.analyze()
    write_to_file(save_path,analyzer)
