import random
import os

def load_word():
    try:
        with open("words.txt", "r") as infile:
            lines = infile.readlines()
            return random.choice(lines).strip().lower()
    except FileNotFoundError:
        print("words.txt 파일을 찾을 수 없습니다. 기본 단어를 사용합니다.")
        return "hello"

guesses = set()  # set을 사용하여 중복 추측 방지
turns = 10
word = load_word()

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    if failed == 0:
        print("\n축하합니다! 단어를 맞추셨습니다!")
        break
    
    print(f"\n남은 기회: {turns}")
    guess = input("한 글자를 입력하세요: ").lower()
    
    if len(guess) != 1:
        print("한 글자만 입력해주세요!")
        continue
        
    if guess in guesses:
        print("이미 추측한 글자입니다!")
        continue
        
    guesses.add(guess)
    
    if guess not in word:
        turns -= 1
        print("틀렸습니다!")
        if turns == 0:
            print(f"게임 오버! 정답은 '{word}'였습니다.")