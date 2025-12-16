import requests

from plotly.graph_objs import Bar
from plotly import offline

# создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3 +json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# сохранение API в переменной.
response_dict = r.json()
print(f'Total repositories: {response_dict['total_count']}')

# анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')
repo_names, stars = [], []

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# построение визуализации
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 2.5, 'color': 'rgb(25,25,250)'}
    },
    'opacity': 0.6
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'font': {'family':'Brush Script MT','size': 28,'color':'green',},

    'xaxis': {'title': {
        'text':'Repository',
        'font':{'family':'Brush Script MT','size': 24,'color':'red'}},
        'tickfont': {'family':'Times New Roman','size': 10}},
    'yaxis': {'title': {
        'text':'Stars',
        'font':{'family':'Times New Roman','size': 24,'color':'black'}},
        'tickfont': {'size': 16,'color':'black'}},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
