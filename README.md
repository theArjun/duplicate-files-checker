# Duplicate Files Checker

Checks the duplicates file in the system.

### Inspiration and Approach Used

In a large collection of files there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for these duplicates.

1. A program that walks a directory and all of its sub-directories for all files with a given suffix (like .mp3) and lists pairs of files with that are the same size. Hint: Use a dictionary where the key of the dictionary is the size of the file from os.path.getsize and the value in the dictionary is the path name concatenated with the file name. As you encounter each file check to see if you already have a file that has the same size as the current file. If so, you have a duplicate size file and print out the file size and the two files names (one from the hash and the other file you are looking at).

2) Adapt the previous program to look for files that have duplicate content using a hashing or checksum algorithm. 

You should create a dictionary where the checksum is the key and the file name is the value. When you compute a checksum and it is already in the dictionary as a key, you have two files with duplicate content so print out the file in the dictionary and the file you just read.
