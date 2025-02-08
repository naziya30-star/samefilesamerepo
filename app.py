import Azureprocess

# Function to calculate the square of a number
def square_number(number):
    print(f"The square of {number} is {number * number}")

def main():
    numbers = [1, 2, 3, 4, 5]
    
    # Creating a list to hold process objects
    processes = []

    # Creating and starting processes
    for number in numbers:
        process = multiprocessing.Process(target=square_number, args=(number,))
        processes.append(process)
        process.start()

    # Waiting for all processes to complete
    for process in processes:
        process.join()

    print("All processes have finished.")

if __name__ == "__main__":
    main()

