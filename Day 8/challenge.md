#### Day 8: Function Parameters & Caesar Cipher
**Challenge:** Write a function that implements the Caesar Cipher for encrypting a message. It should take the message and shift value as parameters.

```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

message = "Hello World"
shift = 3
print(caesar_cipher(message, shift))
```


