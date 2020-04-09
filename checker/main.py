'''Check the Duplicate Files.'''
import os
import sys
import hashlib
import argparse


def calculate_hash(file):
    '''Calculates the hash of the file using SHA-256 hashing algorithm.'''

    # The size of each read from the file.
    block_size = 65536

    # Create the hash object using SHA-256 algorithm.
    file_hash = hashlib.sha256()

    # Open the file to read it's bytes.
    with open(file, 'rb') as file_operation:
        # Read from the file. Take in the amount declared above.
        file_block = file_operation.read(block_size)
        # While there is still data being read from the file.
        while len(file_block) > 0:
            # Update the hash
            file_hash.update(file_block)
            # Read the next block from the file.
            file_block = file_operation.read(block_size)

    # Return the HASH value.
    return file_hash.hexdigest()


def check_duplicate(current_path=None, check_hash=False):
    '''Checks the duplicate files.'''

    try:
        # Check if the path path exists.
        os.chdir(current_path)
    except IOError:
        print('Pass valid path and try again.')
        sys.exit()

    # List of file names.
    files_names = []
    # List of file hash values.
    files_hash_values = []

    # os.walk() returns root, directories(_) and filenames.
    for root, _, files in os.walk('.'):
        for filename in files:

            # Proper Formatting of path like "/home/arjun/Desktop/sample.sp"
            root_path = '' if root == '.' else f'{root}/'
            file_path = f'{os.getcwd()}/{root_path}{filename}'

            # Calculate the size of the file.
            hash_value = os.stat(file_path).st_size
            # Calculate the SHA-256 hash of the file.
            if check_hash:
                hash_value = calculate_hash(file_path)

            files_names.append(file_path)
            files_hash_values.append(hash_value)

    # Convert lists(files_names, files_hash_values) into a dictionary.
    files_info = dict(zip(files_names, files_hash_values))

    # Flipping the files_info dictionary to find dictionary keys with duplicate values.
    # See more on : https://stackoverflow.com/a/20672314/9755816

    flipped_info = {}
    for file_name, hash_value in files_info.items():
        if hash_value not in flipped_info:
            flipped_info[hash_value] = [file_name]
        else:
            flipped_info[hash_value].append(file_name)

    # Return the list of duplicate files.
    duplicate_files = []
    for hash_value, file_list in flipped_info.items():
        if len(file_list) > 1:
            duplicate_files.append(file_list)

    if len(duplicate_files) == 0:
        print('There are no duplicate files.')

    return duplicate_files


# Driver Code
parser = argparse.ArgumentParser(
    description='Checks the duplicates files in the system.')


parser.add_argument(
    '--check-hash',
    '-c',
    action='store_true',
    help='Compare by checking the SHA-256 hash of the files.\n Takes time for comparision.',
)

parser.add_argument(
    '--rename',
    '-r',
    action='store_true',
    help='Renames the duplicate file with suffix \'_DUPLICATE_{id}\' appended.'
)

parser.add_argument(
    '--path',
    '-p',
    nargs=1,
    help='Specify the root path to check the duplicate files.',
    type=str)

args = parser.parse_args()

filepath = args.path[0] if args.path else os.getcwd()

comparision_result = check_duplicate(
    filepath,
    check_hash=args.check_hash)


# Rename the duplicate files with suffix '_DUPLICATE_{id}' appended.
if args.rename:
    for count, duplicate in enumerate(comparision_result):
        for file_count, file in enumerate(duplicate):

            # Find the extension period location in the file name string if exists.
            period_location = file.find('.')
            if period_location != -1:
                filename, extension = file.split('.')
                filename = f'{filename}_DUPLICATE_{count+1}'
                final_filename = f'{filename}.{extension}'
                os.rename(file, final_filename)
            else:
                final_filename = f'{file}_DUPLICATE_{count+1}'
                os.rename(file, final_filename)

            # Update the new file name for printing.
            comparision_result[count][file_count] = final_filename

# Print the duplicate files.
print('\nThe list of duplicate files are : ')
for count, duplicate in enumerate(comparision_result):

    print(f'\nDuplicate File No. {count+1} : ')

    for file in duplicate:
        print(f'"{file}"')
