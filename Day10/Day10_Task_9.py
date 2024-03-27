def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}:{value}")


person(name="JH",age=26,city="Hyd",mob_no=921345372)