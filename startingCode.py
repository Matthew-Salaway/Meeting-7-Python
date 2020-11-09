# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will code a password cracker with the skills we have developed through the previous lessons!

# We will allow the user to enter a password, and then have the program guess the password until it is correct

# First make the variable userPassword and ask the user to enter the password
userPassword = input("Enter your password: ")

# Now we will make the program guess the password
# We can do this by telling the program to come up with random combinations of letters
# And then check if the strings are equal

# The first version of the password cracker will only be letter combinations
# So, make an array of all the possible characters (just letters): Here it is because this is busy coding
# password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z']

# Lets first create the function randomPasswordCracker, with the parameter userPass
# Now create the variable: guess and store "" inside, so we can now compare the guess to the user password

# Think for a moment about the ways we could make the program concatenate letters and then guess the password
# There are many different algorithms, first lets make one that chooses them randomly.

# Lets make a while loop so that the program will keep guessing until it is the password entered by the user
# Then inside the while loop, make the program concatenate a string using the random module to randomly select
# letters from the password array, until it is the same length as the password the user entered
# Once the password and guess are the same, the while loop will break and the password has been cracked



# Now lets make it so the program systematically hits every possible combination in order.
# Think. How can we do this?
# We can make a loop for each letter in the word.
# First guess aaa, then aab, then aac... aba...baa...










# Now lets see which one is faster.
# Call on both functions, and make the program sleep for 2 seconds inbetween (import time)
