"""Model definition of group_accounts application: GroupAccount"""
from django.db import models


class GroupAccount(models.Model):
    """Model definition of account used to share with members in a group"""

    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    creation_date_time = models.DateTimeField(null=True, blank=True)
    last_modification_date_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metadata for group_account model"""

        db_table = "group_account"

    def __str__(self):
        return f"[{self.id}] 최종 변경일시: {self.last_modification_date_time}"
