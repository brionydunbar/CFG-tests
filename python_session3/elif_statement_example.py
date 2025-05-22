"""
IF-ELIF-ELSE statements

If-elif-else handles multiple conditions:
- Check first condition with 'if'
- Check additional conditions with 'elif'
- Optional 'else' for when no conditions are True

Syntax:
    if condition1:
        code for condition 1
    elif condition2:
        code for condition 2
    elif condition3:
        code for condition 3
    else:
        code when no conditions match
"""

# example: weather recommendations; what to wear for different temperatures

temperature = int(input("What is the temperature? "))

if 0 <= temperature < 10:
    print("It's cold, wear a big jacket.")
elif 10 <= temperature < 20:
    print("It's chilly, wear a light jacket.")
elif 20 <= temperature < 35:
    print("It's pretty warm, you don't need a jacket.")
elif 35 <= temperature < 50:
    print("It's too hot, don't go out!")
else:
    print("You will burn to a crisp.")