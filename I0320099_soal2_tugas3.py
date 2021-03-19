dict = {"Name":"Talitha Pranastiti",
        "Hobby":["Dancing", "Running", "Watching Movies"],
        "Social Media":["ig=@prnsttalitha", "idline=talithaprnst", "wa=081228332162"],
        "Favorite Songs":["NCT U-From Home", "NCT U-Misfit", "Pamungkas-To the Bone"],
        "Favorite Food":["Wagyu Beef", "Seblak", "Mie"]}

print(dict)

#ubah hobi
dict["Hobby"][1] = "Singing"
#ubah social media
dict["Social Media"][2] = "twitter=@TalithaP11"
#hapus 2 makanan favorit
del dict["Favorite Food"][:2]
#tambah 1 hobi
dict["Hobby"].append("Dringking Coffee")

print("dict setelah diubah: ")
print(dict)





