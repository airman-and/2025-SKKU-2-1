"""
상속(Inheritance)에 대한 총체적인 설명

1. 상속의 개념
   - 상속은 객체지향 프로그래밍(OOP)의 핵심 개념 중 하나로, 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 것을 의미합니다.
   - 이를 통해 코드 재사용성을 높이고, 계층적 관계를 표현할 수 있습니다.
   - 상속하는 클래스는 '부모 클래스(parent class)' 또는 '기반 클래스(base class)', '슈퍼 클래스(super class)'라고 부릅니다.
   - 상속받는 클래스는 '자식 클래스(child class)' 또는 '파생 클래스(derived class)', '서브 클래스(sub class)'라고 부릅니다.

2. 상속의 종류
   - 단일 상속(Single Inheritance): 한 클래스가 하나의 부모 클래스를 상속받는 형태
   - 다중 상속(Multiple Inheritance): 한 클래스가 여러 부모 클래스를 상속받는 형태 (파이썬에서 지원, Java에서는 지원하지 않음)
   - 다단계 상속(Multilevel Inheritance): 상속 관계가 여러 단계로 이어지는 형태 (A → B → C)
   - 계층적 상속(Hierarchical Inheritance): 하나의 부모 클래스를 여러 자식 클래스가 상속받는 형태
   - 혼합 상속(Hybrid Inheritance): 위의 여러 상속 형태가 혼합된 형태

3. 상속의 장점
   - 코드 재사용성 증가: 이미 작성된 코드를 재사용하여 개발 시간 단축
   - 확장성: 기존 클래스를 수정하지 않고 기능 확장 가능
   - 유지보수성: 공통 코드는 부모 클래스에 위치하여 유지보수가 용이
   - 계층적 구조 표현: 현실 세계의 계층적 관계를 프로그램에서 표현 가능
"""

# 1. 기본 상속 예제
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some generic sound")
    
    def introduce(self):
        print(f"I am {self.name}")

# Animal 클래스를 상속받은 Dog 클래스
class Dog(Animal):
    def make_sound(self):  # 메서드 오버라이딩
        print("Woof!")
    
    def wag_tail(self):  # 새로운 메서드 추가
        print(f"{self.name} is wagging tail")

# Animal 클래스를 상속받은 Cat 클래스
class Cat(Animal):
    def make_sound(self):  # 메서드 오버라이딩
        print("Meow!")
    
    def purr(self):  # 새로운 메서드 추가
        print(f"{self.name} is purring")

# 객체 생성 및 사용
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.introduce()  # 부모 클래스의 메서드 사용
dog.make_sound()  # 오버라이딩된 메서드 사용
dog.wag_tail()  # 자식 클래스의 고유 메서드 사용

cat.introduce()  # 부모 클래스의 메서드 사용
cat.make_sound()  # 오버라이딩된 메서드 사용
cat.purr()  # 자식 클래스의 고유 메서드 사용

# 2. super() 함수 사용 예제
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 클래스의 생성자 호출
        self.student_id = student_id
    
    def introduce(self):
        base_intro = super().introduce()  # 부모 클래스의 메서드 호출
        return f"{base_intro} My student ID is {self.student_id}."

student = Student("John", 20, "S12345")
print(student.introduce())

# 3. 다중 상속 예제
class Engine:
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"Vehicle brand: {self.brand}")

class Car(Engine, Vehicle):  # Engine과 Vehicle 두 클래스를 모두 상속
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)  # 명시적 부모 클래스 생성자 호출
        self.model = model
    
    def full_info(self):
        self.info()
        print(f"Model: {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.start()  # Engine 클래스의 메서드
my_car.info()   # Vehicle 클래스의 메서드
my_car.full_info()  # Car 클래스의 메서드
my_car.stop()   # Engine 클래스의 메서드

# 4. 메서드 해결 순서(Method Resolution Order, MRO)
print("MRO for Car class:", [cls.__name__ for cls in Car.__mro__])

# 5. 추상 클래스 예제
from abc import ABC, abstractmethod

class Shape(ABC):  # 추상 클래스 정의
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        print("This is a geometric shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # 추상 메서드 구현
        return self.width * self.height
    
    def perimeter(self):  # 추상 메서드 구현
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # 추상 메서드 구현
        return 3.14 * self.radius ** 2
    
    def perimeter(self):  # 추상 메서드 구현
        return 2 * 3.14 * self.radius

# 객체 생성 및 사용
rect = Rectangle(5, 4)
circle = Circle(7)

print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

# 6. 속성 상속과 접근 제어
class Base:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"  # 관례적으로 protected
        self.__private_var = "Private"     # 이름 맹글링으로 인한 private
    
    def access_vars(self):
        print(f"Inside Base - Public: {self.public_var}")
        print(f"Inside Base - Protected: {self._protected_var}")
        print(f"Inside Base - Private: {self.__private_var}")

class Derived(Base):
    def access_vars(self):
        print(f"Inside Derived - Public: {self.public_var}")
        print(f"Inside Derived - Protected: {self._protected_var}")
        # 아래 코드는 오류 발생 - 자식 클래스에서 부모의 private 변수에 직접 접근 불가
        # print(f"Inside Derived - Private: {self.__private_var}")
        # 하지만 이렇게는 접근 가능 (이름 맹글링으로 인해)
        print(f"Inside Derived - Private (mangled): {self._Base__private_var}")

base = Base()
derived = Derived()

base.access_vars()
print("-" * 30)
derived.access_vars()

# 7. 다형성(Polymorphism) 예제
def make_animal_sound(animal):  # 다형성을 보여주는 함수
    animal.make_sound()  # 어떤 동물 객체가 전달되든 해당 객체의 make_sound() 호출

animals = [Dog("Rex"), Cat("Mittens"), Dog("Max")]
for animal in animals:
    make_animal_sound(animal)  # 각 동물 타입에 맞는 소리를 출력

# 8. 믹스인(Mixins) 패턴
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class EmailSenderMixin:
    def send_email(self, message, to):
        print(f"Sending email to {to}: {message}")

class User(LoggerMixin, EmailSenderMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def register(self):
        self.log(f"User {self.name} registered")
        self.send_email("Welcome on board!", self.email)

new_user = User("Alice", "alice@example.com")
new_user.register()

# 9. 프로퍼티(Properties)와 상속
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # 절대 영도보다 낮을 수 없음
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

class WeatherStation(Temperature):
    def __init__(self, celsius=0, location="Unknown"):
        super().__init__(celsius)
        self.location = location
    
    def display(self):
        print(f"Location: {self.location}")
        print(f"Temperature: {self.celsius}°C / {self.fahrenheit}°F")

station = WeatherStation(23.5, "Seoul")
station.display()

# 온도 변경
station.celsius = 25.0  # 섭씨 설정
station.display()

station.fahrenheit = 80.0  # 화씨 설정
station.display()