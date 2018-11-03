# Namira LogAnalyzer
Python Script for parsing and analyzing agent2D socer simulation rcl and rcg logs. This project has been used in [NAMIRA TPAS](https://github.com/Farzin-Negahbani/Namira_TPAS)
a Tournament Planning and Analyzer Software.

## Getting Started

You just need python 3.x! running on any OS. You can download and install python 3.x from [here](https://www.python.org/downloads/).
### Installation
    python ./setup.py install
<!-- ### Uninstallation
    python ./setup.py uninstall -->
### How To Use?
## Capabilities of this analyzer

This analyzer could report many match facts, a list of them are as follows
- Pass count 
  - Individually for each player
  - In any self-defined reigon of the playing ground
  - Pass efficiency of team
- Shoot count
  - Individually for each player
  - Shoot efficiency of team
- Possesion 
  - In any desired reigon of the playing ground
  - Possesion on defined reigons
- Kick count
- Tackle count
- say count
### How to Use
#### As a Script
    loganalyzer --path <log file without .rcl or .rcg >
#### As a Module
    import loganalyzer
    from loganalyzer import Parser
    from loganalyzer import Game
    from loganalyzer import Analyzer
    parser = Parser('path to log file without .rcl or .rcg')
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()
    left_team_pass = analyzer.pass_l 
    left_team_in_target_shoot = analyzer.in_target_shoot_l 
    left_team_agent_1 = game.left_team.agents[0].data 
## Authors

* **[Farzin Negahbani](https://github.com/Farzin-Negahbani)** 
* **[Shahryar Bahmai](https://github.com/shahryarbhm)**  
