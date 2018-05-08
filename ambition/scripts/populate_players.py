import csv
from entity.sync import sync_entities
from data import teams, positions
from players.models import Player, Team, Position 


def run():
    print("importing player data now")
    
    with open('./../resources/NFL Salary Visualization - nfl_salaries.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_name = row['player'].split(' ')[0]
            last_name = row['player'].split(' ')[1]
            salary = row['salary']
            team_name = teams.teams[row['team']]
            position_name = positions.positions[row['position']]

            team = Team.objects.filter(name=team_name).first()
            if not team:
                team = Team(name=team_name, name_abbreviated=row['team'])
                team.save()


            position = Position.objects.filter(name=position_name).first()
            if not position:
                position = Position(name=position_name, name_abbreviated=row['position'])
                position.save()
            
            player = Player(
                email='{}.{}@{}.net'.format(first_name, last_name, team.name_abbreviated),
                first_name=first_name,
                password='password123',
                last_name=last_name,
                position=position,
                team=team,
                salary=int(salary))
            player.save()
    print('syncing now')
    sync_entities()
