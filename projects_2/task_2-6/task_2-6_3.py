donor_blood_type = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood_type = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()
if donor_blood_type == recipient_blood_type or donor_blood_type == "I":
    print("Переливание возможно.")
else:
    print("Переливание невозможно.")