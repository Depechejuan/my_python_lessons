#Ways to import this package.
#Of course the file will have errors. Take it as notes

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# This way can be more readeable
from ecommerce.shipping import calc_shipping, calc_tax

calc_shipping()

#If you want to import the entire module
from ecommerce import shipping
shipping.calc_shipping()