This is a proof of concept for the Multilin Switch Denial of Service. 

I had previously stated the only mitigation was to turn off the webserver. 

This was a mistake, Garrettcom have issued a more robust fix that handles the memory corruption ;)

This will also be rolled into the GE firmware, but we are waiting on a report that states this more clearly.

This DOS is likely to affect 7/9 of the GE Multilin family, but also very likely to affect
the Garretcom Magnum6K family. I waited one year before releasing this script to the community.
I am still conflicted about it, but the important factor here is that customers can judge the severity of the issue themselves by using this test script in their own safety testing labs.

https://ics-cert.us-cert.gov/advisories/ICSA-15-013-04A
https://www.gedigitalenergy.com/products/support/multilink/MLSB1214.pdf
http://www.garrettcom.com/techsupport/MNS6K_R456_Release_Notes.pdf
