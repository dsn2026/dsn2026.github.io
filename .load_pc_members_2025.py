#from the csv file which has columns first, last, email, affiliation, country,
#create html table in the format:
#<tr>
#<td>Name</td>
#<td>Affiliation</td>
#<td>Country</td>
#</tr>

import csv

with open('.pcmembers_2025.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

with open('pc_members.html', 'w') as f:
    f.write('<table>\n')
    for row in your_list:
        f.write('<tr>\n')
        f.write('<td>' + row[0] + '</td>\n')
        f.write('<td>' + row[1] + '</td>\n')
        f.write('<td>' + row[2] + '</td>\n')
        f.write('</tr>\n')
    f.write('</table>\n')

