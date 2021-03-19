#isi list sebanyak 10
friends = ['Alica', 'Alvin', 'Alya', 'Maurich', 'Rifqi', 'Rara', 'Sekar', 'Titus', 'Putri', 'Wanda']

#indeks nomor 4,6,7
print(friends[4])
print(friends[6])
print(friends[7])

#ganti nama pada indeks 3,5,9
friends[3] = 'Diva'
friends[5] = 'Raysa'
friends[9] = 'Yuki'

#tambah 2 nama
friends.extend(['Retno', 'Stefany'])

#iteration
for x in friends :
    print(x, end = ' ')

#panjang list
print(len(friends))



