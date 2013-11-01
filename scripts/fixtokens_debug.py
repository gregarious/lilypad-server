#!/usr/bin/env python

# script to fix tokens to ones fixed in the script (necessary until real auth is attempted by client)

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

try:
	feeny = User.objects.get(username='feeny')
	feeny.auth_token = Token('cce9b356c38ed8f3d0a59f2ca9d4cb108e92631f')
except User.ObjectDoesNotExist:
	pass

try:
	turner = User.objects.get(username='turner')
	turner.auth_token = Token('f66dd627a2c9d22c540025cea178ab32e23045af')
except User.ObjectDoesNotExist:
	pass
