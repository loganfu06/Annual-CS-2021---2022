f = open("pokedex_materials/pokemon.csv", "r")
pokemonRaw = f.read()
f.close()
pokeList = pokemonRaw.strip().split("\n")
pokeData = []
for i in pokeList:
    pokeData += [i.split(",")]


html = '<!DOCTYPE html> <html> <head> <meta charset="utf-8"> \n'
html += '''
<style>
body {
    text-align: center;
    margin-left: 500px;
    margin-right: 500px;
    background-color: #bf043f;
    font-family: verdana;
}
img {
    display: block; width: 100%;
}
.dex {
    margin-left: auto;
    margin-right: auto;
    background-color: #e8d8d8;
}

nav li {
   display: inline-block;
   position: relative;
}
nav li ul {
   display: none;      
   position: absolute;
   width: 100px;
   top: 100%;
   padding: 0;
}
nav li:hover > ul {  
   display: block;
}
nav a {
}
'''
html += '</style>'
html += '<title> Pokedex </title> </head> \n'
html += "<body> <h1> Made by: Logan Fu Period 9 </h1>\n"
html += "<p1> I have fond memories of Pokemon when growing up. Technically my first Pokemon game was Gen 4, but I couldn't find some clowns and abandoned the game. My favorite Pokemon game, and my first completed game, would be Gen 5, and I have basically completed all the subsequent games after Gen 5. Right now, I am not very enthusiastic about Pokemon, and prefer Fire Emblem.  </p1> <br> \n"
html += "<br>"



#create colors

#create pages

def generatePages():
    for i in pokeData:
        page = '<!DOCTYPE html> <html> <head> <meta charset="utf-8"> \n'
        page += '<title> {}. {} </title> \n'.format(i[0], i[1])
        page += '''
<style>
body {
    text-align: center;
    margin-left: 500px;
    margin-right: 500px;
    background-color: #bf043f;
    font-family: verdana;
}
table {
    margin-left: auto;
    margin-right: auto;
    background-color: #e8d8d8;
}
nav li {
   display: inline-block;
   position: relative;
}
nav li ul {
   display: none;      
   position: absolute;
   width: 100px;
   top: 100%;
   padding: 0;
}
nav li:hover > ul {  
   display: block;
}
nav a {
}
</style>
'''
        page += '</head> <body> <h1> {} </h1> \n'.format(i[1])
        page += '''
<nav>
<ul>
<li> <a href="allpokemon.html"> Pokedex </a> </li>
'''
        page += '<li> <a href="pokemon_"> Test </a> </li>'
        page += '<li> <a href="#test"> Test </a> </li>'
        page += '''
</ul>
</nav>
'''
        page += '<p1> {} </p1> <br> <br>\n'.format(i[14].replace(";", ","))
        page += '<table border = "1"> \n'
        page += '<tr> <td colspan = "2"> <img width = 100% src="pokedex_materials/img/front/{}.png"> </td> </tr>'.format(i[0])
        page += '<tr> <td> Total </td> <td> {} </td> </tr> \n'.format(i[4])
        page += '<tr> <td> HP </td> <td> {} </td> </tr> \n'.format(i[5])
        page += '<tr> <td> Attack </td> <td> {} </td> </tr> \n'.format(i[6])
        page += '<tr> <td> Defense </td> <td> {} </td> </tr> \n'.format(i[7])
        page += '<tr> <td> Sp. Atk </td> <td> {} </td> </tr> \n'.format(i[8])
        page += '<tr> <td> Sp. Def </td> <td> {} </td> </tr> \n'.format(i[9])
        page += '<tr> <td> Speed </td> <td> {} </td> </tr> \n'.format(i[10])
        page += '</table>'
        f = open('pokemon_{}.html'.format(i[0]), "w")
        f.write(page)
        f.close()

generatePages()

#create main page
html += '<table class = "dex" border = "1"> \n'
html += '<tr><td> </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> </tr> \n'.format(pokeData[0][0],pokeData[0][1],pokeData[0][2],pokeData[0][3])
for i in range(len(pokeData[1:])):
    html += '''<tr><td> <img width = "48px" src="pokedex_materials/img/front/{}.png" onmouseout="this.src='pokedex_materials/img/front/{}.png';" onmouseover="this.src='pokedex_materials/img/back/{}.png';"></td> <td> {} </td> <td> <a href="pokemon_{}.html"> {} </a> </td> <td> {} </td> <td> {} </td> </tr> \n'''.format(pokeData[i+1][0],pokeData[i+1][0],pokeData[i+1][0],pokeData[i+1][0],pokeData[i+1][0],pokeData[i+1][1],pokeData[i+1][2],pokeData[i+1][3])

html += '</table> </body> </html>'

f = open("allpokemon.html", "w")
f.write(html)
f.close()