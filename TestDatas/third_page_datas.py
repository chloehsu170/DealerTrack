# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description: Datas for the third page
'''

#positive multiply
success_numbers=[{"first_number":12,"second_number":"34","check":"408"},
            {"first_number":-12,"second_number":1234567834,"check":-14814814008},
            {"first_number":-1234556789,"second_number":-11,"check":13580124679},
            {"first_number":"1 23","second_number":123,"check":123},
            {"first_number":" 123 ","second_number":" 1qq ","check":123},
            {"first_number":"       1.23","second_number":123,"check":123},
            {"first_number":"1.23","second_number":"12.3","check":12},
            {"first_number":"-1qq","second_number":"-12q3","check":12},
            ]

#negative multiply
wrong_numbers=[{"first_number":"Keys.SPACE","second_number":123,"check":'NaN'},
            {"first_number":123,"second_number":"Keys.TAB","check":'NaN'},
            {"first_number":"123!","second_number":"*123","check":'NaN'},
            {"first_number":"qa1","second_number":"qa2","check":'NaN'},]