# Print the numbers until 100. The numbers divisivble by 3 show Fizz, the numbers divisivble by 5 show Buzz, the numbers divisivble by 15 show FizzBuzz.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
    elif i % 3 == 0:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
        
    else:
        print(i)
