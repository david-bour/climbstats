"""
Export the athletes out into a text file
"""
from crawler import crawl_athletes

with open('athletes.txt', 'w') as fi:
    athletes = crawl_athletes()
    for athlete in athletes:
        fi.write(athlete + '\n')
