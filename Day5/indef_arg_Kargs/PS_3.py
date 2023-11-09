def describe_person(name,**kwargs):
    print(f"Characteristics of {name}:")
    for arg_name,arg_v in kwargs.items():
        print(f"{arg_name}: {arg_v}")




#describe_person("Ash", eye_color="brown", hair_color="black")
