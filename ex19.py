#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print "You have %d cheeses!" % cheese_count
#    print "You have %d boxes of crackers!" % boxes_of_crackers
#    print "Man that's enough for a party!"
#    print "Get a blanket. \n"

#print "We can just give the function numbers directly:"
#cheese_and_crackers(20,30)



#print "OR, we can use variables from our script:"
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)


#print "And we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def outfit_counter(tops, bottoms, dresses):
    outfits = (tops * bottoms) + dresses
    print "You have packed %s outfits. \n" % (outfits)
    if dresses >= tops*bottoms:
        print "%s of your outfits are dresses.\n" % (dresses)
    return outfits

#outfit_counter(2, 2, 5)

#tops = 4
#bottoms = 1
#dresses = 0
#outfit_counter(tops, bottoms, dresses)

tops = int(raw_input("How many tops? "))
bottoms = int(raw_input("How many bottoms? "))
dresses = int(raw_input("How many dresses? "))
outfits = outfit_counter(tops, bottoms, dresses)

laundry = int(raw_input("How many times will you do laundry? "))
if laundry == 0:
    laundry = 1
    print "If you don't do laundry, you will have %s outfits." % (outfits)
else:
    print "If you do laundry %s times, you will have %s outfits." % (laundry, (laundry+1)*outfits)
