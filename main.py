import requests

class SuperHero:
  
    base_url = 'https://akabab.github.io/superhero-api/api'
  
    def _get_data(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        headers = {'Content_Type': 'application/json'}
        response = requests.get(request_url, headers = headers)
        data = response.json()
     
        list_heroes=[]
        for hero in data:
            list_heroes.append({'id': hero['id'],
                                'name': hero['name'],
                                'intelligence':  hero['powerstats']['intelligence']})
        return list_heroes

    def find_id_hero_by_name(self, name_hero):
        list_heroes = self._get_data()
        print(list_heroes)
        for hero in list_heroes:
            if hero['name'] == name_hero:
                id_hero = hero['id']
                break
        return id_hero
    
    def add_intalligence_by_name(self, name_hero):
        list_heroes = self._get_data()
        print(list_heroes)
        for hero in list_heroes:
            if hero['name'] == name_hero:
                intelligence = hero['intelligence']
                break
        return intelligence

class Heroes:

    def __init__(self, id_hero, name, intelligence=0):
        self.id = id_hero
        self.name = name
        self.intelligence = intelligence

    def __lt__(self, other):
        if not isinstance(other, Heroes):
            print(f'Ошибка. {other} не относится к классу Heroes')
        else:
            return self.intelligence < other.intelligence

    def __str__(self):
        res = f'{self.name} id({self.id}): intelligence = {self.intelligence} '
        return res

    

    

if __name__ == '__main__':
  sh = SuperHero()
  Hulk = Heroes(sh.find_id_hero_by_name('Hulk'),'Hulk', sh.add_intalligence_by_name('Hulk'))
  print(Hulk)