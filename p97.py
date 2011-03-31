#!/usr/bin/env python

import time
st = time.time()

result = (28433 * 2**7830457 + 1) % (10**10)
print str(result)[-10:]

print "Time taken: %s" % str(time.time() - st)
