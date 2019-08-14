"""
Proof: https://en.wikipedia.org/wiki/Pythagorean_triple
"""

def pythagora(m,n):

    # Formulas
    if m > n:
        a = m**2 - n**2
    else:
        a = n**2 - m**2

    b = 2*m*n
    c = m**2 + n**2
    print()
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print()
    
    # Pythagora's Theorem confirmation
    print(f'{a}**2 + {b}**2 = {c}**2 ==> {a**2} + {b**2} = {c**2} ==> {a**2 + b**2} = {c**2}')


def request():
    print("Given 'm' and 'n' values, you can obtain 'a','b' e 'c' values for the Pythagorean's Triple\n")
    m = int(input("m: "))
    n = int(input("n: "))
    pythagora(m,n)

request()
