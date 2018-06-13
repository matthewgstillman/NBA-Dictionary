from django.shortcuts import render, redirect
from dictionaries import team_color_dict
import urllib
import requests

# Create your views here.
def index(request):
    context={
        'team_color_dict': team_color_dict
    }
    return render(request, 'nba_dict/index.html', context)

def get_teams(request):
    teams_list = []
    team_count = 0
    for team in team_color_dict['teams']:
        teams_list.append(team.title())
        team_count += 1
    sorted_list = sorted(teams_list)
    # print sorted_list for debugging purposes
    context = {
        'teams_list': teams_list,
        'team_count': team_count,
        'sorted_list': sorted_list
    }
    return render(request, 'nba_dict/teams.html', context)

def team_and_city(request):
    city_and_team_list = []
    team_count = 0
    for team in team_color_dict['teams'].values():
        city_and_team_list.append(str(team['city']) + " " + str(team['team']))
        team_count += 1
        #Added Website line below
        # website = str(team['website'])
    sorted_city_team_list = sorted(city_and_team_list)
    context ={
        'city_and_team_list': city_and_team_list,
        'sorted_city_team_list': sorted_city_team_list,
        'team_count': team_count
        #Adding Website
        # 'website': website
    }
    return render(request, 'nba_dict/team_and_city.html', context)


def team_and_city_color(request):
    team_city_color_list = []
    for team in team_color_dict['teams'].values():
        if 'third_color' in team:
            team_city_color_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + ", " + str(team['secondary_color']) + " and " + str(team['third_color']) )
        else:
            team_city_color_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + " and " + str(team['secondary_color']))
    sorted_team_city_color_list = sorted(team_city_color_list)
    context = {
        'team_city_color_list': team_city_color_list,
        'sorted_team_city_color_list': sorted_team_city_color_list
    }
    return render(request, 'nba_dict/team_city_color.html', context)

def team_city_color_hex(request):
    team_city_colors_hex_list = []
    for team in team_color_dict['teams'].values():
        if 'third_color' in team:
            team_city_colors_hex_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + ", " + str(team['secondary_color']) + " and " + str(team['third_color']) + " (" + str(team['primary_hex']) + ", " + str(team['secondary_hex']) + ", " + str(team['third_hex']) + ")")
        else:
            team_city_colors_hex_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + " and " + str(team['secondary_color']) + " (" + str(team['primary_hex']) + ", " + str(team['secondary_hex']) + ")")    
    sorted_team_city_colors_hex_list = sorted(team_city_colors_hex_list)
    context ={
        'sorted_team_city_colors_hex_list': sorted_team_city_colors_hex_list
    }
    return render(request, 'nba_dict/team_city_color_hex.html', context)

def website(request):
    team_city_colors_hex_website_list = []
    for team in team_color_dict['teams'].values():
        if 'third_color' in team:
            team_city_colors_hex_website_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + ", " + str(team['secondary_color']) + " and " + str(team['third_color']) + " (" + str(team['primary_hex']) + ", " + str(team['secondary_hex']) + ", " + str(team['third_hex']) + ") " + str(team['website']))
            # team = str(team['team'])
            website = str(team['website'])
            print website
        else:
            team_city_colors_hex_website_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['primary_color']) + " and " + str(team['secondary_color']) + " (" + str(team['primary_hex']) + ", " + str(team['secondary_hex']) + ") " + str(team['website']))
            # team = str(team['team'])
            website = str(team['website'])
            print website
    sorted_team_city_colors_hex_website_list = sorted(team_city_colors_hex_website_list)
    context ={
        'team_city_colors_hex_website_list': team_city_colors_hex_website_list,
        'sorted_team_city_colors_hex_website_list':
        sorted_team_city_colors_hex_website_list,
        'website': website,
        # 'team': team
    }
    return render(request, 'nba_dict/website.html', context)


def team_city_conf(request):
    team_city_conf_list = []
    # east_city_conf_list = []
    # west_city_conf_list = []
    for team in team_color_dict['teams'].values():
        team_city_conf_list.append(str(team['city']) + " " + str(team['team']) + " - " + str(team['conference']).title() + " Conference")
        sorted_team_city_conf_list = sorted(team_city_conf_list)
        context = {
            'sorted_team_city_conf_list': sorted_team_city_conf_list
        }
    return render(request, 'nba_dict/team_city_conf.html', context)

def players(request):
    url = 'http://data.nba.net/10s/prod/v1/2016/players.json'
    players_list = requests.get(url).json()
    for player in players_list.values():
        print player
    # print json_data
    context ={
        'players_list': players_list
    }
    return render(request, 'nba_dict/players.html', context)