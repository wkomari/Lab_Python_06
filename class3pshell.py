Python 2.7.2+ (default, Oct  4 2011, 20:03:08) 
[GCC 4.6.1] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> Fenando = Player('Fenando','Torres')
>>> Fenando = Player('Fenando','Torres')
>>> Spain = Team('spanish','euro','grant',12)
>>> Fenando = Player('Fenando','Torres',Spain)
>>> print Fenando.team
spanish
>>> print Fenando.league

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print Fenando.league
AttributeError: Player instance has no attribute 'league'
>>> print Fenando.team.league
euro
>>> 
>>> Ronaldo= Player('Christiano','Ronaldo')
>>> Portugal = Team('portuguese','euro','grant',13)
>>> Ronaldo= Player('Christiano','Ronaldo',Portugal)
>>> print Ronaldo.team
portuguese
>>> print Ronaldo.team.manager_name
grant
>>> Portugal.add_player('Ronaldo')
>>> Portugal.players
['Ronaldo']
>>> Spain.add_player('torres')
>>> Spain.players
['torres']
>>> Spain.add_player('messi')
>>> Spain.players
['torres', 'messi']
>>> 
