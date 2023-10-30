import requests
import json

# url = "https://webhook.site/41ff38ef-74ef-475c-a4bf-23f26b119020/api/v2/registration/aadhaar/generateOtp"
# url = "https://webhook.site/41ff38ef-74ef-475c-a4bf-23f26b119020/v2/registration/aadhaar/generateOtp"
url = "https://healthidsbx.abdm.gov.in/api/v2/registration/aadhaar/generateOtp"

payload = json.dumps({
  "aadhaar": "gv0oLtfOd4T34MSqf6W0Z0rT6Es6ZO81+qmJ2VYnpe5Jc4S4DT12mqiu4cpJG8xosNgZ8Thxq70I4Ej/Vpks8K6Hg1DI+nuR71TJy8Eu6rpMuQyUomit6EG5PdwETER3LdDEbNpLkjAEXoi7vn11hq0GmYEvjk/+VsPynjFoJ/duJgNkSxrd104X+3Od/7ttr10qaLTEOyTzK8HkslXo6Xm9QOu/GZ2zL90C30O9WfTVzDZJUzf5zdRnDcZsxJbj0hMlfWx9I36WiGUTEhFAIIrQgH0lelC39KDh1Z82RMEz1Kdhq7QizBJPjFcGr+HmjFDMiheT1FmJwcVOv8oziZ9ipVlrKB/QwSVY7IOWjGIuXWiltKAUkHVznK2eYXJ0hF3LlQjZlbBAAxZLVY2TRyy3unAkDyBcfWRJGoD0e2S22+5f+GB1LLr+y3OS8QvYW4+CmRQRRXNdiWGdXWZAfS+CbV/yfwEHbL8kaFqbrYX6A3vY6JovLhbDe0L/2a0hSVszNbjSuCWCADJizp8kzuamV2IFrrwgn21AHqXuy+MqKFm2z51kCm7IfVyZi9PdrJeVOr2doeJ2F3M1Nv+OItxVycKHbB+z/B5RnQW8+2G/FMisfKgojL5PQvsm//h5Io27uuFiS0bB8kYc82gRN6r4vsg07Zt1/dMaTSHVvlA="
})
headers = {
  'accept': '*/*',
  'Accept-Language': 'en-US',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBbFJiNVdDbThUbTlFSl9JZk85ejA2ajlvQ3Y1MXBLS0ZrbkdiX1RCdkswIn0.eyJleHAiOjE2OTc4MjQzMzQsImlhdCI6MTY5NzgwMjczNCwianRpIjoiNTA0MDAwNWItOGZjMS00NzUzLTgxYjYtMjZmMWRkZDBmYjMwIiwiaXNzIjoiaHR0cHM6Ly9kZXYubmRobS5nb3YuaW4vYXV0aC9yZWFsbXMvY2VudHJhbC1yZWdpc3RyeSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJiZWM5OTcyZS04MzE2LTRkMjItOGI5OS1lZWU5ZDg3ZGIwZWIiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJTQlhfMDA0MjAwIiwic2Vzc2lvbl9zdGF0ZSI6ImQzYmEyMTJlLTU1NTItNDhjYS05MzkwLTYxYzNhYTMwNGFmMyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2xvY2FsaG9zdDo5MDA3Il0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJoaXUiLCJvZmZsaW5lX2FjY2VzcyIsImhlYWx0aElkIiwiT0lEQyIsImhpcCJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IlNCWF8wMDQyMDAiOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJjbGllbnRJZCI6IlNCWF8wMDQyMDAiLCJjbGllbnRIb3N0IjoiMTAuMjMzLjY5LjE5NyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LXNieF8wMDQyMDAiLCJjbGllbnRBZGRyZXNzIjoiMTAuMjMzLjY5LjE5NyJ9.cwbCYK5Lj98bQRbv5RNxfO-9Fv7u8t0-rPsezgwlCl-bdRObkK5GCESlTVGPs2phPTfBCLc0wi49zwKb1xWyMjnTyBXmCsszu9xXkI2fJMTODJrC8SpiTg32nSa8lJAMWchISKXkem7v60h0MAL8eaVahcig-crymtTCzv7rofYUwrvclY1q1MgsJjcXX6p-F4Cvn2W25K0ULXqN4Dp5ZEmp3uyucT7etTay31Ji5jhrocMf49jyi8Rsrco7lFAelz1B0WSrbDUznDxJ_dza2z1TdlzA1G86vIgQgZ2Er7M7dkepgBvI7fVPyQrjrkdwWgFVZe2uSz_bfnM0q611og'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.content)