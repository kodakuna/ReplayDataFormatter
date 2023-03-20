import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('replay-reader-114bb6fbd9ea.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Test Data')

# create dictionary of showdown usernames and team abbreviations
nameToTeamAbb = {'davo2544': 'BEX', 'theelkspeaks': 'BLL', 'Rocker19304': 'BUF', 'fart': 'CKC',
                 'Craisans': 'CLZ', 'kodakuna': 'COC', 'gannon233': 'CRA', 'DeoxysDEnjoyer': 'DEO',
                 'Killerdroid1230': 'GRE', 'Ash100985': 'LAL', 'jammont3': 'MEM', 'notlukey': 'MIL',
                 'TonyEatWorld': 'NSH', 'Speesquack': 'OAP', 'Thermql': 'RCH', 'dumbbithatwrites': 'SDS',
                 'shadowclause': 'SKG', 'Krbreb': 'TMC', 'lampentelectrabuzz': 'TUS', 'Bluey444': 'VER'}

# define the row length
rowLength = 9

# decide if the sides should be flipped so that the hometeam is on the left
flip = True

# open and read the file contents
f = open("input.txt", "r")

text = f.read()

# split input by whitespace
tokens = text.split()

# read values for team 1
coach1 = tokens[1]

# get the first team abbreviation
abb1 = nameToTeamAbb.get(coach1)

teamAbb1 = [abb1, abb1, abb1, abb1, abb1, abb1]

# find the start of the first players data
i = 1

while tokens[i] != "SP":
    i += 1

i += 1
pokemon1 = ["", "", "", "", "", ""]

j = 0
while j < 6:
    if tokens[i + j * rowLength] == "Tapu" or tokens[i + j * rowLength] == "Mr." or tokens[i + j * rowLength] == "Mime":
        pokemon1[j] = tokens[i + j * rowLength] + " " + tokens[i + 1 + j * rowLength]
        i += 1
    else:
        pokemon1[j] = tokens[i + j * rowLength]
    j += 1

i += 1

hp1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
       tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

kills1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
          tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

deaths1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
           tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 2

luck1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
         tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

dealt1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
          tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

healed1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
           tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

support1 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
            tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

taken = [0, 0, 0, 0, 0, 0]
j = 0

while j < 6:
    numericalHp = hp1[j].removeprefix("(").removesuffix("/100)")
    taken[j] = 100 - int(numericalHp) + int(healed1[j])
    j += 1

taken1 = [taken[0], taken[1], taken[2], taken[3], taken[4], taken[5]]

while tokens[i] != "Coach:":
    i += 1

coach2 = tokens[i + 1]

abb2 = nameToTeamAbb.get(coach2)

teamAbb2 = [abb2, abb2, abb2, abb2, abb2, abb2]

while tokens[i] != "SP":
    i += 1

i += 1

pokemon2 = ["", "", "", "", "", ""]
j = 0
while j < 6:
    if tokens[i + j * rowLength] == "Tapu" or tokens[i + j * rowLength] == "Mr." or tokens[i + j * rowLength] == "Mime":
        pokemon2[j] = tokens[i + j * rowLength] + " " + tokens[i + 1 + j * rowLength]
        i += 1
    else:
        pokemon2[j] = tokens[i + j * rowLength]
    j += 1

i += 1

hp2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
       tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

kills2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
          tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

deaths2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
           tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 2

luck2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
         tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

dealt2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
          tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

healed2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
           tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

i += 1

support2 = [tokens[i], tokens[i + rowLength], tokens[i + 2 * rowLength],
            tokens[i + 3 * rowLength], tokens[i + 4 * rowLength], tokens[i + 5 * rowLength]]

taken = [0, 0, 0, 0, 0, 0]
j = 0

while j < 6:
    numericalHp = hp2[j].removeprefix("(").removesuffix("/100)")
    taken[j] = 100 - int(numericalHp) + int(healed2[j])
    j += 1

taken2 = [taken[0], taken[1], taken[2], taken[3], taken[4], taken[5]]

data = [pokemon1, teamAbb1, [], kills1, deaths1, [], dealt1, taken1, healed1, luck1, support1, [],
        support2, luck2, healed2, taken2, dealt2, [], deaths2, kills2, [], teamAbb2, pokemon2]

# add a sheet with 6 rows and 23 columns
sheet_pokemon = sheet.add_worksheet(rows=6, cols=23, title=f"{coach1} vs {coach2}")

if flip:
    data.reverse()

# write to that sheet
sheet_pokemon.insert_cols(data)
