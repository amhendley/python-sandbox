import os
import jwt


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjQ3OTk0YzZiLTg2YmUtNGMxMi04YzdiLTAzMmVkZDgxMGRhNCJ9.eyJqdGkiOiJhZGZlMTJjOC0yZWFhLTQ0ZjMtYTUyOC03ZmJlMTI4ZjQxZTMiLCJzdWIiOiJKV1QgR2VuZXJhdG9yIiwiYXVkIjoibWUuY29tIiwiaXNzIjoiQUNNRSIsImV4cCI6MTYzNDEwNDk1NCwibmJmIjoxNjM0MDE4NTU0LCJ1c2VyIjoiam9obi5kb2UiLCJyb2xlIjoic2FsZXMifQ.fSyQ_81rqx8kMj2gMo_c1dY5jz465c1GzjnmudYx22Oc5yqX88SDkeKnGfECZPweQVlCrx7Bcquhe3G1sUYF0Bf6JUzJueER22viG__mTiSlwySm_BHlUl1GC-K33fAeemttgWiBeLa2wwDcL-Z02Rwucw8vDKWU_sXPDByqAKXkaOVyyM2i2kXCdo2tW3bczOcTUWgrHEmBkTsUHHwDVk6eml2tykBY1GWc8rUg4VQe_xLxKZxO8_AX8uz-8N5-xLcZZ-cotjHf76xtMYSmxFmP5U8GuCB9zFfuupDVO09ugcsk8M2_oRdJLTsV25tQsi6ouXfT-pRr2zNTxipc6g'

with open(f'{os.environ["HOME"]}/.ssh/id_rsa.pub', 'r') as key_file:
    key = ''.join(key_file.readlines())

decoded_jwt = jwt.decode(jwt=token,
                         key=key,
                         algorithms='RS256',
                         options={
                             "require": [
                                 "exp",
                                 'nbf',
                                 "iss",
                                 "sub",
                                 "user",
                                 'role'
                             ]
                         },
                         verify=True,
                         audience='me.com')

print(decoded_jwt)
