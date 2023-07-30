from data import data
import random
from arts import logo, vs

def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"A - {format_data(account_a)}.")
    print(vs)
    print(f"B - {format_data(account_b)}.")
    
    guess = input("У кого больше подписчиков? Выбери 'A' или 'B': ").lower()
    a_follower_count = account_a["follower_count"] 
    b_follower_count = account_b["follower_count"] 
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)
    if is_correct:
      score += 1
      print(f"Ты прав! Текущий счет: {score}.")
    else:
      game_should_continue = False
      print(f"Извини, ты ошибся. Финальный счет: {score}")

game()