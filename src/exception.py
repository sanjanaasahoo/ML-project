import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #will tell in which line(& in which file) the error has occured.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

    
    #this function shows how the error message should look like.


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    #error_message is getting populated from this (error_message_detail) function

    def __str__(self):
        return self.error_message
    #the custom exception is raised,  return self.error_message is gonna print the error messages

