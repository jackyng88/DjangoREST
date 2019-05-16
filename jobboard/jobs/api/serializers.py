from rest_framework import serializers
from jobs.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    # JobOfferSerializer class extending from ModelSerializer

    class Meta:
        model = JobOffer
        fields = '__all__'