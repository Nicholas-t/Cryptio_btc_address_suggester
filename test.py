# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr
import Bitcoin_address_suggester.viz_v2 as viz


#antoine's xpub address for testing

addresses=['32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp',    #OK
           '3HsVXJadDZFRwQCfVFNHeornRkmZaVcDzP',
           '37ASdZj1gC3qKS1vLMLDQS2MdZTdYN1Kbi',
           '3GARffqjDk5LgfCUhx3L6nCk7dVEwEPUaN']
    
#addresses = sgstr.suggest('1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7').keys()
viz.plot_from_first('32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp', addresses)

"""
chances of errors:
    new innovative wallet anonymity method to better anonymize the person
"""