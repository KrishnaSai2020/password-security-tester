# password-security-tester
This is a program that checks wether your password has been pwned(ie hacked) and its usages.it also checks it 
strength as well at the same time.

The passwords are entered from the command line and multiple passwords can be entered at once.
this project uses the api:'https://api.pwnedpasswords.com/range/' but for security only the first five characters
of the hashed password are sent over the internet. multpile passwords are recieved and your password is retrieved 
locally.
