print("Welcome to Isaac's Chatbot!\n")
print("Hey there")

user_name = input("What is your name? ")
user_age = input("How old are you? ")

print("\n")

choice = 0

while True:
  print("How can I help you today?\n")

  print("1. Option 1\n2. Option 2\n3. Option 3\n4. Option 4\n5. Exit")
  choice = int(input())
  if choice == 5:
    break

print(f"\nGoodbye {user_name}. See you later!")