# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44


pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

characters_per_page = lines_per_page * characters_per_line
characters_per_book = pages_per_book * characters_per_page
bytes_per_book = characters_per_book * bytes_per_character
book_size_mb = bytes_per_book
disk_capacity_mb = disk_capacity_mb * 1024 * 1024


num_books_on_disk = int(disk_capacity_mb // book_size_mb)

print("Количество книг, помещающихся на дискету:", num_books_on_disk)
