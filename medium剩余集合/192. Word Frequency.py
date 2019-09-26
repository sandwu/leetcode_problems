



#题意用shell实现读取文件word.txt，并统计里面的word的次数

"""
Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1




# Read from the file words.txt and output the word frequency list to stdout.


cat words.txt | sed 's/ /\n/g;' | sed '/^\s*$/D' | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'

First sed replaces all spaces with new lines.
Second sed deletes all whitespace-only lines
sort sorts all the words
uniq -c removes the duplicates and prefixes the frequency of each word
sort -nr sorts the input based on the frequency (-r is for descending order)
awk '{print $2 " " $1} reverses the ordering of frequency and word in a line

"""