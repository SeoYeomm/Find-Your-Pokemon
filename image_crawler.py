from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

# 1세대 포켓몬 151마리 이름 리스트
first_gen_pokemon = "Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok, Pikachu, Raichu, Sandshrew, Sandslash, Nidoran♀, Nidorina, Nidoqueen, Nidoran♂, Nidorino, Nidoking, Clefairy, Clefable, Vulpix, Ninetales, Jigglypuff, Wigglytuff, Zubat, Golbat, Oddish, Gloom, Vileplume, Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian, Psyduck, Golduck, Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Abra, Kadabra, Alakazam, Machop, Machoke, Machamp, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Geodude, Graveler, Golem, Ponyta, Rapidash, Slowpoke, Slowbro, Magnemite, Magneton, Farfetch'd, Doduo, Dodrio, Seel, Dewgong, Grimer, Muk, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee, Hypno, Krabby, Kingler, Voltorb, Electrode, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee, Hitmonchan, Lickitung, Koffing, Weezing, Rhyhorn, Rhydon, Chansey, Tangela, Kangaskhan, Horsea, Seadra, Goldeen, Seaking, Staryu, Starmie, Mr. Mime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros, Magikarp, Gyarados, Lapras, Ditto, Eevee, Vaporeon, Jolteon, Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew"
pokemon_list = first_gen_pokemon.split(', ')

pok_num = 1

# 각 포켓몬마다 반복
for pokemon in pokemon_list:
    # 파일 생성
    if not os.path.isdir(f"pokemons/{pok_num}/"):
        os.makedirs(f"pokemons/{pok_num}/")

    # 구글 이미지 검색 화면 불러오기
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    # 검색어 설정 후 검색
    search = "pokemon " + pokemon
    elem = driver.find_element("name", "q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

    # 화면 로딩까지 2초 기다리기
    time.sleep(2)

    # 이미지 찾기
    images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    count = 0
    max_count = 10 # 저장할 사진 수

    # 이미지마다 반복
    for image in images:
        if count > max_count: # 최대 개수만큼 저장했으면 종료
            break

        try: # 썸네일 클릭해 원본 이미지 저장
            image.click()
        
            # 로딩 기다리기
            time.sleep(0.5) 

            imgUrl = driver.find_element('xpath', '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]').get_attribute('src')

            # 파일에 저장
            urllib.request.urlretrieve(imgUrl, f"pokemons/{pok_num}/" + str(count) + ".jpg")
            print(f"Image saved: {pokemon} {count}.jpg")
            count += 1
        except Exception as e:
            print(e)

    pok_num += 1
    
driver.close()
