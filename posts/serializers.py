from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        read_only_fields = ("slug",)


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,  # Для создания и редоктирования, не для чтения
        source='category'  # ПОле ID связи которое ты указываешь, показывает на какое поле смотреть
    )
    time_to_read1 = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'time_to_read', 'category', 'category_id']
        read_only_fields = ("publish_date", "slug")  # Поля только для чтения
        extra_kwargs = {
            'content': {'required': True}
        }  # ПОзволяет менять поведения полей сериализатора

    def get_time_to_read1(self,obj):
        return len(obj.content)/180
