# print("1. 1집")
# print("2. 2집")
# print("3. 3집")
# print("4. 4집")
# print("5. 5집")
# a = int(input("Select a number. (1-5) > "))
#
# if a == 1:
#     print("유리구슬")
# elif a == 2:
#     print("오늘부터")
# elif a == 3:
#     print("시간을")
# elif a == 5:
#     print("핀")
# else:
#     print("No data")



# albums = { 1:"1집",
#            2:'2집',
#            3:'3집',
#            4:'4집',
#            5:'5집'}
#
# print("1. 1집")
# print("2. 2집")
# print("3. 3집")
# print("4. 4집")
# print("5. 5집")
# a = int(input("Select a number. (1-5) > "))
# print(albums.get(a, "No data"))


# def album(x):
#     return {1: "EP 1집: Season of Glass / 유리구슬 (Glass Bead)",
#             2: "EP 2집: Flower Bud / 오늘부터 우리는 (Me Gustas Tu)",
#             3: "EP 3집: SNOWFLAKE / 시간을 달려서 (Rough)",
#             4: "정규 1집: LOL / 너 그리고 나 (NAVILLERA)",
#             5: "EP 4집: THE AWAKENING / FINGERTIP"
#             }.get(x, "No data")
#
#
# print("1. EP 1집")
# print("2. EP 2집")
# print("3. EP 3집")
# print("4. 정규 1집")
# print("5. EP 4집")
# a = int(input("Select a number. (1-5)"))
#
# print(album(a))


def album_glass():
    print("EP 1집: Season of Glass / 유리구슬 (Glass Bead)")


def album_flower():
    print("EP 2집: Flower Bud / 오늘부터 우리는 (Me Gustas Tu)")


def album_snow():
    print("EP 3집: SNOWFLAKE / 시간을 달려서 (Rough)")


def album_lol():
    print("정규 1집: LOL / 너 그리고 나 (NAVILLERA)")


def album_awakening():
    print("EP 4집: THE AWAKENING / FINGERTIP")


print("1. EP 1집")
print("2. EP 2집")
print("3. EP 3집")
print("4. 정규 1집")
print("5. EP 4집")
a = int(input("Select a number. (1-5)"))

albums = {1: album_glass,
          2: album_flower,
          3: album_snow,
          4: album_lol,
          5: album_awakening}

try:
    albums[a]()
except KeyError:
    print("No data")