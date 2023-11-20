class FishCakeMaker:
  def __init__(self, **kwargs):  #** : 가변인자매개변수
    self.size = 10
    self.flavor = "팥"
    self.price = 100

    if "size" in kwargs:
      self.size = kwargs.get("size") #kwargs 딕셔너리 안에 size라는 key값이 있나? 있다면 가져와서 size 변수에 대입
    if "flavor" in kwargs:
      self.flavor = kwargs.get("flavor")
    if "price" in kwargs:
      self.price = kwargs.get("price")

  def show(self):
    print("붕어빵 크기 : {}".format(self.size))
    print("붕어빵 종류 : {}".format(self.flavor))
    print("붕어빵 가격 : {}".format(self.price))
    print("*"*30)

fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size=20, price=300)
fish3 = FishCakeMaker(flavor = "초콜릿", size=15)

fish1.show()
fish2.show()
fish3.show()