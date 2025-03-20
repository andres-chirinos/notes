import random
import subprocess

def generate_random_vector(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def append_vector_to_file(filename, vector):
    with open(filename, 'a') as file:
        file.write(','.join(map(str, vector)) + '\n')

#if __name__ == "__main__":
#    lower_bound = 1
#    upper_bound = 100
#    max_size = 10000  # You can adjust this value as needed
#
#    for vector_size in range(10, max_size + 1, 10):
#        random_vector = generate_random_vector(vector_size, lower_bound, upper_bound)
#        append_vector_to_file('data.txt', random_vector)

def bubble_sort(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

def shell_sort(vector):
    n = len(vector)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = vector[i]
            j = i
            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j -= gap
            vector[j] = temp
        gap //= 2

def insertion_sort(vector):
    for i in range(1, len(vector)):
        key = vector[i]
        j = i - 1
        while j >= 0 and key < vector[j]:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = key

def selection_sort(vector):
    for i in range(len(vector)):
        min_idx = i
        for j in range(i+1, len(vector)):
            if vector[j] < vector[min_idx]:
                min_idx = j
        vector[i], vector[min_idx] = vector[min_idx], vector[i]

def quick_sort(vector):
    if len(vector) <= 1:
        return vector
    pivot = vector[len(vector) // 2]
    left = [x for x in vector if x < pivot]
    middle = [x for x in vector if x == pivot]
    right = [x for x in vector if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def execute_python_sort(sort_function, input_file, output_file, sort_name):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        for line in infile:
            vector = list(map(int, line.strip().split(',')))
            sorted_vector = sort_function(vector.copy())
            outfile.write(f'{sort_name},' + ','.join(map(str, sorted_vector)) + '\n')

if __name__ == "__main__":
    input_file = 'data.txt'
    output_file = 'time.csv'
    
    execute_python_sort(bubble_sort, input_file, output_file, 'bs')
    execute_python_sort(shell_sort, input_file, output_file, 'ss')
    execute_python_sort(insertion_sort, input_file, output_file, 'is')
    execute_python_sort(selection_sort, input_file, output_file, 'ss')
    execute_python_sort(quick_sort, input_file, output_file, 'qs')
    execute_java_script('VectorGenerator.java cli', input_file, output_file)

#Bubble Sort
#Shell Sort
#Insertion Sort
#Selection Sort
#Quick Sort
def execute_java_script(java_file, input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        for line in infile:
            process = subprocess.Popen(['java'] + java_file.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=line.encode())
            if stderr:
                print(f"Error: {stderr.decode()}")
            else:
                outfile.write('jv,'+','.join(stdout.decode().split()) + '\n')

if __name__ == "__main__":
    execute_java_script('VectorGenerator.java cli', 'data.txt', 'time.csv')