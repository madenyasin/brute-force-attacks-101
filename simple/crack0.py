from string import digits
import time

def main():
    print("4 Karakter   |   Rakamlar")
    password = input("Password: ")

    start_time = time.time() # Start the timer
    bruteForce(password)
    end_time = time.time() # Stop the timer

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print("İşlem süresi:", elapsed_time, "saniye")


def bruteForce(password, counter = 0):
    # 4 Karakter | Rakamlar
    for i in digits:
        for j in digits:
            for k in digits:
                for l in digits:
                    print(i, j, k, l)
                    counter += 1
                    if password == i + j + k + l:
                        print("Done!")
                        print(f"{counter}. denemede sonuca ulaşıldı.")
                        return


if __name__ == "__main__":
    main()