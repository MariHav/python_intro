def send_messages(messages,sent_messages):
    """Print messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: '{current_message}'")
        sent_messages.append(current_message)

messages = ['Hello!','How are you?','Have a nice day!']
sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
