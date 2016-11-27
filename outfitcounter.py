def outfit_counter(tops, bottoms, dresses):
    outfits = (tops * bottoms) + dresses
    print "You have packed %s outfits. \n" % (outfits)
    if dresses >= tops*bottoms:
        print "%s of your outfits are dresses.\n" % (dresses)
    return outfits

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
