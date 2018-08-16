
# ==================
# 16_Tuples.py
# ==================


# Tuple is an ordered set of data
# Tuples are similar to list but they are immutable.
# Immutable means that they cannot be changed.
# e.g. if you attempt to append and item to a tuple will give error
# Commas are used to separate the elements of a tuple
# Parenthesis () are not required but are used to remove any
# syntactic ambiguity

# Here is an example

myTuple1 = "a", "b", "c" # Tuple not enclosed in ()
myTuple2 = ("a", "b", "c") # Tuple enclosed in ()

print(myTuple1) # results are in bracket signifying it is a tuple
print(myTuple2) # results are in bracket signifying it is a tuple

print("="*20)

# Results for this are also in bracket showing it is a tuple
# This means you have to add the extra () to signify a tuple

print(("a", "b", "c"))
print("="*20)

# # If you don't put extra (), it will just print the values

print("a", "b", "c")
print("="*20)

# Note that tuples are different from string variables.
# a string is enclosed whole in quotes "" or ''
# But a tuple is an ordered set of data, hence each set enclosed
# in its own "" or ''

myVariable = ("a, b, c")
print("This is a variable: {}".format(myVariable))
print("="*20)



# Slicing in tuples
# here we have example of a tuple

myMovie1 = "Zootopia", "for kids", "2016"
print(myMovie1) # Prints the whole tuple.
print()

# # Now we do slicing, starting from first element

print(myMovie1[0]) # Element 0 is Zootopia
print(myMovie1[1]) # Element 1 is for kids
print(myMovie1[2]) # Element 2 is 2016
print("="*20)

# Since tuples are immutable (cannot be changed), any attempt to
# change them will result in error
# If we try to change element 0 (Zootopia) to say Shrek, it gives error
# Error message is "tuple object does not support item assignment"

# myMovie1[0] = "Shrek" # this will give error

# ==================================================
# How to change tuples using slicing and indexing:
# ==================================================

# Tuples support indexing and slicing and this can be used to update a tuple
# Example, we can change myMovie1 as follows
# A tuple still cannot be changed once created, but you can assign a
# variable with a new object of that type (tuple)

print(myMovie1) # Shows current myMovie1
print()

# This changes myMovie1 to say for adults
# Here "changedMyMovie1" is assigned first item from myMovie1, then "for adults",
# then 3rd item from myMove1

changedMyMovie1 = myMovie1[0], "for adults", myMovie1[2]
print(changedMyMovie1)

# We can also change the movie name to Shrek

changedMyMovie1 = "Shrek", myMovie1[1], myMovie1[2]
print(changedMyMovie1)

print("="*20)

# you can also use same name of the tuple.
# Note that the expressions on the right side of = are evaluated
# before the left hand side.
# So in this case, we are taking the first index of myMovie1, then
# add it to "for adults" then the 3 element of myMovie1
# So now the variable myMovie1 is assigned to the new results on the
# right side of assignment =
# so the variable is mutable, but tuple object that it is assigned
# to is immutable

myMovie1 = myMovie1[0], "for adults", myMovie1[2]
print(myMovie1)
print("="*20)


# Note that "lists" are mutable (Can be changed)
# We will show an example of how a list can be changed

print("Changing lists:")
print()
myMovieList1 = ["ZootopiaList", "for kids", "2016"]
print(myMovieList1) # This shows the original list
print()

# now we want to change list to say "for adults"
myMovieList1[1] = "for Adults"
print(myMovieList1) # Now you can see this has been changed to for adults

print("="*20)


# Why we prefer to use tuples over lists
# (1) We will cover hashes and dictionaries later, but one reason to
# use tuples over lists is that a dictionary key requires immutable object

# (2) Also a list is intended (though not enforced) to contain items of
# the same kind i.e. homogenous items
# Tuples are intended to hold heterogeneous items

# (3) Tuples provide protection to your data because they are immutable
# hence cannot be changed by error.



# how to assign values to a variable

# Assigning same value to different variables
# Note that the right hand side of = is evaluated first
# so 12 is assigned to d first, then to c to b to a

print("Assigning values to variables:")
print()
a = b = c = d = 12
print(a, b, c, d) # All variables are assigned 12

# Assigning different values to different variables

a, b = 12, 13 # This assigns different values to a and b
print(a, b)

# We can also use current values (12 and 13) and reverse them
# This works because the right side is evaluated first.
# so original a is assigned to new b and original b assigned to new a

a, b = b, a
print(a, b)
print("="*20)

# =====================
# UNPACKING THE TUPLE:
# =====================

# Note that "a, b = 12, 13" looks like a tuple
# This means we can assign the elements of a tuple in a single assignment
# We will use our original tuple here

print("Unpacking a tuple:")
print()

myMovie1 = "Zootopia", "for kids", "2016"
print(myMovie1)
print()

# Here we assign contents of myMovie1 tuple to the three variables
# title, forWho and year.
# This is called unpacking the tuple

print("Unpacked tuple:")
title, forWho, year = myMovie1
print(title) # prints individual elements
print(forWho)
print(year)
print()

print(title, forWho, year) # Can print it all in one line
print()

print("="*20)

# ============================================================
# Reason why we prefer tuples (immutable) vs lists (mutable):
# ============================================================

# we will create list myList1
print("tuples (immutable) vs lists (mutable):")
print()

myList1 = ["shrek", "for Kids", "2015"] # a list - uses [ ]
print(myList1)
print()

# Now since lists are mutable, we will append "good movie"

print("Append 'good movie':")
myList1.append("good movie")
print(myList1) # output here shows "good movie is appended to list.
print()

# Now Lets try to unpack the appended myList1
# This unpacking goes well because we have 4 objects to unpack and
# assigned them to 4 variables.

title, artist, year, review = myList1
print(title)
print(artist)
print(year)
print(review)

print("="*20)

# Problem with list comes if someone thought myList1 was the original
# one with three objects, then tries to unpack it into 3 variables
# This will give an error saying too many values to unpack (expects 3)
# This is why we prefer to use tuples which are immutable to avoid errors


print("Unpack myList1 into 3 variables:")
print()
print(myList1)  # prints whole list

# This gives error message" "ValueError: too many values to unpack (expected 3)"

# title, artist, year = myList1
# print(title)
# print(artist)
# print(year)

print("="*20)

# NOTE: If you try to append to a tuple, you get error saying
# tuple object has no attribute append

# print("Append to tuple:")
# print()
#
# myMovie1 = "Zootopia", "for kids", "2016"
# myMovie1.append("Very Good")

# ===================
# Tuples in a Tuple
# ===================

# A Tuple can contains elements that are themselves tuples
# We are going to create tuple named snoopSong1 with attributes
# Title, Artist, year and tracks
# NOTE the 4th tuple (tracks) is iself a tuple. hence tuple in tuple

snoopSong1 = "Doggy Style", "Snoop Dogg", 1998, (
    (1, "who am I"), (2, "Whats my Name"), (3, "Gin and Juice")
)
print(snoopSong1) # This prints the whole tuple
print()

# Now we will unpack snoopSong1 and print them one by oe
# we see that tracks is returned as a tuple in its own right.
# Note that we enclose e.g. (1, "who am I") in brackets so that python
# knows there are 4 tuples in tracks, and not 8

title, artist, year, track = snoopSong1
print(title)
print(artist)
print(year)
print(track)

print("="*20)

# Here is an example of output if you don't enclose the 4th tuple
# in individual brackets, the result we get for the 4th tuple
# is a tuple with 6 entries, numbers and songs

print()
snoopSong2 = "Doggy Style", "Snoop Dogg", 1998, (
    1, "who am I", 2, "Whats my Name", 3, "Gin and Juice"
)

title, artist, year, track = snoopSong2
print(title)
print(artist)
print(year)
print(track)

print("="*20)

# We can also be able to extract individual tracks as follows
# Note the \ after 1998 comes on its own when you hit enter to go to
# new line. Ignore it.

print()
snoopSong3 = "Doggy Style", "Snoop Dogg", 1998, \
             (1, "who am I"), (2, "Whats my Name"), (3, "Gin and Juice")


print(snoopSong3) # This prints the whole tuple
print()

# The downside of this unpacking is you need to know the number
# of tuples to unpack, otherwise you get an error if you unpack too
# many or too few

title, artist, year, track1, track2, track3 = snoopSong3
print(title)
print(artist)
print(year)
print(track1) # pulls track 1
print(track2) # pulls track 2
print(track3) # pulls track 3

print("="*20)


# Tuples challenge
# Given the tuple below that represents the Imelda May album "More Mayhem"
# Write code to print the album details followed by listing of all the tracks in the album
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with comma)

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town walz"))

print(imelda)
print()
print("Album: {}".format(imelda[0]))
print("Title: {}".format(imelda[1]))
print("Year: {}".format(imelda[2]))
print("Tracks:")
track1, track2, track3, track4 = imelda[3]
print(track1)
print(track2)
print(track3)
print(track4)

print("="*20)

# # You can do same thing above using for loop


print("Method 2 using for loop for 4th element")
print()

# We unpack tuple imelda and assign it to 4 variables
# Note that track will itself contain a tuple
title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track) # This has a tuple in itself

print()

# We want to use a for loop to print the elements in tuple track
# We also add tab ("\t") to the print to tab the results
# This prints track as a tuple

for song in track:
    print("\t", song)

# if we want to print the tracks individually, we can do as follows
print()
for song in track:
    trackNumber, title = song # unpacks tuple song into two elements, then we print them
    print("\tTrack Number: {}, Title: {}".format(trackNumber, title))

print("="*20)


# A tuple is immutable (cannot be changed)
# But if a tuple contains a list as one of its elements, the list itself can be changed
# 4th element in tuple imelda is a list because it is enclosed in []
# Tuple imelda itself has 4 objects, and that cannot be changed.

imelda = "More Mayhem", "Imelda May", 2011, [
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town walz")]

print("initial imelda")
print(imelda) # initial imelda
print()

# But we can change the 4th element which is a list by appending a new track to it.
imelda[3].append((5, "All of you"))
print("second imelda")
print(imelda) # Second imelda. We see it prints the updated track


title, artist, year, track = imelda
track.append((6, "Eternity"))
print()
print("Third imelda")
print(imelda) # Third imelda. We see it prints the updated track

# Now we can print the third imelda one line at a time
print()
print("Third imelda one line at a time")
print(title)
print(artist)
print(year)
print()

# We want to use a for loop to print the elements in tuple track
# We also add tab ("\t") to the print to tab the results
# This prints track as a tuple

for song in track:
    print("\t", song)


