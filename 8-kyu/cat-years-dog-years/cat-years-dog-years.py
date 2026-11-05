def human_years_cat_years_dog_years(human):
    cat = 15
    dog = 15
    if human > 1:
        dog = dog + 5*(human-2) + 9
        cat = cat + 4*(human-2) + 9
    return [human,cat,dog]