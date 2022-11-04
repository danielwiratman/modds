# Motorcycle Drowsiness Detection System

## Our Team:
- Filipus Dani Astono
- Pegasus Violin Surjaningtyas

## Taken from our proposal's abstract:  
Pada proyek ini, kami mengusulkan sebuah sistem pendeteksi kantuk pengendara roda dua
menggunakan kamera yang bernama MoDDS (Motorcyclist Drosiness Detection System). Algoritma
yang diusulkan mendeteksi kedipan mata pengendara dan memperkirakan kondisi kesadaran
pengendara berdasarkan interval dan frekuensi kedipan. Untuk mendeteksi kedipan, algoritma
menggunakan pelacak ROI (Region of Interest) untuk mendapatkan gambar mata dan algoritma CSRT
yang menghasilkan nilai SLC (Single-Linkage Clustering) yang dapat mengidentifikasi bukaan mata.
CSRT tracker adalah implementasi C++ dari CSR-DCF (Channel and Spatial Reliability of Discriminative
Correlation Filter). Algoritma yang diusulkan memberikan kinerja waktu nyata yang dapat dijalankan
pada perangkat yang disematkan. Untuk prototipe MoDDS, kami menggunakan papan pengembang
Raspberry Pi 4B sebagai prosesor utama yang memproses gambar dari Raspberry Pi Camera V2.1.

## Images

![image](https://user-images.githubusercontent.com/74503671/199908154-dd419582-d4b6-4435-b445-7cc1ef079a1a.png)
