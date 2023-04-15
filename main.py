# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ly6mQKASQUjlRR5pDjZgvOc7lQLIXX50
"""

from modul import Transaction

t1 = Transaction()

t1.tambah_item('ayam goreng', 2, 20000)
t1.tambah_item('pasta gigi', 3, 15000)

t1.check_data_item()

t1.delete_item('pasta gigi')

t1.check_data_item()

t1.reset_belanjaan()

t1.check_data_item()

t2 = Transaction()

t2.tambah_item('ayam goreng', 2, 20000)
t2.tambah_item('pasta gigi', 3, 15000)
t2.tambah_item('mainan mobil', 1, 200000)
t2.tambah_item('mi instant', 5, 3000)

t2.check_data_item()

t2.discount_checkout()