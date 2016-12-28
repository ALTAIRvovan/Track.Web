from django.contrib.auth.forms import UserCreationForm
from .models import User
import logging
import json

logger = logging.getLogger(__name__)

class UserRegistrationForm(UserCreationForm):

    def is_valid(self):
        logger.debug("UserRegistrationForm has sent. Form data:" + json.dumps(self.data))
        return super().is_valid()

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name")