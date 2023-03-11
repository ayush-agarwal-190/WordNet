plants = ['अहिंस्रा', 'कोथरी पत्त्रघना'  'महाकण्टकिनी', 'वज्रतुण्ड',  'वज्रदण्डक वज्रवृक्ष' ,  'विदर', 'विश्वसारक', 'शून्या' ]

plants_dict = {}

for plant in plants:
    first_letter = plant[0]
    if first_letter not in plants_dict:
        plants_dict[first_letter] = [plant]
    else:
        added = False
        for key, value in plants_dict.items():
            if plant in value:
                added = True
                break
        if not added:
            for key, value in plants_dict.items():
                if value[0] == first_letter:
                    plants_dict[key].append(plant)
                    break

for key, value in plants_dict.items():
    print(f" {key}: {', '.join(value)}")
