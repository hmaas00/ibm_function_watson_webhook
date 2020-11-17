#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys

# MyCode

import requests

import json


people_id_dict = {'Luke Skywalker':1,
                    'C-3PO':2,
                    'R2-D2':3,
                    'Darth Vader':4,
                    'Leia Organa':5,
                    'Owen Lars':6,
                    'Beru Whitesun lars':7,
                    'R5-D4':8,
                    'Biggs Darklighter':9,
                    'Obi-Wan Kenobi':10,
                    'Anakin Skywalker':11,
                    'Wilhuff Tarkin':12,
                    'Chewbacca':13,
                    'Han Solo':14,
                    'Greedo':15,
                    'Jabba Desilijic Tiure':16,
                    'Wedge Antilles':18,
                    'Jek Tono Porkins':19,
                    'Yoda':20,
                    'Palpatine':21,
                    'Boba Fett':22,
                    'IG-88':23,
                    'Bossk':24,
                    'Lando Calrissian':25,
                    'Lobot':26,
                    'Ackbar':27,
                    'Mon Mothma':28,
                    'Arvel Crynyd':29,
                    'Wicket Systri Warrick':30,
                    'Nien Nunb':31,
                    'Qui-Gon Jinn':32,
                    'Nute Gunray':33,
                    'Finis Valorum':34,
                    'Padmé Amidala':35,
                    'Jar Jar Binks':36,
                    'Roos Tarpals':37,
                    'Rugor Nass':38,
                    'Ric Olié':39,
                    'Watto':40,
                    'Sebulba':41,
                    'Quarsh Panaka':42,
                    'Shmi Skywalker':43,
                    'Darth Maul':44,
                    'Bib Fortuna':45,
                    'Ayla Secura':46,
                    'Ratts Tyerel':47,
                    'Dud Bolt':48,
                    'Gasgano':49,
                    'Ben Quadinaros':50,
                    'Mace Windu':51,
                    'Ki-Adi-Mundi':52,
                    'Kit Fisto':53,
                    'Eeth Koth':54,
                    'Adi Gallia':55,
                    'Saesee Tiin':56,
                    'Yarael Poof':57,
                    'Plo Koon':58,
                    'Mas Amedda':59,
                    'Gregar Typho':60,
                    'Cordé':61,
                    'Cliegg Lars':62,
                    'Poggle the Lesser':63,
                    'Luminara Unduli':64,
                    'Barriss Offee':65,
                    'Dormé':66,
                    'Dooku':67,
                    'Bail Prestor Organa':68,
                    'Jango Fett':69,
                    'Zam Wesell':70,
                    'Dexter Jettster':71,
                    'Lama Su':72,
                    'Taun We':73,
                    'Jocasta Nu':74,
                    'R4-P17':75,
                    'Wat Tambor':76,
                    'San Hill':77,
                    'Shaak Ti':78,
                    'Grievous':79,
                    'Tarfful':80,
                    'Raymus Antilles':81,
                    'Sly Moore':82,
                    'Tion Medon':83}

def translate_olhos(cor : str):
  cor = cor.replace('blue','azuis')
  cor = cor.replace('yellow','amarelos')
  cor = cor.replace('red','vermelhos')
  cor = cor.replace('brown','castanhos')
  cor = cor.replace('blue-gray','azul-cinza')
  cor = cor.replace('black','negros')
  cor = cor.replace('orange','laranjas')
  cor = cor.replace('hazel','cor de mel')
  cor = cor.replace('pink','rosas')
  cor = cor.replace('unknown','cor desconhecida...')
  cor = cor.replace('gold','dourados')
  cor = cor.replace('green','verdes')
  cor = cor.replace('white','brancos')
  return cor

def translate_cabelo(cor : str):
  cor = cor.replace('blond','loiro')
  cor = cor.replace('n/a','sem cabelo...')
  cor = cor.replace('none','sem cabelo...')
  cor = cor.replace('brown','castanho')
  cor = cor.replace('grey','cinza')
  cor = cor.replace('black','preto')
  cor = cor.replace('white','branco')
  cor = cor.replace('auburn','ruivo')
  cor = cor.replace('blonde','loiro')
  return cor

def translate_pele(cor : str):
  cor = cor.replace('fair','clara')
  cor = cor.replace('gold','dourada')
  cor = cor.replace('white','branca')
  cor = cor.replace('blue','azul')
  cor = cor.replace('light','clara')
  cor = cor.replace('red','vermelha')
  cor = cor.replace('unknown','desconhecida...')
  cor = cor.replace('green','verde')
  cor = cor.replace('tan','bronzeada')
  cor = cor.replace('brown','marrom')
  cor = cor.replace('pale','pálida')
  cor = cor.replace('metal','metálica')
  cor = cor.replace('dark','negra')
  cor = cor.replace('mottle','manchada')
  cor = cor.replace('grey','cinza')
  cor = cor.replace('orange','laranja')
  cor = cor.replace('yellow','amarela')
  cor = cor.replace('silver','prateada')
  return cor
  
def translate_genero(gen : str):
  gen = gen.replace('female', 'feminino')
  gen = gen.replace('male', 'masculino')
  gen = gen.replace('n/a', 'sem sexo...')
  gen = gen.replace('none', 'sem sexo...')
  gen = gen.replace('hermaphrodite', 'hermafrodita')
  return gen

def main(dict):
    
    try:  
        if dict["compara"] == "true":
            
            r1 = requests.get(f'https://swapi.dev/api/people/{people_id_dict[dict["personagem1"]]}/')
            r2 = requests.get(f'https://swapi.dev/api/people/{people_id_dict[dict["personagem2"]]}/')
            
            idade1 = int(float(r1.json()['birth_year'].replace('BBY','')))
            idade2 = int(float(r2.json()['birth_year'].replace('BBY','')))
            
            if idade1 > idade2:
                resposta = f'{dict["personagem1"]} tinha {idade1} anos no ano da batalha de Yavin enquanto ' + \
                    f'{dict["personagem2"]} tinha {idade2} anos, ou seja, {dict["personagem1"]}' + \
                    ' tem mais idade!'
                    
                return {"resp": resposta}
            
            elif idade1 < idade2:
                
                resposta = f'{dict["personagem2"]} tinha {idade2} anos no ano da batalha de Yavin enquanto ' + \
                    f'{dict["personagem1"]} tinha {idade1} anos, ou seja, {dict["personagem2"]}' + \
                    ' tem mais idade!'
                    
                return {"resp": resposta}
                
            else:
                
                resposta = f'{dict["personagem1"]} e {dict["personagem2"]} tinham a mesma idade' + \
                    f' no ano da batalha de Yavin, {idade1} anos'
                    
                return {"resp": resposta}
                
    except ValueError:
        
        resposta = f'alguém tem idade desconhecida... ' + \
            f'{dict["personagem1"]} ou {dict["personagem2"]}...'
        
        return {"resp": resposta}
        
    except KeyError:
        print('nada')
    
    r = requests.get(f'https://swapi.dev/api/people/{people_id_dict[dict["nome"]]}/')
    
    resp = {}
    resp['nome'] = r.json()['name']
    resp['altura'] = r.json()['height']
    resp['peso'] =  r.json()['mass']
    resp['cabelo'] = translate_cabelo(r.json()['hair_color'])
    resp['pele'] = translate_pele(r.json()['skin_color'])
    resp['olhos'] = translate_olhos(r.json()['eye_color'])
    resp['idade'] = r.json()['birth_year'].replace('BBY', ' anos, no ano da batalha de Yavin')
    resp['sexo'] = translate_genero(r.json()['gender'])
    
    return resp
