import os
import sys

class housingexception(Exception):

    def __init__(self, error_message:Exception, error_detail:sys)-> str:

        super().__init__(error_message)
        self.error_message = housingexception.detailed_error_message(error_message = error_message, error_detail = error_detail)
    
    
    @staticmethod
    def detailed_error_message(error_message:Exception, error_detail:sys)-> str:
        """
        error message : Exception object
        error detail : object of sys module
        """
        _,_ , exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in the script : [{file_name} in the line number : {line_number}] error_message :[{error_message}]"
        
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return housingexception.__name__.str()