# password-security-tester
This is a web application that checks wether your password has been pwned(ie hacked) and its usages. It also checks it 
strength as well at the same time.

this project uses the api:'https://api.pwnedpasswords.com/range/' but for security only the first five characters
of the hashed password are sent over the internet. Multpile passwords are recieved and your password and it's num of breaches 
is 'sieved' locally.
