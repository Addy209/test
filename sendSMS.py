from twilio.rest import Client
account_sid = 'ACe4726f4c1b5d38bcfc3509357c30baae'
auth_token = 'cf2d7a7dcb7cf1dcad6815eb32a7a972'
client = Client(account_sid, auth_token)
message = client.messages.create(body='Your OTP for Twilio is 125478', from_=[+12542124588], to=[+918709337711])
print(message.sid)