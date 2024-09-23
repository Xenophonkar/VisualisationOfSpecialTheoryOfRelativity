import os
import datetime


#η εντολή σβήνει ένα αρχείο
#os.remove("paradeigma.txt")

#η εντολή αλλάζει ενα όνομα αρχείου απο Blind_Guardian_Lyrics.txt σε moyfa
#os.rename("Blind_Guardian_Lyrics.txt","moyfa.txt")

#η εντολή ελέγχει εαν υπαρχει το αρχείο moyfa και το εμφανίζει
print(os.path.exists("moyfa.txt"))

#η εντολή μας δίνει το μέγεθος ενός αρχείου και το εμφανίζει
print(os.path.getsize("moyfa.txt"))

#η εντολή μας δίνει την ημερομηνία τελευταις τροποποίησης ενός αρχείου και το εμφανίζει
#μας δίνει το αποτέλεσμα σε δευτερόλεπτα απο την 1η ιανουαρίου 1970 λεγεται timestamp
print(os.path.getmtime("moyfa.txt"))
timestamp=os.path.getmtime("moyfa.txt")
print(datetime.datetime.fromtimestamp(timestamp))

#η εντολή μας δείχνει εαν το αρχείο υπάρχει ή οχι
print(os.path.isfile("moyfa.txt"))

#η εντολή μας δείχνει το Path ενος αρχείου
print(os.path.abspath("moyfa.txt"))

#η εντολή μας δίνει το φάκελο που λειτουργεί αυτη τη στιγμή η python
print(os.getcwd())

#η εντολή δημιουργεί ένα καινούργιο φάκελο
#os.mkdir("New_dir")

#η εντολή μας μεταφέρει στο φάκελο που θέλουμε
os.chdir("New_dir")
print(os.getcwd())

#η εντολη διαγράφει ένα φάκελο
#os.rmdir("Newer_dir")

#η εντολή μας δείχνει τι περιέχει ένας φάκελος
print(os.listdir("Newer_dir"))

dir = "Newer_dir"

for  name in os.listdir(dir):#για καθε αντικείμενο στην λίστα
    fullname=os.path.join(dir, name)#το ονομα του αρχείου/φακελου δινεται απο την join ανεξάρτητα απο το λειτουργικο
    if os.path.isdir(fullname):#εαν το αρχειο ειναι φάκελος εκτυπώνει κάτι ενώ εάν είναι αρχείο κάτι άλλο
        print("{} is a directory".format(fullname))
    else:
        print ("{} is a file".format(fullname))

