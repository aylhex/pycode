#!/usr/bin/env python
#coding:utf-8
# Author:   --<cj>
# Purpose: 
# Created: 2013/11/4

import sys
import read_data
if __name__=='__main__':
    dist_path_list=[]
    res_path_list=[
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201310\31\1151',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201310\31\1157',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201310\31\1717',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\01\1144',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\01\1630',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\01\1914',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\01\1947',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\01\2150',
        '\\10.20.220.119\dubarelease\updata\UpdateIndex_kav2010\backFile\1509\201311\02\1730',
    ]
    for item in res_path_list:        
        dist_item=read_data.path_119to223(item)[0]
        dist_path_list.append(dist_item)
        print dist_item