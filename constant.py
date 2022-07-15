from oauth2client.service_account import ServiceAccountCredentials

CSS_SELECTOR = {
    "buttons": "div.pv-top-card-v2-ctas.pt2.display-flex",
    "employees": "span.link-without-visited-state.t-bold.t-black--light",
    "profile_detail": "div.entity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light",
    "result": "div.pb2.t-black--light.t-14",
    "profile_heading": "h1.text-heading-xlarge.inline.t-24.v-align-middle.break-words",
    "desc": "div.text-body-medium.break-words",
    "emp_button": "div.display-flex.mt2.mb1",
    "company_detail": "div.block.mt2",
    "company_website": "a.ember-view.org-top-card-primary-actions__action",
    # driver.find_elements_by_css_selector('div.artdeco-dropdown.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view')
    # 'more_button': 'div.artdeco-dropdown.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-right.ember-view',
    'more_button': 'button.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2',

    'more_button_dropdown': 'span.display-flex.t-normal.flex-1',
    'connect_inside_button': 'button.mr2.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view',
    'add_note_button': 'button.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1',
    # 'more_button' :'button.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1',
    #             textarea.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3
    'note_area': 'textarea.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3',

    'send_button': 'button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view',
    'connct_button': 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action',
    'connect_button': '#ember73',
}

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/cred.json", scope)

# sheet_name = 'Sourcing Campaign Worksheet'
# tab_name = 'Oleander LinkedIn Outreach'
# sheet_name = 'Linkedin Outreach Report '
# tab_name = 'request_accepted'
sheet_name='test_prospects'
tab_name='Sheet1'

# shukirit_cookies = [{'domain': '.linkedin.com', 'expiry': 1644996476, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=TB13:s=T:r=T:a=T:p=T:g=3730:u=728:x=1:i=1644938738:t=1644996474:v=2:sig=AQFyXQ2jRz2rDl7-HvmsuceF6eReuhIw"'}, {'domain': '.linkedin.com', 'expiry': 1647530734, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQFNNVpU-ds6dwAAAX79_SbMcCJX9jhPq3tZbKo6nILFRLc7Maef8izU2WkDsw-z63NQ24u_ItYmvI4EK1oC6XU8eEieIH2N'}, {'domain': '.linkedin.com', 'expiry': 1647530733, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQK6xesrGCBOBAAAAX79_SGUsezmliE0TexYn2MWoxvaJg5hhTZ9XXxLUfMASawumGJgt7Q28E7qGe3wDjQAuA'}, {'domain': '.linkedin.com', 'expiry': 1647530733, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQImVuOIpXGBGQAAAX79_SGUK9kIaIeSw8XABkECetkvp21F-ZOFYUUIV8zY6iZE5fIgkWKqq779X_9ckt9EzkvnfjyPatCtp0UiidhiE_pRNBKUQXthLgzTzO1mR5Pi_AKzfHJmsl72nMiv7HWcraGeGd8OI4AXr5KhTYufJfcwSl9R0Om75Uhylq7dTV0LYgr64IOJdFpSR5HbCjsJx0qcflNp33M8Oygg2dcJG7ZMAMyGiZgEdvjW-nvAASBnMdafkmzHOS97T0l9t6u-aHIwScj5ARGcKGnx8I8'}, {'domain': '.linkedin.com', 'expiry': 1652714731, 'httpOnly': False, 'name': '_guid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1c8ef2e9-a0fd-4abc-aac2-45e15caa0264'}, {'domain': '.linkedin.com', 'expiry': 1652714741, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'd97a606b-1a51-47d3-9220-efab4f9416e9'}, {'domain': '.www.linkedin.com', 'expiry': 1708052329, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&20220215152116464a8b8f-5f4c-4360-8454-85f6f5891f01AQHTw6M-t1JJIcQ_zfEIiv1JHr2xkVwo"'}, {'domain': '.linkedin.com', 'expiry': 1652714638, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.www.linkedin.com', 'expiry': 1676474638, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDAS1KaAUBRYUmAAABfv37swkAAAF_Igg3CVYAnNXNposMMavwVoKnbN2aUXRwe4XcBBymMCHje8O6cGFCeHFZ4SPIROqPpDXfTOKteGWoo1GKZdJ-ZcCox3PB3fZDTa32feFtO6fbeVuzOvYI6VG3'}, {'domain': '.linkedin.com', 'expiry': 1660490478, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-637568504%7CMCIDTS%7C19039%7CMCMID%7C47063406115669082434185683244861213363%7CMCAAMLH-1645543278%7C12%7CMCAAMB-1645543278%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1644945678s%7CNONE%7CvVersion%7C5.1.1'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=en-us'}, {'domain': '.linkedin.com', 'expiry': 1647530734, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQFNNVpU-ds6dwAAAX79_SbMcCJX9jhPq3tZbKo6nILFRLc7Maef8izU2WkDsw-z63NQ24u_ItYmvI4EK1oC6XU8eEieIH2N'}, {'domain': '.www.linkedin.com', 'expiry': 1660490727, 'httpOnly': False, 'name': 'li_theme_set', 'path': '/', 'secure': True, 'value': 'app'}, {'domain': '.www.linkedin.com', 'expiry': 1708010478, 'httpOnly': False, 'name': 'G_ENABLED_IDPS', 'path': '/', 'secure': False, 'value': 'google'}, {'domain': '.www.linkedin.com', 'expiry': 1660490727, 'httpOnly': False, 'name': 'li_theme', 'path': '/', 'secure': True, 'value': 'system'}, {'domain': '.linkedin.com', 'expiry': 1708052329, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&5f9218ab-f760-4634-8a74-c799082fd168"'}, {'domain': '.www.linkedin.com', 'expiry': 1646148327, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'secure': True, 'value': 'Asia/Calcutta'}, {'domain': '.www.linkedin.com', 'expiry': 1652714638, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:1087441763785260119"'}, {'domain': '.linkedin.com', 'expiry': 1647530559, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'secure': False, 'value': '47286134682053674484240604695375329656'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'sdsc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '22%3A1%2C1644938031730%7ECONN%2C03sP4%2B5kqKtIx3TbCphiyIW63N%2BI%3D'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}]
# akshit
cookies = [{'domain': '.linkedin.com', 'expiry': 1655617932, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=VB82:s=V:r=V:a=V:p=V:g=3024:u=54:x=1:i=1655531540:t=1655617930:v=2:sig=AQE9djEX6pNgC9Ea1bTi_zZeoAUX7HSc"'}, {'domain': '.linkedin.com', 'expiry': 1658123539, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQFPCPqmPR1njQAAAYF1Xon4KmV2LzrBveUDkmUC4dmTvgdBcU6_GPd0Yd6cDRZhQvNh4Quq3ZDNfKYsA4bU_v8r0qamKgsa'}, {'domain': '.linkedin.com', 'expiry': 1671083539, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-637568504%7CMCIDTS%7C19162%7CMCMID%7C46880810913543432773976509797509481939%7CMCAAMLH-1656136339%7C12%7CMCAAMB-1656136339%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1655538739s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C2003617119'}, {'domain': '.linkedin.com', 'expiry': 1663307539, 'httpOnly': False, 'name': '_guid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'c4082e4e-3cf3-44de-912d-ac2a22d662b8'}, {'domain': '.linkedin.com', 'expiry': 1658123539, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQJ-_ZSCiBmXRwAAAYF1XoiIwSos0RSnfraEIG-LSC_yM7A9JKku6qx3x1e67V29pcznffthStrHnLpuB989nA'}, {'domain': '.linkedin.com', 'expiry': 1658123539, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQKjMYFw1KcjUAAAAYF1XoiI9orPw5m0Enat90QXtS009F1kxefv86Wnuhq6e1kH16IMSExRTc_HmKN-_7dguhic-h6L5LF9JtkspJ4T5J9dGeX9lMR1aOtoYUy_Kw0Et4S8LVxxJ3xXvRe1PwMRkM5SbcaqowQ19vGblfDSCdJc7w2rRSAdra-rgMSCvH5w5gPhI5VUDKq7XvhQtldL9cACwzT5H1If664At49doD2iApQNXsj_OELBSdrwY1GWSqpfvFOCHAKmH9L2OiQ-4U7bozDz1mC-9rCbUZo'}, {'domain': '.linkedin.com', 'expiry': 1663307541, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'f0c8c7ec-5fbb-4185-8b40-2fdc2dd19d8e'}, {'domain': '.linkedin.com', 'expiry': 1718645360, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&1f2b81b9-0de0-4b6a-8407-afd8abfe7029"'}, {'domain': '.www.linkedin.com', 'expiry': 1671083536, 'httpOnly': False, 'name': 'li_theme', 'path': '/', 'secure': True, 'value': 'light'}, {'domain': '.www.linkedin.com', 'expiry': 1687067530, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDATelIp4FIx3lAAABgXVeZjIAAAGBmWrqMk0Ap22dzSCIh8jkSmgE1hBWjlsGjyX7MITnSJKasZmV7KjVM2uGFgD2e8kcT5XMo0JdUiBK_u4hgXXs4vdJAnLVNuCZz99yooLMBmPoIIDC6ioz_OsP'}, {'domain': '.www.linkedin.com', 'expiry': 1718645360, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&20220618055147fe7c03c4-07f8-4895-84f6-bcc95386c7a0AQHO8cKDZz28_90G6LACe3OZ4_kzX5WQ"'}, {'domain': '.linkedin.com', 'expiry': 1663307530, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=en-us'}, {'domain': '.linkedin.com', 'expiry': 1658123539, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQFPCPqmPR1njQAAAYF1Xon4KmV2LzrBveUDkmUC4dmTvgdBcU6_GPd0Yd6cDRZhQvNh4Quq3ZDNfKYsA4bU_v8r0qamKgsa'}, {'domain': '.www.linkedin.com', 'expiry': 1671083536, 'httpOnly': False, 'name': 'li_theme_set', 'path': '/', 'secure': True, 'value': 'app'}, {'domain': '.www.linkedin.com', 'expiry': 1718603512, 'httpOnly': False, 'name': 'G_ENABLED_IDPS', 'path': '/', 'secure': False, 'value': 'google'}, {'domain': '.www.linkedin.com', 'expiry': 1656741136, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'secure': True, 'value': 'Asia/Calcutta'}, {'domain': '.www.linkedin.com', 'expiry': 1663307530, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:0044831515793762415"'}, {'domain': '.linkedin.com', 'expiry': 1658123539, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'secure': False, 'value': '47378657956061687424026299066103838232'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}]
cookies = [{'domain': '.linkedin.com', 'expiry': 1655618828, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=VB10:s=V:r=V:a=V:p=V:g=3932:u=30:x=1:i=1655532437:t=1655618826:v=2:sig=AQFsXY3iUgKo52bd-tS8aRkqkAI2OwvL"'}, {'domain': '.linkedin.com', 'expiry': 1671084437, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-637568504%7CMCIDTS%7C19162%7CMCMID%7C73580107761490146181962427217113264284%7CMCAAMLH-1656137237%7C12%7CMCAAMB-1656137237%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1655539637s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1511591200'}, {'domain': '.linkedin.com', 'expiry': 1663308436, 'httpOnly': False, 'name': '_guid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'e4acf2d6-cdf8-4db8-9a7a-9c69dde0bb01'}, {'domain': '.linkedin.com', 'expiry': 1658124436, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQHjzHAEF-wJxwAAAYF1bDhyF4TNWHPyVNzPdCCKpJEV86Dc7V5ET1Pg25wLeCGkU8vSxzSbjChbiV3BbGqCdVDgIDxwp30q'}, {'domain': '.linkedin.com', 'expiry': 1658124435, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQLVYMtOKGMEOQAAAYF1bDcIBsUxaTl_X9ip00d586_DlJqqTLjXBqRscB8jaSlncptn39kWvHlwtRdE57ORXQ'}, {'domain': '.linkedin.com', 'expiry': 1658124435, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQJwuOLttbksUgAAAYF1bDcIJlNeISokKm_reg7lq7SLN7hOPmIaj5LpTgZPxfwjhecNDNGHVbt83Rap2PmYDq8Udcq1FuBWCJjVxpfdVjkHNHUD5N-hbWWjvs10ZYMlxbjNDeyzw4S4BErfVDBn7K6xGTIkKibYRk2v2S-HnS7hMxaUebKwk0s3MCU9dTGcZS-zNE56oEHHMKu76UnU1YnSMObIgNgK85ZBWm62Qr4cnSam2q4r0udbw5ED5MeYBceM9kLjCKMWNir9HyqXg8cXTW1uzAw9YNX9dPM'}, {'domain': '.linkedin.com', 'expiry': 1663308438, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'c455f0cd-a8f2-489a-a100-f7b71b4e844f'}, {'domain': '.linkedin.com', 'expiry': 1718646264, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&e780c6a3-f91c-47fb-829e-5610091e8e0b"'}, {'domain': '.www.linkedin.com', 'expiry': 1671084431, 'httpOnly': False, 'name': 'li_theme', 'path': '/', 'secure': True, 'value': 'light'}, {'domain': '.www.linkedin.com', 'expiry': 1687068427, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDATh6BMYF8boqAAABgXVsFDcAAAGBmXiYN04AZ5dnLpKK7F5BPwrsOmrYt9H4uKU_DlJS6SXr3WnNbCJma85SzQlCBah_N46VyKRu9o94gJczCn51yLALWeMmryL066PiKwjECpeIxxJFtgofF55Y'}, {'domain': '.www.linkedin.com', 'expiry': 1718646264, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&202206180606510e3e65dd-b116-408c-8ba9-2a65b00ae731AQH0PM0vTiVlTyNQ_CKF_5VGhIwkrqSN"'}, {'domain': '.linkedin.com', 'expiry': 1663308427, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=en-us'}, {'domain': '.linkedin.com', 'expiry': 1658124436, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQHjzHAEF-wJxwAAAYF1bDhyF4TNWHPyVNzPdCCKpJEV86Dc7V5ET1Pg25wLeCGkU8vSxzSbjChbiV3BbGqCdVDgIDxwp30q'}, {'domain': '.www.linkedin.com', 'expiry': 1671084431, 'httpOnly': False, 'name': 'li_theme_set', 'path': '/', 'secure': True, 'value': 'app'}, {'domain': '.www.linkedin.com', 'expiry': 1718604413, 'httpOnly': False, 'name': 'G_ENABLED_IDPS', 'path': '/', 'secure': False, 'value': 'google'}, {'domain': '.www.linkedin.com', 'expiry': 1656742031, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'secure': True, 'value': 'Asia/Calcutta'}, {'domain': '.www.linkedin.com', 'expiry': 1663308427, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:6658692610218748292"'}, {'domain': '.linkedin.com', 'expiry': 1658124437, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'secure': False, 'value': '74094867352938935212014479113664512855'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}]
#cookies = [{'domain': '.linkedin.com', 'expiry': 1653563680, 'httpOnly': False, 'name': 'lidc', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': '"b=VB35:s=V:r=V:a=V:p=V:g=3414:u=562:x=1:i=1653494342:t=1653563680:v=2:sig=AQHk8HDOozCrWF6PvlC6s2f32VcGQYbt"'},
#            {'domain': '.linkedin.com', 'expiry': 1656086341, 'httpOnly': False, 'name': 'lms_ads', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': 'AQFK6ViGfg_0igAAAYD78V3vGtUle6gxEQFhBlYwmMKb82tj0Q_Nmz_2gZxXgdWKteONbA2JEW-k2pLLnSlpnkpqns4g_KD4'},
#            {'domain': '.linkedin.com', 'expiry': 1656086340, 'httpOnly': False, 'name': 'AnalyticsSyncHistory',
#             'path': '/', 'sameSite': 'None', 'secure': True,
#             'value': 'AQKTYKegDTvMbAAAAYD78VyVDziIrvf37vkXgWbrY92RQf1f8C3b3eihPeaucBL9eDz_Npfgg4xSH6zA8MQe8g'},
#            {'domain': '.linkedin.com', 'expiry': 1656086340, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': 'AQIyaoETfzr9XQAAAYD78VyVDWYwfcGHQcbmahu4s-2PkgQVLeTICywyEjrvzYAVsj09dcVhe5l7ZBz-rr_7LAagS1nRjOWVjYb7Djt3XXWhTt0qA1YBy6sq4LP4NHH95A8MS5taLcDMw6F4TRQYUj5qFnuOU71qU5iqqXCpg744U9DUKzI-ewpzeXN4HCw940N8KeSVnQsiP1b0n-8KaSrtZKXh9y98x4zXti6jrFq-59H11ZnIdq6OTpGpQx2LgeAPNZvOt3sXglkuL3IIHuNKxOloOiYiPIrTqRU'},
#            {'domain': '.linkedin.com', 'expiry': 1661270340, 'httpOnly': False, 'name': '_guid', 'path': '/',
#             'sameSite': 'None', 'secure': True, 'value': 'a3a15036-baa3-4672-b76c-54ed8ab85ffc'},
#            {'domain': '.linkedin.com', 'expiry': 1669046340, 'httpOnly': False,
#             'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False,
#             'value': '-637568504%7CMCIDTS%7C19138%7CMCMID%7C62307084461137418132859871494126748481%7CMCAAMLH-1654099140%7C12%7CMCAAMB-1654099140%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1653501540s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1187700158'},
#            {'domain': '.linkedin.com', 'expiry': 1661270342, 'httpOnly': False, 'name': 'li_sugr', 'path': '/',
#             'sameSite': 'None', 'secure': True, 'value': '16143941-1dc0-4599-a27f-27809280f636'},
#            {'domain': '.linkedin.com', 'expiry': 1716608127, 'httpOnly': False, 'name': 'bcookie', 'path': '/',
#             'sameSite': 'None', 'secure': True, 'value': '"v=2&80362a55-ed77-4d50-879d-a741785e7ffd"'},
#            {'domain': '.www.linkedin.com', 'expiry': 1669046338, 'httpOnly': False, 'name': 'li_theme', 'path': '/',
#             'secure': True, 'value': 'light'},
#            {'domain': '.www.linkedin.com', 'expiry': 1685030335, 'httpOnly': True, 'name': 'li_at', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': 'AQEDAS1AwWcEr8rGAAABgPvxSOgAAAGBH_3M6E4AyXxfWUfOi-2-gCEwVH1hWo1EcgMVMl5yMGwFpfFeZ4HncOG7unbhg35b8XMubFf5GKFTxA4-42exXss9oCw9hrxqYlxS0BmssuwCXUeFq1OXMIuu'},
#            {'domain': '.www.linkedin.com', 'expiry': 1716608127, 'httpOnly': True, 'name': 'bscookie', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': '"v=1&202205251557549d604639-4790-4ed6-8306-2ef024ebc0a6AQHxsJSoHbR7tjWttSfa3v0GFijBk0hQ"'},
#            {'domain': '.linkedin.com', 'expiry': 1661270335, 'httpOnly': False, 'name': 'liap', 'path': '/',
#             'sameSite': 'None', 'secure': True, 'value': 'true'},
#            {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None',
#             'secure': True, 'value': 'v=2&lang=en-us'},
#            {'domain': '.linkedin.com', 'expiry': 1656086341, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/',
#             'sameSite': 'None', 'secure': True,
#             'value': 'AQFK6ViGfg_0igAAAYD78V3vGtUle6gxEQFhBlYwmMKb82tj0Q_Nmz_2gZxXgdWKteONbA2JEW-k2pLLnSlpnkpqns4g_KD4'},
#            {'domain': '.www.linkedin.com', 'expiry': 1669046338, 'httpOnly': False, 'name': 'li_theme_set', 'path': '/',
#             'secure': True, 'value': 'app'},
#            {'domain': '.www.linkedin.com', 'expiry': 1716566276, 'httpOnly': False, 'name': 'G_ENABLED_IDPS',
#             'path': '/', 'secure': False, 'value': 'google'},
#            {'domain': '.www.linkedin.com', 'expiry': 1654703938, 'httpOnly': False, 'name': 'timezone', 'path': '/',
#             'secure': True, 'value': 'Asia/Calcutta'},
#            {'domain': '.www.linkedin.com', 'expiry': 1661270335, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/',
#             'sameSite': 'None', 'secure': True, 'value': '"ajax:4839196844456069747"'},
#            {'domain': '.linkedin.com', 'expiry': 1656086340, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/',
#             'secure': False, 'value': '62489593572596306542846102083512447114'},
#            {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'sdsc', 'path': '/', 'sameSite': 'None',
#             'secure': True, 'value': '22%3A1%2C1653494252119%7EJAPP%2C0faytBIKSrZYoJKDV%2FhtHf%2BgrIUg%3D'},
#            {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg',
#             'path': '/', 'secure': False, 'value': '1'}]

# message = "Hi {},\n\n" \
#           "Can't offer BMWs to your next tech hires?\n\n" \
#           "Hiring for tech is tough right, some say tougher than raising funds.\n\n" \
#           "Startups funded by Sequoia & Accel chose us to find vetted developers that are available to join " \
#           "immediately.\n\n" \
#           "Is this something relevant to you right now?\n\n" \
#           "Thanks,"

# message = "Hi,\n" \
#           "I am looking to add engineering talent to my team. Let me know if you can help us with our requirements.\n" \
#           "I am looking for React Native, Node JS, React JS & Django developers.\n" \
#           "Please share your contact info to expedite our engagement.\n" \
#           "More about the company - http://getdefault.in\n\n" \
#           "Thanks !!"



# message = "Hi, \n" \
#           "I’m looking for developers for the project I’m working on and I think you can be a great addition. \n" \
#           "If you could share your Resume, I can take a look and take this discussion forward. \n" \
#           "Cheers!"

# message = "Hi,\n" \
#           "I am looking for a technical Resume Writer to help me with a project at my company.\n\n" \
#           "If you are interested please fill this form:\n" \
#           "https://getdefault.zohorecruit.in/jobs/Careers/45931000001231103/Resume-Writer?source=CareerSite\n\n" \
#           "Best of luck!"

# message = "Hi,\n" \
#           "Work at the top 1% companies in India (Swiggy, Zenoti, Airtel, OYO, etc) and get a salary bump of 40% - 100%.\n" \
#           "We at Default focused on quality and pay for your skills.\n\n" \
#           "If this seems relevant to you,then let's connect.\n" \
#            "Cheers,\n" \
#           "Akshit Rungta"

message="Hi,\n"\
    "Thanks for accepting my request. \n\n"\
    "I am good at django framework Do you have any opening for me. \n"

# message = "Hi, {} \n" \
#           "Happy to connect with you.\n" \
#           "I’m good at training and development and have experience of 2 years in HR\n" \
#           "Looking forward to discuss with you if you’ve any requirements related to HR\n" \
#           "Please do let me know\n" \
#           "Thanks and regards,\n" \
#           "Vanshika"
