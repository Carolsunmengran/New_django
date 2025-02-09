from django.test import TestCase

# Create your tests here.
import  requests,pprint

response = requests.get('http://localhost:7788/api/mgr/customers?action=list_customer')
# response = requests.get('http://localhost:8000/api/mgr/customers?action=add_customer')

pprint.pprint(response.json())