file = open('MultTable.html','w')
file.write('''<html>
	<head>
		<title>Multiplication Table</title>
		<style>
			table{
				top:50%; 
				left:50%; 
				position:absolute; 
				margin-top:-260px; 
				margin-left:-270px;
			}
			td{
				padding: 15px; 
				text-align: center
			}
			th{
				font-size: 20px
			}
			.bold{
				font-weight: bold; 
				font-size: 20px
			}
		</style>
	</head>
	<body>
		<table border="1px";>
			<thead>
				<tr>
					<th colspan="10">
						Multiplication Table 
					</th>
				</tr>
			</thead>
			<tbody>
				<tr>''')

s = ''	

for i in range(1, 11):
	s += '          <td class="bold">' + str(i) + '</td>\n'
s += '          </tr>\n\n'

for i in range(2, 11):
  s += '        <tr>\n  <td class="bold">' + str(i) + '         </td>\n'
  for j in range(2, 11):
    s += '          <td>' + (str) (i*j) + '</td>\n'
  s += '        </tr>\n\n'

s += '''</table>
		</tbody>
	</body>
</html>'''

file.write(s)
file.close

