# 01
def get_score(**courses):
    for course, score in courses.items():
        print(f"{course} => {score}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)
# 02


def get_people_scores(name="Unknown", **courses):
    if not courses:
        print(f"Hello {name} You Have No Score To Show")
    else:
        if name == "Unknown":
            for course, score in courses.items():
                print(f"{course} => {score}")
        else:
            print(f"Hello {name} This Is Your Score Table:")
            for course, score in courses.items():
                print(f"{course} => {score}")


# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)
# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)
# Test 3
get_people_scores(Logic=70, Problems=60)
# Test 4
get_people_scores("Ahmed")


# 03

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(name="Unknown", **scores_list):

    if not scores_list:
        print(f"Hello {name} You Have No Score To Show")
    else:
        if name == "Unknown":
            for course, score in scores_list.items():
                print(f"{course} => {score}")
        else:
            print(f"Hello {name} This Is Your Score Table:")
            for course, score in scores_list.items():
                print(f"{course} => {score}")


# Test 1
get_the_scores("Osama", **scores_list)
# Test 2
get_the_scores("Osama")
# Test 3
get_the_scores(**scores_list)
