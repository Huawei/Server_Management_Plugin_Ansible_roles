#!/usr/bin/python

import json


def hsu(output_str=''):
    '''
    convert Huawei Server Upgrade Tool output to json
    '''
    output = json.loads(output_str)
    if output:
        if output['rc'] == 0:
            return output['data']
        else:
            return output['msg']

    return None


# def plain(drivers):
#     '''
#     convert drivers to plain string
#     '''
#     import itertools
#     if drivers and len(drivers) > 0:
#         flattened_list = list(itertools.chain(*drivers))
#         return ' '.join(['"{0}"'.format(item) for item in flattened_list])
#     else:
#         return ''

def plain(drivers, inbands, outbands):
    '''
    convert drivers to plain string
    '''
    import itertools
    merged = []
    merged.extend(drivers if drivers else [])
    merged.extend(inbands if inbands else [])
    merged.extend(outbands if outbands else [])
    
    if merged and len(merged) > 0:
        flattened_list = list(itertools.chain(*merged))
        return ' '.join(['"{0}"'.format(item) for item in flattened_list])
    else:
        return 'auto'


class FilterModule(object):
    '''
    custom jinja2 filters for handle HSU response
    '''

    def filters(self):
        return {
            'hsu': hsu,
            'plain': plain
        }
