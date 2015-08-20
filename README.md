This is a proof of concept for the Multilin Switch Denial of Service. 
Apparently the mitigation to this DOS is to turn off the HTTPS management interface and use telnet for managing the device or perhaps GE Enervista software.
This DOS is likely to affect 7/9 of the GE Multilin family, but also very likely to affect
the Garretcom Magnum6K family. I waited one year before releasing this script to the community.
I am still conflicted about it, but the important factor here is that customers can judge the severeity of the issue themselves by using this test script in their own safety testing labs.

I feel a year of coordinating with ICS-CERT and GE & Garretcom is sufficient for them to complete their fixes and inform their customers. I leave it as an exercise to the reader to decide if this 
vuln report captures the effects of this code (and yes, they were given the code being released here).

https://ics-cert.us-cert.gov/advisories/ICSA-15-013-04A

Let the community of users decide if network downtime is acceptable in the environments these switches operate in. Thanks to ICS-CERT for their time and effort coordinating with both myself and the vendor.
