
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,s):
        

        
        self.scores.append(s) #in the python shell, type e.g. ama=Player('ama','ludu')
                              # ama.scores
                              # ama.add_score(3)
    #def add_newteam(self,y):
     #   self.team.append(y)

    def total_score(self):
      
 
        x= sum (self.scores)
        return x
        return len (self.scores) 

    def average_score(self):
        m= len(self.scores)
        print m
        
        avgscore = sum (self.scores)/float(m)
        print avgscore
# another example
class Team:
    def __init__(self,name,league,manager_name,points):
            self.name = name
            self.league = league
            self.manager_name = manager_name
            self.points= points
            self.players= []
    def add_player(self,s):
            self.players.append(s)
    
            
            
    def __str__(self):
        x= str(self.name)
        return x
   # print x  

    #example 8
class Match:
    def __init__(self,home_team,away_team,date,home_scores,away_scores):
        self.home_team = home_team
        self.away_team = away_team
        self.date = datetime.date
        self.home_scores ={}
        self.away_scores ={}

    def home_score(self):
        x = sum(self.home_scores)
        if x == 0:
            return 0
        else:
            return x
        
    def away_scores(self):
        y = sum(self.away_scores)
        
        if y == 0:
            return 0
        else:
            return y
        
    






        #{'home_scores':'player_last_name','player_scorekey:value pairs'}
        #self.away_scores = {'away_scores':'player_last_name','player_scorekey:value pairs'}
        








'''def __init__(self,firstname,lastname,team):
    self.firstname = Fenando
    self.lastname = Torres
    self.team = Spain
def __init_(self,firstname,lastname,team):
    self.firstname = Christiano
    self.lastname = Ronaldo
    self.team = Portugal

def __int__(self,Christiano,Ronaldo,Portugal)
'''

 
