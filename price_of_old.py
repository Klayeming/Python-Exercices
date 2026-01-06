"""
Docstring for price_of_old
#32 Write a program who calculete the mount to give for year old 
"""
def year_old(mount, old):
    all_mount = 0
    for i in range(1, old+1):
        all_mount = all_mount + (mount +(i*3))
    year_mount = mount + (old*3)
    print(f"the mount for year when he/she turns {old} old will be {year_mount}")
    print(f"the mount for account when he/she turns {old} old year is {all_mount}")

mount = float(input("Please write the initial mount: ")) 
old = int(input("Please enter age: "))
year_old(mount, old)