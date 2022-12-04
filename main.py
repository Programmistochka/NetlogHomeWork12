import requests

class SuperHero:
  
    base_url = 'https://akabab.github.io/superhero-api/api'
  
    def _get_data(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        headers = {'Content_Type': 'application/json'}
        response = requests.get(request_url, headers = headers)
        data = response.json()
     
        print(data)
        #for hero in data:
        #    print (hero['id'], hero['name'])
        list_heroes=[]
        for hero in data:
            #print (hero['id'], hero['name'])
            list_heroes.append({'id': hero['id'],
                                'name': hero['name'],
                                'intelligence':  hero['powerstats']['intelligence']})
        print(list_heroes)

    

if __name__ == '__main__':
  sh = SuperHero()
  sh._get_data()
  #sh.list_all_heroes()