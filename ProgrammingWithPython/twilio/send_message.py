from twilio.rest import TwilioRestClient

account_sid = "AC92dda00ca1938a7c30751f1cdf5b551b" # Your Account SID from www.twilio.com/console
auth_token  = "7c80901f3bf4895e71522f3bc2657951"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+14694509938",    # Replace with your phone number
    from_="+14696172043") # Replace with your Twilio number

print(message.sid)