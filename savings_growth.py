"""
Module: Savings Growth Calculator

Calculates accumulated savings over years with fixed annual increase.

Logic: Each year adds $3 to the initial amount.
Example: Starting with $100, after 5 years: amounts are $103, $106, $109, $112, $115.
"""

def year_old(mount, old):
    """Calculate savings accumulation over years.
    
    Args:
        mount (float): Initial amount
        old (int): Number of years
    """
    all_mount = 0
    # Sum of: mount, mount+3, mount+6, ..., mount+3*old
    for i in range(1, old+1):
        all_mount = all_mount + (mount + (i*3))
    year_mount = mount + (old*3)
    print(f"The amount at year {old} will be {year_mount}")
    print(f"The total account when reaching {old} years old is {all_mount}")

mount = float(input("Please write the initial amount: "))
old = int(input("Please enter number of years: "))
year_old(mount, old)