#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import json

# Main part of the program
if __name__ == '__main__':

    # [1] is limit
    # [2] is lower_bound

    # Set up defaults:
    # limit is 100
    # lower_bound is 0
    try:
        if len(sys.argv) < 3:
            if len(sys.argv) < 2: 
                limit = 100
            else:
                limit = sys.argv[1]  
            lower_bound = 0
        else:
            limit = sys.argv[1]
            lower_bound = sys.argv[2]
    except:
        print ("Failed to retrieve arguments.")        

    # Now trying to get_producers
    try:
        
        api_endpoint = 'http://mainnet.eoscannon.io'

        api_request = '/v1/chain/get_producers'

        url = api_endpoint + api_request

        parameters = '''{
            "limit": {limit},
            "lower-bound": {lower_bound},
            "json": true,
            }'''

        # No time for prettiness, sorry!

        print(json.dumps(requests.post(url=url, data=parameters).json(), indent=2))

    except:
        print ("Failed to retrieve info.")

    finally:
        exit(0)