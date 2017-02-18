from __future__ import division

"""This file contains all the information of the army"""
army = {}
content = open('army.csv').readlines()
for i, c in enumerate(content):
    if i == 0: continue
    line = c.split(',')
    if line[0] not in army.keys(): army[line[0]] = {}
    if line[1] not in army[line[0]].keys(): army[line[0]][line[1]] = {}
    print i+1, line
    army[line[0]][line[1]]['Damage per Second'] = float(line[2])
    army[line[0]][line[1]]['Damage per Attack'] = float(line[3])
    army[line[0]][line[1]]['Hitpoints'] = float(line[4])
    army[line[0]][line[1]]['Training Cost'] = float(line[5])
    army[line[0]][line[1]]['TrainingTime'] = float(line[9])

for key in army:
    for level in army[key]:
        print key,  army[key][level]