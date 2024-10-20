class Food:
  def __init__(self, name, url, comment, hashtag):
      self.name = name

      self.url = url

      self.comment = comment

      self.hashtag = hashtag
 

  def getName(self):
      return self.name

  def geturl(self):
      return self.url

  def getComment(self):
      return self.comment

  def getHashtag(self):
      return self.hashtag

class Art:
  def __init__(self, name, url, comment, hashtag):
      self.name = name

      self.url = url

      self.comment = comment

      self.hashtag = hashtag


  def getName(self):
      return self.name

  def geturl(self):
      return self.url

  def getComment(self):
      return self.comment

  def getHashtag(self):
      return self.hashtag

class Language:
  def __init__(self, name, url, comment, hashtag):
      self.name = name

      self.url = url

      self.comment = comment

      self.hashtag = hashtag


  def getName(self):
      return self.name

  def geturl(self):
      return self.url

  def getComment(self):
      return self.comment

  def getHashtag(self):
      return self.hashtag

def foodCulture():
  
  foodList = [
      Food("Shami Kebab", "https://www.teaforturmeric.com/wp-content/uploads/2019/04/Instant-Pot-Shami-Kabab-960x540.jpg", "Shami kebab are tender, wholesome patties made with beef and chana dal (yellow split peas). ", "#dinner, #beef, #yummy"),
      Food("Aloo Tikki", "https://www.teaforturmeric.com/wp-content/uploads/2024/02/Aloo-Tikki-16-960x540.jpg", "This recipe for Pakistani-style Aloo Tikki is made with mashed potatoes, onions, herbs, and spices.", "#tasty, #yummy, #potato"),
      Food("Seekh Kebab", "https://www.teaforturmeric.com/wp-content/uploads/2018/10/Seekh-Kebab-4-960x540.jpg", "A flavorful, tender kebabs that don't break or fall off the skewers.", "#kebab, #dinner, #delicious"),
      Food("Roast Chicken", "https://untoldrecipesbynosheen.com/wp-content/uploads/2023/01/steam-roast-main-1.jpg", "This chicken, also known as Degi Steam Roast, uses an ancient South Asian cooking method called dum.", "#dinner, #chicken, #roast"),
      Food("Tandoori Fish", "https://untoldrecipesbynosheen.com/wp-content/uploads/2024/06/tandoori-fish-main-2.jpg", "Tandoori fish is traditionally cooked in a tandoor with mild-flavored white fish", "#fish, #easy, #Pakistani, #food")
  ]
  
  artList = [
      Art("Truck Art", "https://media.npr.org/assets/img/2022/01/27/2021-12-23-truckart-44_slide-5fa2a097f9d2c494b6f84aec2e6e6188ddcc61da.jpg?s=1100&c=85&f=jpeg", "These trucks highlight floral designs and caligraphy.", "#automotives, #painting, #floral"),
      Art("Kalash Oil Painting", "https://i.etsystatic.com/23192516/r/il/4a1b71/3343542711/il_570xN.3343542711_qh33.jpg", "This vibrant oil painting on stretched canvas depicts three Kalash sisters from the Chitral district of North-Western Pakistan. The Kalash are a Dardic indigenous group, speaking the Kalasha language. The cool tones of the Chitral Valley are juxtaposed against the vibrant textures and warm toned-fabric of their traditional attire.", "#painting, #oilPainting"),
      Art("Art of Gandhara", "https://asiasociety.org/sites/default/files/0/01.15.jpg", "This sculpture represents complex cultural influences — from Scytho-Parthian to Greco-Roman traditions — that fed the extraordinary artistic production of this region from the first century B.C.E. through fifth century C.E.", "#sculpture, #Buddhism"),
      Art("Indo-Islamic Architecture", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Tomb_of_Shah_Rukn-e-Alam_2014-07-31.jpg/220px-Tomb_of_Shah_Rukn-e-Alam_2014-07-31.jpg", "This is the architecture of the Indian subcontinent produced by and for Islamic patrons and purposes.", "#architecture, #buildings"),
      Art("Calligraphy", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBXPqFv1tWYfu1a7cFeLG_Y9hM-QSjdBbo5w&s", "Wall Calligraphy is one of the most prestigious forms of fine art in which Arabic Calligraphy possesses a special religious and social significance in Pakistan and it is also seen in many historic mosques around the country.", "#calligraphy, #tiling")
  ]
  
  languageList = [
      Language("Excerpt of Text", "https://www.ucl.ac.uk/atlas/urdu/images/Pic11.jpg", "This is an excerpt of the text", "#text, #language"),
      Language("Multani Script", "https://upload.wikimedia.org/wikipedia/commons/8/82/Example_of_a_Multani_variant_of_Landa_script%2C_a_mercantile_shorthand_script_of_Punjab%2C_from_1880.png", "This is an excerpt of Multani speech", "#language, #excerpt"),
      Language("Written Urdu", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqPfXVvyJrRYU0Sb53HF80z4Y-kEkql-VcOQ&s", "This is an image of written Urdu.", "#language, #learning, #calligraphy"),
      Language("Urdu Lettering", "https://media.licdn.com/dms/image/D4D12AQG-q9NF46sOxA/article-cover_image-shrink_720_1280/0/1677207696314?e=2147483647&v=beta&t=wtzZXZnlIa3k6lAN-wAgSSbJsl32dcrulSyLy6kdK-c", "This is a piece of text of the Urdu language", "#Urdu, #language, #linguistics"),
      Language("Piece of Text", "https://i0.wp.com/sikhspirit.com/wp-content/uploads/2017/12/shahmukhi.jpg?resize=384%2C301&ssl=1", "This is an excerpt of the text", "#text, #writing, #language")
 
  ]
  
  return foodList, artList, languageList

