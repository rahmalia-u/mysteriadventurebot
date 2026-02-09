import time
import random

def print_dramatis(teks):
    """Fungsi untuk print teks dengan jeda 0.5 detik"""
    print(teks)
    time.sleep(0.5)

def cek_keberuntungan():
    """Random chance 30% untuk mendapat bonus keberuntungan"""
    return random.randint(1, 100) <= 30

def hitung_damage_random():
    """Damage bisa 20 (normal) atau 35 (critical hit)"""
    if random.randint(1, 100) <= 25:  # 25% critical hit
        return 35, True
    return 20, False

def cek_mood_boss():
    """Random mood boss: 'kejam' atau 'agak baik hati'"""
    return random.choice(['kejam', 'baik hati'])

def ascii_pedang_menang():
    """Tampilkan ASCII art pedang saat menang"""
    pedang = """
        ⚔️  KEMENANGAN! ⚔️
        
            |
            |
           /|\\
          / | \\
            |
            |
           ◯◯◯
          (███)
           ███
            |
            |
           |||
           |||
           / \\
          /   \\
    """
    print(pedang)
    time.sleep(1)

def ascii_tengkorak_kalah():
    """Tampilkan ASCII art tengkorak saat kalah"""
    tengkorak = """
        ☠️  KEKALAHAN! ☠️
        
          ╔═══╗
          ║ ● ║  ←← SKULL
          ║ ◉ ║
          ╚═╦═╝
            ║
          ╔═╩═╗
          ║███║
          ║███║
          ╚═══╝
           │ │
           │ │
    """
    print(tengkorak)
    time.sleep(1)

def game_utama():
    nyawa = 100
    print_dramatis("✨ --- MEMULAI PETUALANGAN DIGITAL --- ✨")
    print_dramatis("Selamat datang di dunia kode yang berbahaya!")
    nama = input("\n🎮 Siapa namamu, pemberani? ")
    print_dramatis(f"\n👋 Ayo {nama}! *tepuk tangan dramatis* 👏")
    print_dramatis(f"📊 Nyawa Awal: {nyawa} ❤️ (Semoga cukup!)")
    
    # Cek keberuntungan awal
    if cek_keberuntungan():
        print_dramatis("✨ WOW! Kamu merasakan aura keberuntungan! +10 BONUS HP!")
        nyawa += 10
        print_dramatis(f"Nyawa jadi: {nyawa} ❤️")
    else:
        print_dramatis("⚠️  Peringatan: Setiap pilihan salah = -20 HP (atau mungkin LEBIH!)")
    
    print_dramatis("\n🎲 INGAT: Ada elemen keberuntungan di setiap keputusan!")
    print_dramatis("\nKamu tiba di persimpangan dengan dua pintu misterius...\n")
    
    print_dramatis("🌳 Jalur 1: LEMBAH CODING")
    print_dramatis("   → Penuh ALGORITMA AJAIB & PENYIHIR ANEH 🧙‍♂️")
    print_dramatis("\n🏔️  Jalur 2: GUNUNG BUG")
    print_dramatis("   → Dipenuhi BUG GANAS & MAKHLUK DEBUG 🐛")
    
    pilihan = input("\nKe mana kamu ingin pergi? (Lembah Coding / Gunung Bug): ").strip()
    
    if pilihan.lower() == "lembah coding":
        cerita_lembah_coding(nama, nyawa)
    elif pilihan.lower() == "gunung bug":
        cerita_gunung_bug(nama, nyawa)
    else:
        damage, is_critical = hitung_damage_random()
        nyawa -= damage
        if is_critical:
            print_dramatis(f"\n💥 CRITICAL HIT! DAMAGE BERLIPAT GANDA!")
        print_dramatis(f"\n❌ SALAH! Pilihan yang valid hanya 'Lembah Coding' atau 'Gunung Bug'!")
        print_dramatis("🎪 SISTEM GAME: Kamu pilih hal yang tidak ada di dunia sini!")
        print_dramatis("Entitas Misterius: 'Error 404: Pilihan tidak ditemukan di dimensi ini!'")
        print_dramatis(f"💔 Nyawa berkurang {damage}! Sisa: {nyawa}❤️")
        if nyawa <= 0:
            print_dramatis("\n☠️  GAME OVER! NYAWA MU HABIS!")
            print_dramatis(f"Kesimpulan perjalanan {nama}:")
            print_dramatis("Kamu telah terlalu banyak membuat pilihan ANEH dan kalah dari petualangan ini!")
            print_dramatis("Better luck next time, junior developer! 👋😅")
            ascii_tengkorak_kalah()
        else:
            print_dramatis("Silakan coba jalur LAIN dengan lebih hati-hati...\n")
            game_utama()

def cerita_lembah_coding(nama, nyawa):
    print_dramatis(f"\n🌳 === LEMBAH CODING === 🌳")
    print_dramatis(f"❤️ Nyawa: {nyawa}")
    print_dramatis(f"\n{nama} melangkah ke lembah yang berpendar hijau...")
    print_dramatis("Pohon-pohon terbuat dari STACK dan QUEUE bergoyang aneh 😵")
    time.sleep(1)
    
    # Random power up sebelum bertemu boss
    if random.randint(1, 100) <= 40:  # 40% chance
        bonus_hp = random.randint(10, 25)
        nyawa += bonus_hp
        print_dramatis(f"\n🌟 Kamu menemukan POTION HP! +{bonus_hp} HP!")
        print_dramatis(f"Nyawa sekarang: {nyawa}❤️")
    
    print_dramatis("\n🧙‍♂️ TIBA-TIBA... Seorang penyihir aneh muncul!")
    print_dramatis("Penyihir: 'Halo! Nama ku Py Thon... ya, saya dari Monty Python! 🐍'")
    print_dramatis("Penyihir: 'Aku sedang STRESS membuat code, mau bantu?'")
    
    mood = cek_mood_boss()
    if mood == 'kejam':
        print_dramatis("Penyihir: 'Kamu hadapan ku dengan WAJAH GARANG!'")
        print_dramatis("Aura gelap mengelilinginya... Py Thon sedang dalam mood KEJAM!")
    else:
        print_dramatis("Penyihir: 'FYI: Aku sudah debug 47 kali tapi tetap error! 😭'")
        print_dramatis("Dia terlihat agak menyesal... mungkin akan sedikit baik hati?")
    
    print_dramatis("\n⚠️  Py Thon memberi KUIS CODING PERTAMA!")
    print_dramatis("Pertanyaan: Berapa output dari: print(2 + 2 * 2)? (A/B/C)")
    print_dramatis("A) 6  |  B) 8  |  C) Mungkin galaxi lain punya jawabannya")
    jawab = input("\n🎯 Pilihan kamu: ").upper().strip()
    
    if jawab == "A":
        print_dramatis("\n✅ BENAR! Kamu mengerti operator precedence!")
        print_dramatis("Py Thon: 'Wah, cerdas! Ada soal lagi nih untuk mu...'")
        print_dramatis("Py Thon: 'Jika kamu jawab benar, harta karun menanti!'")
    else:
        damage, is_critical = hitung_damage_random()
        nyawa -= damage
        
        if is_critical:
            print_dramatis(f"\n💥 CRITICAL HIT! Py Thon SANGAT MARAH!")
            if mood == 'kejam':
                print_dramatis("Py Thon (yang SUDAH kejam): 'NYAHAHAHA SALAH BANGET!'")
            print_dramatis(f"Damage berlipat ganda! -{damage} HP!")
        else:
            print_dramatis(f"\n❌ SALAH! '{jawab}' bukan jawaban yang valid LOL")
            if mood == 'kejam':
                print_dramatis("Py Thon: 'HAHAHA! Kamu sungguh bodoh!'")
            else:
                print_dramatis("Py Thon: 'Eh, coba lagi sih... tapi kena deh -20 HP'")
        
        print_dramatis(f"💔 Nyawa turun {damage}! Sisa: {nyawa}❤️")
        ascii_tengkorak_kalah()
        return nyawa
    
    # PERTANYAAN KEDUA - Setelah jawab benar pertanyaan pertama
    print_dramatis("\n📚 Py Thon: 'Soal berikutnya... Apa itu recursion?'")
    print_dramatis("A) Function yang memanggil dirinya sendiri")
    print_dramatis("B) Function yang memanggil function lain")
    print_dramatis("C) Function yang dipuji orang")
    jawab2 = input("\n🎯 Pilihan kamu: ").upper().strip()
    
    if jawab2 == "A":
        print_dramatis("\n✅ BENAR LAGI! Kamu jenius!")
        print_dramatis("Py Thon: 'Kamu menguasai coding! Tapi... ada ANCAMAN di gunung...'")
        print_dramatis("Py Thon: 'Debug Bugs sedang mengincarmu! Ingin peringatan?'")
        
        print_dramatis("\n🔓 PERCABANGAN: Pilih strategi kamu!")
        print_dramatis("1) Tetap di Lembah dan ambil harta karun Python 💎")
        print_dramatis("2) Pergi ke Gunung Bug untuk hadapi Debug Master 🏔️")
        pilihan = input("\n🎯 Pilihan kamu (1/2): ").strip()
        
        if pilihan == "1":
            print_dramatis("\n🐍 Kamu mengambil harta karun Python dengan aman!")
            print_dramatis("Py Thon: 'Selamat! Kamu sudah master di bidangku!'")
            print_dramatis("Kamu berhasil meninggalkan lembah dengan harta karun Python! 🐍💎")
            ascii_pedang_menang()
        else:
            print_dramatis("\n⚠️  Kamu berniat ke Gunung Bug untuk verifikasi final!")
            print_dramatis("Py Thon: 'Berani! Okay, tapi jadilah hati-hati...'")
            cerita_gunung_bug(nama, nyawa, from_lembah=True)
    else:
        damage, is_critical = hitung_damage_random()
        nyawa -= damage
        print_dramatis(f"\n❌ SALAH!")
        print_dramatis("Py Thon: 'Tahu kan recursion adalah concept penting!'")
        print_dramatis(f"💔 Nyawa turun {damage}! Sisa: {nyawa}❤️")
        ascii_tengkorak_kalah()
    
    return nyawa

def cerita_gunung_bug(nama, nyawa, from_lembah=False):
    print_dramatis(f"\n🏔️  === GUNUNG BUG === 🏔️")
    print_dramatis(f"❤️ Nyawa: {nyawa}")
    print_dramatis(f"\n{nama} mulai mendaki gunung yang terjal...")
    
    if from_lembah:
        print_dramatis("\n💡 Py Thon memberimu PETUNJUK RAHASIA sebelum pergi!")
        print_dramatis("Py Thon: 'Historis bug paling terkenal adalah... Moth 1947!'")
        print_dramatis("🎁 Bonus: Kamu sudah tahu jawabannya! Hehe 😉")
        bonus_hp = random.randint(20, 30)
        nyawa += bonus_hp
        print_dramatis(f"✨ Bonus HP dari Py Thon! +{bonus_hp} HP!")
        print_dramatis(f"Nyawa sekarang: {nyawa}❤️")
    
    # Random encounter sebelum boss
    encounter = random.choice(['aman', 'sesat', 'harta'])
    if encounter == 'sesat':
        print_dramatis("\n⚠️  KAMU SESAT DI GUNUNG! -15 HP!")
        nyawa -= 15
        print_dramatis(f"Nyawa sekarang: {nyawa}❤️")
    elif encounter == 'harta':
        bonus = random.randint(15, 30)
        nyawa += bonus
        print_dramatis(f"\n🪙 KAMU TEMUKAN HARTA KARUN! +{bonus} HP!")
        print_dramatis(f"Nyawa sekarang: {nyawa}❤️")
    
    print_dramatis("\nTiba-tiba RIBUAN bug terbang mengelilingi! 🐛🐛🐛")
    print_dramatis("Mereka berteriak dalam bahasa biner yang menakutkan: 01010101!")
    time.sleep(1)
    
    print_dramatis("\n👹 MAKHLUK DEBUG MUNCUL DENGAN RAHANG YANG MENGANGA!")
    print_dramatis("Debug Master: 'SELAMAT DATANG DI NERAKA GIT CONFLICT! 🔥'")
    print_dramatis("Debug Master: 'Ada 100 bug di sini, coba tebak jenis bug apa?'")
    
    mood = cek_mood_boss()
    if mood == 'kejam':
        print_dramatis("Debug Master: 'BERSIAPLAH UNTUK DITAKLUKKAN!'")
    else:
        print_dramatis("Debug Master: '(Hint: Tebakan salah = dijadiin stack overflow!)'")
    
    print_dramatis("\n⚠️  DEBUG MASTER MEMBERI TANTANGAN!")
    print_dramatis("Pertanyaan: Bug paling FAMOUS di dunia programming? (A/B/C)")
    print_dramatis("A) Moth dari tahun 1947 (di komputer Mark II) 🦋")
    print_dramatis("B) Y2K Bug - komputer paranoid tahun 2000")
    print_dramatis("C) BUG di game favorit saya")
    jawab = input("\n🎯 Pilihan kamu: ").upper().strip()
    
    if jawab == "A":
        print_dramatis("\n✅ BENAR! Itu bug LEGENDARIS!")
        print_dramatis("Debug Master: 'Wow! Kamu tahu sejarah bug! Patut dihargai!'")
        print_dramatis("🐛 Bug-bug yang menakutkan tadi terbang pergi menghormati mu!")
        
        if from_lembah:
            print_dramatis("\n✨ Debug Master: 'Py Thon sudah memberitahu mu ya?'")
            print_dramatis("Debug Master: 'Bagus! Ke dua cabang pengetahuan telah kau kuasai!'")
            print_dramatis("🎁 ULTIMATE POWER UNLOCKED! Kamu ditetapkan sebagai MASTER DIGITAL! 🏆")
            ascii_pedang_menang()
        else:
            print_dramatis("\n🎁 Kamu mendapat BADGE MASTER DEBUGGING!")
            print_dramatis("Kamu menaklukkan gunung dengan penuh kemenangan! 🏆")
            ascii_pedang_menang()
    else:
        damage, is_critical = hitung_damage_random()
        nyawa -= damage
        
        if is_critical:
            print_dramatis(f"\n💥 CRITICAL HIT! SEMUA BUG MENYERANG!")
            if mood == 'kejam':
                print_dramatis("Debug Master: 'NYAHAHAHA TAK AMPUN!'")
            print_dramatis(f"Damage berlipat ganda! -{damage} HP!")
        else:
            print_dramatis(f"\n❌ SALAH! Itu bukan sejarah bug LEGENDARY!")
            if mood == 'kejam':
                print_dramatis("Debug Master: 'HAHAHAHA! SEKARANG MATI!'")
            else:
                print_dramatis("Debug Master: 'Ehh, sayang sekali. Tapi -20 HP deh.'")
        
        print_dramatis(f"🐛 BUG-BUG terbang menyerbu dan mencuri {damage} HP!")
        print_dramatis(f"💔 Nyawa turun {damage}! Sisa: {nyawa}❤️")
        
        if from_lembah:
            print_dramatis("\nDebug Master: 'Bahkan dengan petunjuk Py Thon pun kamu salah!'")
            print_dramatis("Kamu berlari turun gunung DENGAN RASA MALU BERLIPAT GANDA! 😱😭")
        else:
            print_dramatis("Kamu berlari turun gunung sambil dikejar bug-bug marah 😱")
        ascii_tengkorak_kalah()
    
    return nyawa
    
def main():
    """Main loop dengan opsi main lagi"""
    main_lagi = True
    while main_lagi:
        game_utama()
        
        # Tanyakan apakah pemain ingin main lagi
        print_dramatis("\n" + "=" * 50)
        jawab = input("🎮 Main lagi? (y/n): ").strip().lower()
        
        if jawab == 'y' or jawab == 'yes':
            print_dramatis("\n🚀 Memulai petualangan baru...!\n")
            main_lagi = True
        else:
            print_dramatis("\n👋 Terima kasih telah bermain! Sampai jumpa, developer muda!")
            print_dramatis("🎊 GAME OVER - Terima kasih telah menyelesaikan petualangan digital! 🎊")
            main_lagi = False

if __name__ == "__main__":
    main()