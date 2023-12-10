# Praktikum_TG_E6

Dokumentasi Praktikum 1 dan 2 Mata Kuliah Teori Graf oleh Kelompok 6

### Kelompok 6

|                       Nama                               |    NRP     |
| :------------------------------------------------------: | :--------: |
|   [Nabila Aidah Diani](https://github.com/nabilaaidah)   | 5025211032 |
|   [Mashita Dewi](https://github.com/mashitaad)           | 5025211036 |
|   [Andhika Lingga Mariano](https://github.com/Deekuh)    | 5025211161 |

## Daftar Isi
- [Praktikum 1](#praktikum-1)
  - [Soal](#soal-praktikum-1)
  - [Penjelasan Singkat LMIS](#penjelasan-singkat-LMIS)
  - [Penyelesain](#penyelesaian-praktikum-1)
- [Praktikum 2](#praktikum-2)
  - [Penjelasan Singkat Permasalahan](#penjelasan-singkat-permasalahan)
  - [Penyelesain Praktikum 2](#penyelesaian-praktikum-2)
- [Referensi](#referensi)
 
## Praktikum 1

### Soal Praktikum 1
> Implemantasikan sebuah program untuk menyelesaikan permasalahan “Largest Monotonically Increasing Subsequence”

### Penjelasan Singkat LMIS
“Largest Monotonically Increasing Subsequence” adalah subsequence terpanjang dari suatu sequence yang elemen-elemennya meningkat secara monotonik. Untuk menyelesaikan permasalahan ini, kita dapat menggunakan algoritma Longest Increasing Subsequence (LIS) dengan kompleksitas waktu `O(N log N)` 

### Penyelesaian Praktikum 1
Berikut adalah implementasi algoritma LIS menggunakan bahasa pemrograman Python yang telah kami buat:

```ruby
from bisect import bisect_left

def lengthOfLIS(nums):
    n = len(nums)
    ans = [nums[0]]
    for i in range(1, n):
        if nums[i] > ans[-1]:
            ans.append(nums[i])
        else:
            low = bisect_left(ans, nums[i])
            ans[low] = nums[i]
    return len(ans)

nums = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of LIS is", lengthOfLIS(nums))
```

Implementasi di atas menggunakan pendekatan Binary Search untuk mencari subsequence terpanjang. Algoritma ini mempertahankan daftar “bucket” yang merepresentasikan subsequence yang valid. Daftar ini awalnya kosong dan diiterasi dari kiri ke kanan. Untuk setiap nomor dalam daftar, dilakukan langkah-langkah berikut:
- Jika nomor tersebut lebih besar dari elemen terakhir dari bucket terakhir (yaitu elemen terbesar dalam subsequence saat ini), maka nomor tersebut ditambahkan ke akhir daftar. Hal ini menunjukkan bahwa kita telah menemukan subsequence yang lebih panjang.
- Jika tidak, dilakukan pencarian biner pada daftar bucket untuk menemukan elemen terkecil yang lebih besar dari atau sama dengan nomor saat ini. Langkah ini membantu kita mempertahankan sifat elemen yang meningkat dalam bucket. Setelah menemukan posisi untuk diperbarui, elemen tersebut diganti dengan nomor saat ini. Hal ini menjaga bucket tetap terurut dan memastikan bahwa kita memiliki potensi untuk subsequence yang lebih panjang di masa depan 1.

## Praktikum 2

### Soal Praktikum 2
> Jika sebuah bidak kuda diletakkan pada sebarang kotak untuk kemudian melakukan perjalanan (dengan cara pergerakan kuda) mengunjungi ke semua (8x8) kotak papan catur. Jika diinginkan situasi bahwa kuda tsb dapat mengakhiri perjalnaan pada attacking square, mengakhiri perjalanan di sebarang kotak. Maka aplikasikan algoritma untuk menyelesaikan masalah diatas ke dalam sebuah program dengan menunjukkan rute perjanlanan seperti gambar kanan bawah

### Penjelasan Singkat Permasalahan
Berdasarkan soal masalah tersebut dikenal sebagai “Knight’s Tour Problem” dan dapat diselesaikan menggunakan algoritma backtracking. Algoritma backtracking adalah teknik rekursif yang digunakan untuk menyelesaikan masalah optimasi. Ini mencoba untuk membangun solusi secara inkremental, satu bagian pada satu waktu, sambil mempertimbangkan batasan masalah. Berikut adalah algoritma backtracking untuk menyelesaikan masalah Knight’s Tour:
- Mulai dari kotak awal.
- Jika semua kotak telah dikunjungi, kembalikan true.
- Untuk setiap langkah yang mungkin dari kotak saat ini, lakukan langkah berikutnya.
- Jika langkah berikutnya mengarah ke solusi, kembalikan true.
- Batalkan langkah dan coba langkah lainnya.
- Jika tidak ada langkah yang mungkin, kembalikan false.

### Penyelesaian Praktikum 2
Berikut adalah contoh kode Python yang mengimplementasikan algoritma backtracking untuk menyelesaikan masalah Knight’s Tour:

```ruby
def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1):
        return True
    return False

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()

def solveKT():
    board = [[-1 for i in range(N)]for i in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if(not solveKTUtil(board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(board)

def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == N*N):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if(solveKTUtil(board, new_x, new_y, move_x, move_y, pos+1)):
                return True
            board[new_x][new_y] = -1
    return False

N = 8
solveKT()
```

Berikut adalah penjelasan singkat dari setiap fungsi dalam program kami:
- `isSafe(x, y, board)` Fungsi ini memeriksa apakah langkah yang diambil oleh kuda masih berada di dalam papan catur dan kotak tersebut belum pernah dikunjungi sebelumnya.
- `printSolution(board)` Fungsi ini mencetak solusi Knight’s Tour pada papan 8x8. Setiap kotak yang dikunjungi akan dicetak dengan nomor langkah yang sesuai.
- `solveKT()` Fungsi ini menginisialisasi papan catur, daftar langkah kuda, dan memanggil fungsi solveKTUtil() untuk menyelesaikan masalah Knight’s Tour.
- `solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos)` Fungsi ini menggunakan algoritma backtracking untuk menyelesaikan masalah Knight’s Tour. Fungsi ini mencoba   setiap kemungkinan langkah kuda dan memeriksa apakah langkah tersebut mengarah ke solusi. Jika solusi ditemukan, fungsi akan mengembalikan True. Jika tidak, fungsi akan mencoba langkah lainnya.

## Referensi
### Referensi Soal Praktikum 1
- [sushiljacksparrow/Python_Practice](https://github.com/sushiljacksparrow/Python_Practice/blob/e59e4dae227d60b5b93f4f8371c287cc1fa41450/longest_bitonic_susequence.py)
- [GeeksforGeeks - Longest Monotonically Increasing Subsequence](https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n-simple-implementation/)
- [Stack Overflow - Obtaining the Longest Increasing Subsequence in Python](https://stackoverflow.com/questions/27324717/obtaining-the-longest-increasing-subsequence-in-python)
- [Stack Overflow - Largest Monotonically Increasing or Decreasing Subsequence](https://stackoverflow.com/questions/40337207/largest-monotonically-increasing-or-decreasing-subsequence)
- [GeeksforGeeks - Set Insert Function in C++ STL](https://www.geeksforgeeks.org/set-insert-function-in-c-stl/)
- [GeeksforGeeks - Longest Monotonically Increasing Subsequence N Log N](https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/)
- [Dynamic Programming 7 - Longest Increasing Subsequence](https://homepages.gac.edu/~sskulrat/Courses/2014F-375/lectures/dp7.pdf)

### Referensi Soal Praktikum 2
- [amenimethenni/AlgorithmesGenetiques](https://github.com/amenimethenni/AlgorithmesGenetiques/blob/010c1d89ea63d95641936387ff7b1fcfc791d19a/Knight's_Tour_Pb.py)
- [Muhammad-Osama31/AI-N-Queen-Probelm](https://github.com/Muhammad-Osama31/AI-N-Queen-Probelm/blob/30718960445832e8b86cb53e630413ec12c7f340/Knight.py)
- [huytran-cloud/TranDangHuy-C4T-A03](https://github.com/huytran-cloud/TranDangHuy-C4T-A03/blob/cfa4638ae6ee32af499569a30eeda62e87acafc4/TranDangHuy-C4T-A03/Chess-Knight/KnightsTour.py)
- [FedorBel/algorythms](https://github.com/FedorBel/algorythms/blob/d51ad4252b5b37b31765af4b5f16746f2675548f/knights_tour/knights_tour.py)
- [Tutorialspoint - The Knight's Tour Problem](https://www.tutorialspoint.com/The-Knight-s-tour-problem)
- [Runestone Academy - Implementing Knight's Tour](https://runestone.academy/ns/books/published/pythonds/Graphs/ImplementingKnightsTour.html)
- [Stack Overflow - Knights Tour Count Steps](https://stackoverflow.com/questions/39628430/knights-tour-count-steps-that-takes-to-go-from-a-to-b)
- [GeeksforGeeks - The Knight's Tour Problem](https://www.geeksforgeeks.org/the-knights-tour-problem/)
