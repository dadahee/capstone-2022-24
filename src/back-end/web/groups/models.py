"""Model definition of groups application: Group"""
from django.db import models
from django.utils import timezone
from group_accounts.models import GroupAccount
from providers.models import Provider


class Group(models.Model):
    """Model definition of Group composed of leader and members"""

    STATUS_CHOICES = (
        ("Recruiting", "모집중"),
        ("Recruited", "모집완료"),
        ("Reviewing", "검토중"),
        ("Watching", "관람중"),
    )
    id = models.BigAutoField(primary_key=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, db_column="providerId")
    group_account = models.ForeignKey(GroupAccount, on_delete=models.CASCADE, db_column="groupAccountId")
    status = models.CharField(max_length=10, default="Recruiting", choices=STATUS_CHOICES)
    creation_date_time = models.DateTimeField(default=timezone.now, db_column="creationDateTime")
    start_watching_date_time = models.DateTimeField(null=True, blank=True, db_column="startWatchingDateTime")
    end_watching_date_time = models.DateTimeField(null=True, blank=True, db_column="endWatchingDateTime")

    def __str__(self):
        return f"[{self.get_status_display()}] {self.provider} 모임 #{self.id}"
