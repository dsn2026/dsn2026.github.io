#from the csv file which has columns first, last, email, affiliation, country,
#create html table in the format:
#<tr>
#<td>first last</td>
#<td>affiliation</td>
#<td>country</td>
#</tr>

import csv

with open('pcmembers.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

with open('pc_members.html', 'w') as f:
    f.write('<table>\n')
    for row in your_list:
        f.write('<tr>\n')
        f.write('<td>' + row[0] + ' ' + row[1] + '</td>\n')
        f.write('<td>' + row[3] + '</td>\n')
        f.write('<td>' + row[4] + '</td>\n')
        f.write('</tr>\n')
    f.write('</table>\n')

