from datetime import datetime

from django.utils.timesince import timesince

from rest_framework import serializers

from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # Class extending from the DRF ModelSerializer class

    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        '''
        model corresponds to the model we're trying to build the model for.
        Then we need to tell Django which fields of the model we want to
        serialize.

        Some examples for fields - 
        fields = '__all__'     Specifies that we want all of the fields
        fields = ('title', 'description, 'body')     Specifies we want some.
        exclude = ('id',)       Shows everything besides what you specify.
        '''
        model = Article
        exclude = ('id',)

    def get_time_since_publication(self, object):
        # Function to get the time since it was first published. Returns
        # time_delta to the above time_since_publication field. Django 
        # convention stipulates that the field calls a function with 
        # get_ in front of the same field name since the SerializerMethodField
        # was called.
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        # Check that the description and title are different. 
        # (Object-level Serializer Validation)
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and Description must differ from one another!')
        return data

    def validate_title(self, value):
        # Field-level validation check for the title field
        if len(value) < 30:
            raise serializers.ValidationError('Title must be at least 30 characters long!')
        return value

'''
Below implemention using just the base Serializer class from the Django
REST Frmamework

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update (self, instance, validated_data):
        # function to update an existing Article.
        # if there is no data being passed, just use the current one.
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', 
                                                    instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', 
                                                    instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        # Check that the description and title are different. 
        # (Object-level Serializer Validation)
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and Description must differ from one another!')
        return data

    def validate_title(self, value):
        # Field-level validation check for the title field
        if len(value) < 60:
            raise serializers.ValidationError('Title must be at least 60 characters long!')
        return value
'''