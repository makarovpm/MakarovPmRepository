import requests
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token_url = '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'

    def KullaniciAra(self,username):
        response = requests.get(self.api_url + '/users/'+ username)
        return response.json()
    
    def DepolariBul(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    def DepoOlustur(self):
        response = requests.get(self.api_url + '/user/repo?/acces_token='+self.token_url, json={

           "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": False,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": False,
  "bio": "There once was...",
  "twitter_username": "monatheoctocat",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z"

  }
    )
        return response.json()
        

github = Github()

while True:
    secim = input("1-Kullanıcı Ara\n2- Depoları Bul\n3- Depo Oluştur\n4- Çıkış\nSeçiminiz: ")
    if secim == '4':
        print("Çikiş (Exit) Yapildi.")
        break
    else:

        if secim == '1':
            username = input("Kullanici Adi Giriniz: ")
            result = github.KullaniciAra(username)
            print(f"Kullanici Adi: {result['name']}, Herkese Acik Public: {result['public_repos']}, Takipci: {result['followers']}")

        elif secim == '2':
            username = input("Kullanici Adi Giriniz: ")
            result = github.DepolariBul(username)
            for repo in result:
                print(repo)
        elif secim == '3':
            username = input("Kullanici Depo Adi Giriniz: ")
            result = github.DepoOlustur(username)
            print(result)
        else:
            print("Geçersiz Bir İşlem Yaptınız.")