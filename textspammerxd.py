from twilio.rest import Client
client = Client(
    "AC5fa60409ac8e6bd12e1677da29a7eea3", "84632e550f2b748e7b1e65ca547f495e"
)
sender = "+15134406219"
receiver = "+15403956720"
message = "FUCk YOU BITCH"
amount = int(input("amount: "))
for i in range(0, amount):
    client.messages.create(to=receiver, from_=sender, body=message)
    print(f"[{i+1}] out of [{amount}] sent.")
    print(f"{sender}: {message} -------------> {receiver}")