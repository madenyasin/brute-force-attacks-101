from string import ascii_letters
import time

def main():
    print("5 Karakter   |   Harfler (Büyük - Küçük)")
    password = input("Password: ")
    
    start_time = time.time() # Start the timer
    bruteForce(password)
    end_time = time.time() # Stop the timer

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print("İşlem süresi:", elapsed_time, "saniye")


def bruteForce(password, counter = 0):
    #   5 Karakter  |   Harfler (Büyük - Küçük) 
    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                for l in ascii_letters:
                    for m in ascii_letters:
                        print(i, j, k, l, m)
                        counter += 1
                        if password == i + j + k + l + m:
                            print("Done!")
                            print(f"{counter}. denemede sonuca ulaşıldı.")
                            return

if __name__ == "__main__":
    main()