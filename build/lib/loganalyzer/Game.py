from loganalyzer.Team import Team

class Game:
    
    def __init__(self, parser):
        self.parser = parser
        self.right_goal   = 0
        self.left_goal    = 0
        self.server_prama = {}
        self.right_team   = Team(parser.right_team,'r')
        self.left_team   = Team(parser.left_team,'l')
        self.agent_types  = {}
        self.play_modes   = {}
        self.ball_pos    = {}
        self.set_teams_data()
        ##'''playerTypes[i]={'stamina':,...}'''
        
    def set_play_modes(self,cycle,playMode):
        self.play_modes[cycle]=playMode
        
    def set_ball_position(self,cycle,ball_data):
        self.ball_pos[cycle]={'x':ball_data[1],'y':ball_data[2],'Vx':ball_data[3],'Vy':ball_data[4]}
        
    def set_teams_data(self):
        
        for cycle in self.parser.data_rcg:
            if cycle[0][0]=='show':
                self.set_ball_position(cycle[0][1],cycle[0][2])
                self.left_team.set_agents_data(cycle[0],self)
                self.right_team.set_agents_data(cycle[0],self)
            elif cycle[0][0]=='playmode':
                self.set_play_modes(cycle[0][1],cycle[0][2])
            elif cycle[0][0]=='server_param':
                for i in range(1,len(cycle[0])):
                    self.server_prama[cycle[0][i][0]]=cycle[0][i][1]
            elif cycle[0][0]=='player_type':
                data={}
                for i in range(2,len(cycle[0])):
                    data[cycle[0][i][0]]=cycle[0][i][1]
                self.agent_types[cycle[0][1][1]]=data
                
    def get_agent_data(self,side,number):
        
        if side == 'l':
            return self.left_team.agents[number-1].get_data()
        else:
            return self.right_team.agents[number-1].get_data()
        
        
#    def get_last_kickers(self, cycle):
#        m = 0
#        kickers = []
#        for agent in (self.left_team.agents+self.right_team.agents):
#            if(agent.data[cycle]['last_tackle_cycle']>m ):
#                m=agent.data[cycle]['last_tackle_cycle']
#                kickers.clear()
#                kickers.append(agent)
#            
#            elif(agent.data[cycle]['last_tackle_cycle'] == m):
#                kickers.append(agent)
#            
#            if(agent.data[cycle]['lastkickCycle']>m ):
#                m=agent.data[cycle]['lastkickCycle']
#                kickers.clear()
#                kickers.append(agent)
#                
#            elif(agent.data[cycle]['lastkickCycle'] == m):
#                kickers.append(agent)
#                
#        return kickers   
            
#        
            
    def get_kickers(self, cycle):
        kickers = []
        for agent in self.left_team.agents+self.right_team.agents :
            if( agent.data[cycle]['is_tackled'] or agent.data[cycle]['is_kicked']):
                kickers.append(agent)
        return kickers   
                
    
    def get_last_kickers(self, cycle):
        m = 0
        kickers = []
        for agent in (self.left_team.agents+self.right_team.agents):
            if cycle in agent.data:
                if(agent.data[cycle]['last_tackle_cycle']>m or agent.data[cycle]['lastkickCycle']>m ):
                    if(agent.data[cycle]['last_tackle_cycle'] > agent.data[cycle]['lastkickCycle']):
                        m=agent.data[cycle]['last_tackle_cycle']
                    else:
                        m=agent.data[cycle]['lastkickCycle']
                    kickers.clear()
                    kickers.append(agent)

                elif(agent.data[cycle]['last_tackle_cycle'] == m or agent.data[cycle]['lastkickCycle'] == m):
                    kickers.append(agent)
            else:
                print(cycle)

        return kickers   
    
    def get_play_on_cycles(self):
        play_on_cycles = []
        cycles = list(self.play_modes.keys())
        for i in range(len(cycles)):
            if(self.play_modes[cycles[i]] == 'play_on'):
                play_on_cycles+=range(cycles[i],cycles[i+1])
        return play_on_cycles
    