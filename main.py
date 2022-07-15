# from .googleSheet_operations import getInput
# from .constant import sheet_name, tab_name
import time

import googleSheet_operations
import constant
from action import crm_li_outreach, generate_accepted_request_report


def main():
    data, sheet = googleSheet_operations.getInput(constant.sheet_name, constant.tab_name)
    # data, sheet = googleSheet_operations.getInput('Recruitment - Top funnel outreach', 'Resume Maker')
    # data, sheet = googleSheet_operations.getInput('testing_sheet', 'testing')
    # print(str(data[0]['message'].format('gourab')))
    # linkedin_list = googleSheet_operations.processData(data)
    # print(constant.message)
    linkedin_list = [i['Linkedin'] for i in data if i['Request Sent'] == '']
    print(linkedin_list)
    crm_li_outreach(linkedin_list, constant.message, sheet)
    time.sleep(20)
    # print(linkedin_list)

    # generate_accepted_request_report(sheet)


# if __name__ == "__main__":
#     print(constant.message)
#     # main()

main()
