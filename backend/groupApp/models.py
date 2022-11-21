from xml.dom import ValidationErr
from django.db import models
from django.forms import ValidationError
from core.models import User


class InterestGroup(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=500, default="")
    members = models.ManyToManyField(User, blank=True, related_name="groups_member_in")
    location = models.CharField(max_length=255, default="")
    quote = models.TextField(max_length=500, default="")
    groupAdmin = models.ForeignKey(
        "core.User",
        on_delete=models.DO_NOTHING,
        default=None,
        related_name="groups_admin_in",
    )
    interests = models.ManyToManyField("Interest", blank=True)
    meetingDate = models.DateField(blank=True, null=True)
    groupups = models.ManyToManyField("GroupUp", blank=True)
    sentLikes = models.ManyToManyField(
        "InterestGroup", blank=True, related_name="liked_groups"
    )
    contactInfo = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        null=True,
        to_field="email",
    )

    REQUIRED_FIELDS = ["name", "description", "groupAdmin"]

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=1000, default="")

    REQUIRED_FIELDS = ["name", "description"]

    def __str__(self):
        return self.name


class GroupUp(models.Model):

    group1 = models.ForeignKey(
        "InterestGroup",
        on_delete=models.CASCADE,
        related_name="groupUps_group1",
    )

    group2 = models.ForeignKey(
        "InterestGroup", on_delete=models.CASCADE, related_name="groupUps_group2"
    )
    groupUpAccept = models.BooleanField(default=False)
    isSuperGroupup = models.BooleanField(default=False)

    plannedDate = models.DateField(blank=True, null=True)

    REQUIRED_FIELDS = ["group1", "group2"]

    class Meta:
        unique_together = ("group1", "group2")

    def __str__(self):
        return (
            self.group1.name
            + " "
            + self.group2.name
            + ("(*)" if self.isSuperGroupup else "")
        )
