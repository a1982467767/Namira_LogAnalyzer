import math
class Analyzer:


    def __init__(self, game):
        self.game           = game
        self.play_on_cycles = game.get_play_on_cycles()
        self.pass_status    = 0 # 0 --> no kick,  1 --> one kicker detected
        self.pass_last_kicker = -1
        self.pass_last_kick_cycle = -1
        self.i = 0

        #results
        #right TEAM
        self.pass_r = 0
        self.intercept_r = 0
        self.all_shoot_r = 0
        self.on_target_shoot_r = 0
        self.possesion_r = 0
        self.used_stamina_r = 0
        #left TEAM
        self.pass_l = 0
        self.intercept_l = 0
        self.all_shoot_l = 0
        self.on_target_shoot_l = 0
        self.possesion_l = 0
        self.used_stamina_l = 0

    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y


    def check_shoot(self, key):

        # print(self.play_on_cycles)
        if key in self.game.ball_pos:
            if(key not in self.play_on_cycles):
                self.shoot_status = 0
            elif( self.shoot_status == 0 and (self.game.ball_pos[key]['Vx']**2 + self.game.ball_pos[key]['Vy']**2)** 0.5  > 2.2 ):
                
                
                kickers = self.game.get_kickers(key)

                if(len(kickers)>0 and kickers[0].team.name == self.game.right_team.name and math.hypot(kickers[0].data[key]['x']+51.6,kickers[0].data[key]['y'] )< 20 and self.game.ball_pos[key]['Vx']   ):
                    ball1= (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2= (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    (x,y) = Analyzer.line_intersection((ball1,ball2), ((52.6,1),(52.6,0)) )
                    if(y> -12 and y< 12 ):
                        print("Shoooooooot R", key, kickers[0].number)
                        self.on_target_shoot_r +=1

                elif(len(kickers)>0 and kickers[0].team.name == self.game.left_team.name and  math.hypot(kickers[0].data[key]['x']-51.6,kickers[0].data[key]['y'] ) < 20 and self.game.ball_pos[key]['Vx']):
                    ball1= (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2= (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    (x,y) = Analyzer.line_intersection( (ball1,ball2), ((52.6,1),(52.6,0)) )
                    if(y> -12 and y< 12 ):
                        print("Shoooooooot L", key, kickers[0].number)
                        self.on_target_shoot_l +=1


    def check_pass(self, key):
        if len(self.game.get_last_kickers(key))>0:
            if(key not in self.play_on_cycles):
                self.pass_status = 0

            elif(self.pass_status == 0):
                self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                self.pass_last_kick_cycle = key
                self.pass_status      = 1

            elif(self.pass_status == 1 ):
                #get_last_kicker =self.game.get_last_kickers(key)
                #print('get_last_kicker')
                #print(get_last_kicker)

                if(self.pass_last_kicker == self.game.get_last_kickers(key)[0] and self.game.get_last_kickers(key)[0].data[key]['is_kicked']):
                    self.pass_status = 1
                    self.pass_last_kick_cycle = key


                elif(self.pass_last_kicker != self.game.get_last_kickers(key)[0]  and  self.pass_last_kicker.team == self.game.get_last_kickers(key)[0].team  ):
                    self.i = self.i+1
                    print(self.i," Pass Detected" , self.pass_last_kick_cycle, self.pass_last_kicker.number, self.pass_last_kicker.team.name)

                    if(self.pass_last_kicker.team.name == self.game.right_team.name):
                        self.pass_r += 1
                    else:
                        self.pass_l += 1

                    self.pass_status = 1
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key


                elif(self.pass_last_kicker.team != self.game.get_last_kickers(key)[0].team):
                    #print("Pass intercept", self.pass_last_kick_cycle, self.game.get_last_kickers(key)[0].number, self.game.get_last_kickers(key)[0].team.name)
                    if(self.game.get_last_kickers(key)[0].team.name == self.game.right_team.name):
                        self.intercept_r += 1
                    else:
                        self.intercept_l += 1
                    self.pass_status = 1
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key


    def analyze(self):
        ''' pass, shoot, pass intercept, shoot intercept, possesion ,  '''

        for key in range(1,self.play_on_cycles[-1]+1):
            self.check_pass(key)
            self.check_shoot(key)
