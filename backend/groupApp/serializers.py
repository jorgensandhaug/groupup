from django.forms import ValidationError
from rest_framework import serializers
from .models import InterestGroup, Interest, GroupUp
from authorization.serializers import UserSerializer


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ["name", "description"]

    def create(self, validated_data):
        interest = Interest.objects.create(**validated_data)
        return interest

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class GroupUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUp
        fields = [
            "group1",
            "group2",
            "groupUpAccept",
            "isSuperGroupup",
            "plannedDate",
            "id",
        ]

    def create(self, validated_data):
        # Outgoing: We should ensure that the requester is a member of this group
        group1 = validated_data.get("group1")
        # Incoming
        group2 = validated_data.get("group2")

        isSuperGroupup = validated_data.get("isSuperGroupUp")
        mirror_groupup = (
            GroupUp.objects.all()
            .filter(group2_id=group1.id)
            .filter(group1_id=group2.id)
        )

        # Update existing object if the mirror groupup exists.
        # This implies that both groups have approved to groupup
        if mirror_groupup.exists():
            groupup = mirror_groupup.first()

            # Ignore request if the groupup is already approved
            if groupup.groupUpAccept:
                return groupup

            if not groupup.isSuperGroupup and isSuperGroupup:
                groupup.isSuperGroupup = True

            groupup.groupUpAccept = True
            groupup.save()
            return groupup
        else:
            groupup = GroupUp.objects.create(**validated_data)
            return groupup

    def update(self, instance, validated_data):
        instance.group1 = validated_data.get("group1", instance.group1)
        instance.group2 = validated_data.get("group2", instance.group2)
        instance.plannedDate = validated_data.get("plannedDate", instance.plannedDate)
        instance.save()
        return instance

    def validate(self, data):
        if "group1" not in data or "group2" not in data:
            return data
        if data["group1"] == data["group2"]:
            raise serializers.ValidationError("A group cannot GroupUp with oneself.")
        return data


def interestToId(interest):
    obj, created = Interest.objects.get_or_create(
        name=interest["name"], description=interest["description"]
    )
    return obj.id


class InterestGroupSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    # members = UserSerializer(many=True)
    # matches = GroupMatchSerializer(many=True)

    class Meta:
        model = InterestGroup
        fields = [
            "id",
            "name",
            "description",
            "location",
            "quote",
            "members",
            "interests",
            "meetingDate",
            "groupAdmin",
            "contactInfo",
        ]
        read_only_fields = ["members", "groupAdmin", "contactInfo"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["groupAdmin"] = request.user
        validated_data["contactInfo"] = request.user

        interests = validated_data.pop("interests")
        interestGroup = InterestGroup.objects.create(**validated_data)

        interestArr = list(map(lambda i: interestToId(i), interests))

        interestGroup.interests.set(interestArr)
        interestGroup.members.set([request.user])
        interestGroup.save()
        return interestGroup

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.meetingDate = validated_data.get("meetingDate", instance.meetingDate)
        instance.location = validated_data.get("location", instance.location)
        instance.quote = validated_data.get("quote", instance.quote)

        if "interests" in validated_data:
            interests = list(
                map(lambda i: interestToId(i), validated_data.get("interests"))
            )
            instance.interests.set(interests)

        instance.save()
        return instance
