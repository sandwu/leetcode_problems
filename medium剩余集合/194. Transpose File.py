



#题意用shell颠倒文本数据

"""
Example:

If file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30


# Read from the file file.txt and print its transposed content to stdout.

cat file.txt | awk '{for(i=0;++i<=NF;)a[i]=a[i]?a[i] FS $i:$i}END{for(i=0;i++<NF;)print a[i]}'


"""