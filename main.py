import requests
import json
import hashlib
import os

accountmail = input("Whats Your Gmail: ")
accountpasswordhash = input("Whats Your Password: ")

hash_object = hashlib.md5(accountpasswordhash.encode())
accountpassword = hash_object.hexdigest()
print(accountpassword)

accounturl = f"https://account.sploop.io/login?mail={accountmail}&hash={accountpassword}"

response = requests.get(accounturl)
if response.status_code == 200:
  data = response.json()
  yourscore = data['score']

  if yourscore >= 3296100000:
    currentrank = "Eternal ($1000)"
    nextrank = "N/A"
  elif yourscore >= 1696100000:
    currentrank = "Radiant"
    nextrank = "Eternal"
  elif yourscore >= 1296100000:
    currentrank = "Astral"
    nextrank = "Radiant"
  elif yourscore >= 1096100000:
    currentrank = "Celestial"
    nextrank = "Astral"
  elif yourscore >= 896100000:
    currentrank = "Draconic"
    nextrank = "Celestial"
  elif yourscore >= 696100000:
    currentrank = "Immortal"
    nextrank = "Draconic"
  elif yourscore >= 496100000:
    currentrank = "Divine"
    nextrank = "Immortal"
  elif yourscore >= 296100000:
    currentrank = "Mystic"
    nextrank = "Divine"
  elif yourscore >= 196100000:
    currentrank = "Amber"
    nextrank = "Mystic"
  elif yourscore >= 116100000:
    currentrank = "Platinum"
    nextrank = "Amber"
  elif yourscore >= 86100000:
    currentrank = "Ruby"
    nextrank = "Platinum"
  elif yourscore >= 35000000:
    currentrank = "Emerald"
    nextrank = "Ruby"
  elif yourscore >= 20100000:
    currentrank = "Diamond"
    nextrank = "Emerald"
  elif yourscore >= 10100000:
    currentrank = "Gold"
    nextrank = "Diamond"
  elif yourscore >= 6100000:
    currentrank = "Silver"
    nextrank = "Gold"
  elif yourscore >= 2100000:
    currentrank = "Bronze"
    nextrank = "Silver"
  elif yourscore >= 900000:
    currentrank = "Copper"
    nextrank = "Bronze"
  elif yourscore >= 100000:
    currentrank = "Stone"
    nextrank = "Copper"
  else:
    currentrank = "Wood"
    nextrank = "Stone"

  print(
      f"Account Username: {data['nickname']}#{data['counter']}\nAccount Score: {data['score']} & Current Rank {currentrank} - Next Rank : {nextrank} \nKills : {data['kill']} & Death: {data['death']} \nTop Leaderboard = None (will added soon)"
  )
else:
  print("Error, Having Account issue or wrong password")

os.system("pause") # If you use python in windows. this code should need if you use replit then you will see this "sh: 1: pause: not found" just ingore it.
