# /!/usr/bin/python3
# coding:utf-8
__author__ = 'Yanwen Xu'
'''
description: datas for the first page
'''
# positive login
success=[{"user":"asdf123"},{"user":"asdf 123"},{"user":"!234344!"},{"user":" "},{"user":"!"},
        {"user":"!2343qdsdsfdfdfdczzzzzz"},{"user":" 23abc "}]
        

# negative login
wrong_datas=[{"user":""}]

#positive addition
success_numbers=[{"first_number":"12","second_number":"34","check":"66"},
            {"first_number":"-12","second_number":"1234567834","check":"1234567822"},
            {"first_number":"-1234556789","second_number":"-11","check":"-1234556800"},
            {"first_number":" 123 ","second_number":" 1qq ","check":"124"},
            {"first_number":"       1.23","second_number":"123","check":"124"},
            {"first_number":"1.23","second_number":"12.3","check":"13"},
            {"first_number":"-1qq","second_number":"-12q3","check":"-13"},
            {"first_number":"1 23","second_number":"123","check":'124'},
            ]

#negative addition
wrong_numbers=[{"first_number":"Keys.SPACE","second_number":"123","check":'NaN'},
            {"first_number":"123","second_number":"Keys.TAB","check":'NaN'},
            {"first_number":"123!","second_number":"*123","check":'NaN'},
            {"first_number":"qa1","second_number":"qa2","check":'NaN'}]
