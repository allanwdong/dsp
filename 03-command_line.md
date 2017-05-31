# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  
pwd:  show current working directory path
mkdir: creating a directory
rm: deletes file
rm -r: deletes directory and everything inside it (CAN NOT UNDO)
cd: change directory
cd ..: go up to previous directory
ls: list files in directory
ls -a: list files + hidden files in directory
ls -l: list all content in long format
ls -t: order files and directories by time they were last modified
[can use order such as 'ls -alt' and system will recognize]
touch: create file
cp [a] [b] [c]: copies contents of [a] and [b] into [c]
mv [a] [b] [c]: movies files [a] and [b] into [c]
mv [a] [b]: changes name of file [a] to file [b] (technically moves file [a] into argument [b])


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  - list files/directories in directory
`ls -a`  - list everything in directory, including hidden files
`ls -l`  - list long format of files/directories in directory
`ls -lh`  - list long format of files/directories in directory, with readable file size units
`ls -lah` - list long format of all files/directories in directory, with readablefile size units
`ls -t`  - list files/directories in directory ordered by time, newest first
`ls -Glp`  - list long format of files/directories, with directories ended with '/' symbol, with files and directories differently colored


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -G` - differentiate btw files and directories easily by coloring the names differently
`ls -lh`  - list long format of files/directories in directory, with readable file size units
`ls -R` - list recursive directory tree
`ls -S` - sorts list by file size
`ls -t` - sorts list by date modified, newest first

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` is used to add the output of ther standard inout to the end of the second command.

`find ~/ds/metis/metis/metisgh/ -name "prework" | rm "dsp"`
 

