def outfit_counter(tops, bottoms, dresses):
    outfits = (tops * bottoms) + dresses
    print "You have packed %s outfits. \n" % (outfits)
    if dresses >= tops*bottoms:
        print "%s of your outfits are dresses.\n" % (dresses)
    return outfits

tops = float(raw_input("How many tops? "))
bottoms = float(raw_input("How many bottoms? "))
dresses = float(raw_input("How many dresses? "))
outfits = int(outfit_counter(tops, bottoms, dresses))

days = int(raw_input("How many days are you packing for? "))
laundry_trips = days / outfits
if days <= outfits:
    print "You will not need to do laundry."
elif days % outfits == 0:
    print "You will need to do laundry %s times." % (laundry_trips - 1)
else:
    print "You will need to do laundry %s times." % (laundry_trips)

#laundry = int(raw_input("How many times will you do laundry? "))
#if laundry == 0:
 #   laundry = 1
  #  print "If you don't do laundry, you will have %s outfits." % (outfits)
#else:
 #   print "If you do laundry %s times, you will have %s outfits." % (laundry, (laundry+1)*outfits)
