- Tugas Analisis 1
Jika `hero1.hp` diubah menjadi 500, maka nilai HP `hero1` akan berubah menjadi 500 saat dicetak. Hal ini terjadi karena `hero1` dan `hero2` adalah objek yang terpisah meski berasal dari class yang sama, sehingga perubahan pada satu objek tidak memengaruhi objek lainnya.

- Tugas Analisis 2
Parameter `lawan` harus berupa objek utuh, bukan string, karena di dalam method `serang()` kita perlu memanggil method dan atribut milik lawan (seperti `lawan.diserang()` dan `lawan.name`). String tidak memiliki method tersebut, sehingga tidak bisa digunakan untuk berinteraksi antarobjek.

- Tugas Analisis 3
Jika `super().__init__()` dihapus, akan muncul error `AttributeError: 'Mage' object has no attribute 'name'`. Ini terjadi karena constructor `Hero` tidak pernah dijalankan, sehingga atribut `name`, `hp`, dan `attack_power` tidak pernah dibuat pada objek `Mage`.
Fungsi `super()` adalah untuk memanggil constructor milik class induk, sehingga class anak dapat mewarisi proses inisialisasi data tanpa perlu menulis ulang kode yang sama.

- Tugas Analisis 4
1. Akses `hero1._Hero__hp` tetap berhasil menampilkan nilai HP. Ini karena Python melakukan *name mangling*, bukan benar-benar menyembunyikan atribut. Namun cara ini tetap tidak boleh dilakukan karena melewati validasi pada setter, sehingga data bisa menjadi tidak valid.
2. Jika validasi pada `set_hp` dihapus, maka `hero1.set_hp(-100)` akan membuat HP menjadi -100. Ini membuktikan bahwa setter berfungsi sebagai penjaga aturan/validasi data, bukan sekadar formalitas.

- Tugas Analisis 5
1. Jika method `serang` di class `Hero` dihapus, akan muncul error `TypeError: Can't instantiate abstract class Hero with abstract method serang`. Ini karena `Hero` wajib mengimplementasikan seluruh method abstrak dari `GameUnit`.
2. Jika `unit = GameUnit()` dijalankan, akan muncul error serupa karena `GameUnit` adalah abstract class yang hanya berfungsi sebagai kontrak/blueprint, bukan objek nyata yang bisa dipakai langsung.

- Tugas Analisis 6
1. Menambahkan class `Healer` tidak akan mengubah kode loop sama sekali, selama `Healer` memiliki method `serang()`. Ini menunjukkan keuntungan polymorphism: kode utama tidak perlu diubah saat ada penambahan class baru.
2. Jika nama method pada class `Archer` diubah menjadi `tembak_panah`, program akan error karena loop memanggil method `serang()`. Ini menunjukkan bahwa nama method harus konsisten antara class induk dan class anak agar polymorphism dapat berjalan.
